#!/usr/bin/env python
from __future__ import absolute_import
import argparse
import sys

from pluribus.commands import commands

def main(argv=None):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title='Commands available')

    for command in commands:
        command.add_arguments(subparsers)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args(argv)

    args.func(args)


if __name__ == '__main__':
    main()
