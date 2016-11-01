#!/usr/bin/env python

import sys
import zlib
import argparse

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--decompress', action='store_true', help='decompress mode')
    parser.add_argument('-c', '--compress', action='store_true', help='compress mode')
    parser.add_argument('-i', '--input', help='file to read from (default=stdin)')
    parser.add_argument('-o', '--output', help='file to write to (default=stdout)')
    opts = parser.parse_args(args)

    if opts.input and opts.input != '-':
        infile = open(opts.input)
    else:
        infile = sys.stdin

    if opts.output and opts.output != '-':
        outfile = open(opts.output)
    else:
        outfile = sys.stdout

    if opts.decompress:
        op = zlib.decompress
    else:
        op = zlib.compress

    outfile.write(op(infile.read()))


if __name__ == '__main__':
    main(sys.argv[1:])
