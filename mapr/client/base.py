class Client(object):
    def __init__(self, master_dsn):
        super(Client, self).__init__()

    def connect(self):
        raise NotImplementedError()

    def send(self, msg):
        raise NotImplementedError()

    def receive(self, filter_=None):
        raise NotImplementedError()
