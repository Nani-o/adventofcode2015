#!/usr/bin/env python

import pytest
from aoc.day3 import part1, part2

test_inputs = [
    "^v",
    "^>v<",
    "^v^v^v^v^v"
]

expected_part1 = [2, 4, 2]
expected_part2 = [3, 3, 11]

@pytest.mark.parametrize("input,expected", list(zip(test_inputs, expected_part1)))
def test_part1(input, expected):
    solution = part1(input)
    assert solution == expected

@pytest.mark.parametrize("input,expected", list(zip(test_inputs, expected_part2)))
def test_part2(input, expected):
    solution = part2(input)
    assert solution == expected
