#!/usr/bin/env python

import pytest
from aoc.day2 import part1, part2

def test_part1():
    input = "2x3x4\n1x1x10\n"
    solution = part1(input)
    assert solution == 101

def test_part2():
    input= "2x3x4\n1x1x10\n"
    solution = part2(input)
    assert solution == 48
