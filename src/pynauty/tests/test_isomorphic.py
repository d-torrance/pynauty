#!/usr/bin/env python

import sys
import copy
from pynauty import isomorphic, delete_random_edge, random_relabel
import pytest


def test_isomorphic(graph):
    gname, g, numorbit, grpsize, gens = graph
    x, xs = random_relabel(g)
    assert isomorphic(g,x)
    e = delete_random_edge(x)
    assert not isomorphic(g,x)
