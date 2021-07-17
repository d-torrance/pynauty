#!/usr/bin/env python

import sys
import copy
from pynauty import isomorphic, delete_random_edge, Version, canon_label, random_relabel
import pytest


def test_canon_label(graph):
    print(Version())
    print('Python version: ' + sys.version)
    print('Testing pynauty.{isomorphic(),certificate(),delete_random_edge(),copy()}')
    gname, g, numorbit, grpsize, gens = graph
    print('%-37s ...' % gname, end=' ')
    sys.stdout.flush()
    clg = canon_label(g)
    x, xs = random_relabel(g)
    clg_ = []
    for y in clg:
        clg_.append(xs[y])
    assert clg_ == canon_label(x)
    e = delete_random_edge(x)
    print('    removed random edge {:<13} ...'.format(str(e)), end=' ')
    assert clg_ != canon_label(x)
