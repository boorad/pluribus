from __future__ import absolute_import

from .base import Client


class DebugClient(Client):
    def connect(self):
        print 'Debugging connection.'

    def send(self, msg):
        print 'Sending message: %r' % msg
