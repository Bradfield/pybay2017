#!/usr/bin/env python3
import sys


def make_grayscale(indata):
    return indata


if __name__ == '__main__':
    assert len(sys.argv) == 3, 'Usage: solution.py infile.bmp outfile.bmp'
    _, infile, outfile = sys.argv
    indata = open(infile, 'rb').read()
    outdata = make_grayscale(indata)
    open(outfile, 'wb').write(outdata)
    print('ok')
