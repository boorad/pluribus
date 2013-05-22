"""Start a mapr master process locally.

A ``master`` process

* maintains cluster, job, and task state,
* partitions jobs into map and reduce tasks,
* sends tasks to workers,
* synchronizes counters.

And, eventually, much more!

"""


def add_arguments(subparsers):
    parser = subparsers.add_parser('master', help='Start a master process.')
    parser.add_argument('-b', '--bind', default='localhost:7787',
                        help='Which address to bind to. (%(default)s)')
    parser.set_defaults(func=start_master_process)


def start_master_process(args):
    pass
