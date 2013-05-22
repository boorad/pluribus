import marshal
import types

from pluribus import proto


def map_(fn):
    fn._map = True
    return fn

def reduce_(fn):
    fn._reduce = True
    return fn


class Job(object):
    def __init__(self, name, map_=None, reduce_=None):
        self.name = name
        self.map_ = map_
        self.reduce_ = reduce_

    def get_map(self):
        return self.dumps(self.map_)

    def get_reduce(self):
        return self.dumps(self.reduce_)

    def set_map(self, code_string):
        self.map_ = self.loads(code_string)

    def set_reduce(self, code_string):
        self.reduce_ = self.loads(code_string)

    @classmethod
    def dumps(cls, fn):
        return marshal.dumps(fn.func_code)

    @classmethod
    def loads(cls, code_string):
        code = marshal.loads(code_string)
        return types.FunctionType(code, globals(), code.co_name)


class LocalJob(Job):
    def __init__(self, mod_name)
        self.mod = __import__(mod_name)
        map_ = self.find_method(self.mod, '_map')
        reduce_ = self.find_method(self.mod, '_reduce')
        super(LocalJob, self).__init__(mod_name, map_, reduce_)

    @classmethod
    def find_method(cls, module, method):
        for o in dir(module):
            obj = getattr(module, o)
            if getattr(obj, method, None):
                return obj


def run_as_client(client, job_name):
    msg = proto.NewJob.serialize(LocalJob(job_name))
    client.send(msg)
