#!/usr/bin/env python

import pytest
from aoc.day1 import part1, part2

test_inputs_part1 = [
    "(())",
    "()()",
    "(((",
    "(()(()(",
    "))(((((",
    "())",
    "))(",
    ")))",
    ")())())"
]

test_inputs_part2 = [
    ")",
    "()())"
]

expected_part1 = [0, 0, 3, 3, 3, -1, -1, -3, -3]
expected_part2 = [1, 5]

@pytest.mark.parametrize("input,expected", list(zip(test_inputs_part1, expected_part1)))
def test_part1(input, expected):
    solution = part1(input)
    assert solution == expected

@pytest.mark.parametrize("input,expected", list(zip(test_inputs_part2, expected_part2)))
def test_part2(input, expected):
    solution = part2(input)
    assert solution == expected
