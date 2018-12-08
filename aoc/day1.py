#!/usr/bin/env python

def part1(puzzle_input):
    floors_up = puzzle_input.count('(')
    floors_down = puzzle_input.count(')')
    return floors_up - floors_down

def part2(puzzle_input):
    index = 0
    floor = 0
    for move in puzzle_input:
        index += 1
        if move == '(':
            floor += 1
        elif move == ')':
            floor -= 1
        if floor == -1:
            return index
