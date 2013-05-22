from __future__ import absolute_import
import threading

from .base import BaseServer


class MasterServer(BaseServer):

    def __init__(self):
        super(MasterServer, self).__init__()
        self.clients = {}

    def handle_message(self, client, addr, data):
        print data

    def handle_connection(self, client, addr):
        self.clients[addr] = client
        print 'Connection from: %s' % addr[0]

    def handle_disconnect(self, client, addr):
        del self.clients[addr]
        print 'Disconnect: %s' % addr
