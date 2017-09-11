#!/usr/bin/env python
# encoding: utf-8
"""arg wrapper
"""

import argparse

class Arg(object):
    """simple arg wrapper
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-v", "--verbosity", help="increase output verbosity")
        self.parser.add_argument("-i", "--input", help="set the input filename", required=True)
        self.parser.add_argument("-o", "--output", help="set the output filename", required=True)

    def parse(self):
        """parse arguments from command line
        """
        return self.parser.parse_args()

def main_function():
    """the main function
    """
    args = Arg().parse()
    print("input:{0}".format(args.input))
    print("output:{0}".format(args.output))

if __name__ == "__main__":
    main_function()
