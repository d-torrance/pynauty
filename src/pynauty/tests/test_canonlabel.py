#!/usr/bin/env python

import sys
import copy
from pynauty import canon_label, random_relabel
import pytest


def test_canon_label(graph):
    gname, g, numorbit, grpsize, gens = graph
    clg = canon_label(g)
    x, xs = random_relabel(g)
    clx = canon_label(x)
    clg_ = []
    for y in clg:
        clg_.append(xs[y])
    if clg_ == clx:
        print('canon_label remap is OK')
    elif clg == clx:
        print('canon_label original is OK')
    else:
        print('canon_label dual FAILURE!')
    assert clg_ == clx
