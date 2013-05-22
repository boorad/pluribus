"""Start a worker process locally.

A ``worker`` process

* executes map and reduce tasks,
* feeds data back to the master.

"""


def add_arguments(subparsers):
    parser = subparsers.add_parser('worker', help='Start a worker process.')
    parser.add_argument('-m', '--master', default='localhost:7787',
                        help='The address of the master. (%(default)s)')
    parser.set_defaults(func=start_worker_process)


def start_worker_process(args):
    pass
