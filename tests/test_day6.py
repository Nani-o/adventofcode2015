#!/usr/bin/env python

import pytest
from aoc.day6 import part1, part2

def test_part1():
    input = ("turn on 0,0 through 999,999\n"
             "toggle 0,0 through 999,0\n"
             "turn off 499,499 through 500,500")
    solution = part1(input)
    assert solution == 998996

def test_part2():
    input = ("turn on 0,0 through 0,0\n"
             "toggle 0,0 through 999,999")
    solution = part2(input)
    assert solution == 2000001
