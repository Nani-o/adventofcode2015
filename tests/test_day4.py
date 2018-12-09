#!/usr/bin/env python

import pytest
from aoc.day4 import part1, part2

test_inputs = [
    "abcdef",
    "pqrstuv"
]

expected_part1 = [609043, 1048970]

@pytest.mark.parametrize("input,expected", list(zip(test_inputs, expected_part1)))
def test_part1(input, expected):
    solution = part1(input)
    assert solution == expected

