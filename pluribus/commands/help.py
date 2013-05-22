"""Print documentation for the given command.

"""

import imp
import importlib
import sys


def add_arguments(subparsers):
    parser = subparsers.add_parser('help', help='Get help with a command.')
    parser.add_argument('command', nargs='?')
    parser.set_defaults(func=print_command_help)


def print_command_help(args):
    command = args.command
    if command is None:
        print 'You asked for help in general.'
    else:
        path = importlib.import_module('pluribus.commands').__path__
        try:
            imp.find_module(command, path)
        except ImportError:
            print >> sys.stderr, "I don't know that command."
            sys.exit(1)

        module = importlib.import_module('pluribus.commands.%s' % command)
        print module.__doc__

        print 'To see command options, run: %(prog)s %(command)s --help\n' % {
            'prog': 'pluribus',
            'command': command,
        }
