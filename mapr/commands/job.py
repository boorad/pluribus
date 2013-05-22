"""Send a new job to the mapr cluster.

A ``job`` is a python file or module with appropriately named or annotated
objects defining the MapReduce job.

Jobs MUST define a map operation and a reduce operation. They MAY define
partition operations, input readers, output writers, or other settings.

"""


def add_arguments(subparsers):
    parser = subparsers.add_parser('job', help='Send a new job to the master.')
    parser.add_argument('module',
                        help='A module containing map and reduce methods.')
    parser.add_argument('-m', '--master', default='localhost:7787',
                        help='Which mapr master to connect to (%(default)s)')
    parser.set_defaults(func=job_handler)


def job_handler(args):
    pass
