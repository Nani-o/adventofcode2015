#!/usr/bin/env python

import re

def is_nice_string1(string):
    vowels = "aeiou"
    vowel_count = 0
    for vowel in vowels:
        vowel_count += string.count(vowel)
    if vowel_count < 3:
        return False

    regex = re.compile(r'.*([a-z])\1.*')
    if not regex.match(string):
        return False

    banned_strings = ['ab', 'cd', 'pq', 'xy']
    for banned_string in banned_strings:
        if banned_string in string:
            return False

    return True

def is_nice_string2(string):
    regex = re.compile(r'.*([a-z]{2}).*\1.*')
    if not regex.match(string):
        return False

    regex = re.compile(r'.*([a-z])[a-z]\1.*')
    if not regex.match(string):
        return False

    return True


def part1(puzzle_input):
    strings = puzzle_input.split('\n')
    nice_strings = 0
    for string in strings:
        if is_nice_string1(string):
            nice_strings += 1
    return nice_strings

def part2(puzzle_input):
    strings = puzzle_input.split('\n')
    nice_strings = 0
    for string in strings:
        if is_nice_string2(string):
            nice_strings += 1
    return nice_strings
