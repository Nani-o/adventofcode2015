#!/usr/bin/env python

from hashlib import md5

def get_hash_input(secret, zero_count):
    solution = 0
    zeros = "0" * zero_count

    while True:
        hash_input = "{}{}".format(secret, solution).encode('utf-8')
        hash = md5(hash_input).hexdigest()
        if hash[0:zero_count] == zeros:
            return solution
        solution += 1


def part1(puzzle_input):
    secret = puzzle_input
    return get_hash_input(secret, 5)

def part2(puzzle_input):
    secret = puzzle_input
    return get_hash_input(secret, 6)
