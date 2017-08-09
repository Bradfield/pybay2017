#!/usr/bin/env python3

from dictionary import Dictionary


def run_tests():
    """
    Ensure that your dictionary works. Add your own tests here!
    """
    d = Dictionary()
    assert 'a' not in d
    d['a'] = 1
    assert d['a'] == 1
    print('Tests passed')


if __name__ == '__main__':
    run_tests()
