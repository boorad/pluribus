import errno
import Queue
import select
import signal
import socket
import threading
import traceback
from multiprocessing.pool import ThreadPool

from pluribus._listen import listen


class BaseServer(object):

    BACKLOG = 5
    stopped = True

    def __init__(self):
        #signal.signal(signal.SIGINT, self.sigint_hander())
        listen()

    def reset(self):
        self._threadpool = None
        self._poll = select.epoll()
        self._connections = {}
        self._events = Queue.Queue()

    def handle_message(self, data, addr):
        raise NotImplementedError()

    def handle_connection(self, client, addr):
        raise NotImplementedError()

    def handle_disconnect(self, client, addr):
        raise NotImplementedError()

    def accept(self):
        emask = select.EPOLLIN | select.EPOLLPRI | select.EPOLLERR | select.EPOLLHUP
        while not self.stopped:
            try:
                client, addr = self._sock.accept()
            except socket.error:
                continue

            client.setblocking(0)

            self._connections[client.fileno()] = (client, addr)
            self._poll.register(client, emask)

            self.queue_event(self.handle_connection, client, addr)

    def close_client(self, fd):
        client, addr = self._connections[fd]
        self._poll.unregister(client)
        del self._connections[fd]
        client.close()
        self.queue_event(self.handle_disconnect, client, addr)

    def poll(self):
        failed = {}
        while not self.stopped:
            events = self._poll.poll(timeout=1)

            for fd, evt in events:
                client, addr = self._connections[fd]
                if evt & select.EPOLLIN or evt & select.EPOLLPRI:
                    msg = ''
                    while not self.stopped:
                        try:
                            chunk = client.recv(4096)
                            if not chunk:
                                failed.setdefault(fd, 0)
                                failed[fd] += 1
                                if failed[fd] > 3:
                                    self.close_client(fd)
                                    del failed[fd]
                                break
                            msg += chunk
                        except socket.error as e:
                            if e.errno in (errno.EWOULDBLOCK, errno.EAGAIN):
                                break
                            else:
                                client.close()
                                raise
                    self.queue_event(self.handle_message, client, addr, msg)
                if evt & select.EPOLLERR or evt & select.EPOLLHUP:
                    self.close_client(fd)

    def queue_event(self, func, *args, **kwargs):
        self._events.put((func, args, kwargs))

    def process_events(self):
        while not self.stopped:
            try:
                func, args, kwargs = self._events.get(timeout=1)
            except Queue.Empty:
                continue

            try:
                func(*args, **kwargs)
            except Exception as e:
                print e
                #traceback.print_last()
            finally:
                self._events.task_done()

    def thread(self, target):
        thread = threading.Thread(name=target.__name__, target=target)
        thread.start()
        return thread

    def serve(self, host, port):
        self.reset()
        self.stopped = False
        addr = (socket.gethostbyname(host), port)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind(addr)
        self._sock.listen(self.BACKLOG)


        self._accept_thread = self.thread(self.accept)
        self._poll_thread = self.thread(target=self.poll)
        self._event_thread = self.thread(target=self.process_events)

    def sigint_hander(self):
        def handler(signal, frame):
            if not self.stopped:
                self.stop()
        return handler

    def stop(self):
        self.stopped = True
        for fd in self._connections:
            self._connections[fd][0].close()
        self._sock.shutdown(socket.SHUT_RDWR)
        self._sock.close()
        self._poll.close()
        self._accept_thread.join()
        self._poll_thread.join()
        self._event_thread.join()
