#!/usr/bin/env python

import pytest
from aoc.day5 import part1, part2

def test_part1():
    input = ("ugknbfddgicrmopn\n"
             "aaa\n"
             "jchzalrnumimnmhp\n"
             "haegwjzuvuyypxyu\n"
             "dvszwmarrgswjxmb")
    solution = part1(input)
    assert solution == 2

def test_part2():
    input = ("qjhvhtzxzqqjkmpb\n"
             "xxyxx\n"
             "uurcxstgmygtbstg\n"
             "ieodomkazucvgmuy\n")
    solution = part2(input)
    assert solution == 2
