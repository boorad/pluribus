from __future__ import absolute_import

try:
    import cPickle as pickle
else:
    import pickle


class Message(object):
    pass


class NewWorker(Message):
    pass


class Heartbeat(Message):
    pass


class NewJob(Message):

    @classmethod
    def serialize(cls, obj):
        data = {
            'name': obj.name,
            'map_': obj.get_map(),
            'reduce_': obj.get_reduce(),
        }
        new_job = NewJob()
        new_job.data = data
        return pickle.dumps(new_job)

    @classmethod
    def unserialize(cls, code):
        new_job = pickle.loads(code)
        return new_job


class StartTask(Message):
    pass


class EndTask(Message):
    pass
