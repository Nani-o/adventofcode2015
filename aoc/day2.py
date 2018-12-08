#!/usr/bin/env python

def part1(puzzle_input):
    dimensions = puzzle_input.rstrip('\n').split('\n')
    total = 0
    for dimension in dimensions:
        l, w, h = map(int, dimension.split('x'))
        square_feet = 2 * l * w + 2 * w * h + 2 * h * l
        total += square_feet

        sorted_dim = sorted([l, w, h])
        smallest_area = sorted_dim[0] * sorted_dim[1]

        total += smallest_area
    return total

def part2(puzzle_input):
    dimensions = puzzle_input.rstrip('\n').split('\n')
    total = 0
    for dimension in dimensions:
        l, w, h = map(int, dimension.split('x'))

        sorted_dim = sorted([l, w, h])
        smallest_perimeter = sorted_dim[0] * 2 + sorted_dim[1] * 2
        total += smallest_perimeter

        ribbon = l * w * h
        total += ribbon
    return total
