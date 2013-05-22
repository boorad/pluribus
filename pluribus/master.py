from __future__ import absolute_import

from pluribus import job


class Master(object):
    jobs = {}
    tasks = {}
    workers = {}
    host = None
    port = None

    def __init__(self, host=None, port=None):
        self.host = host or '0.0.0.0'
        self.port = port or 7787

    def add_job(self, job_name):
        self.jobs[job_name] = job.Job(job_name)

    def start_job(self, job_name)
        job = self.jobs[job_name]

        map_fn = job.dumps(job.map_)
