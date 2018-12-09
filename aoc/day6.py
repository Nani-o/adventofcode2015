#!/usr/bin/env python

import re

def parse_instruction(instruction):
    regex = re.compile(r"^(\w*\s*\w*)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)$")
    search = regex.search(instruction)
    action = search.group(1)
    start_x = int(search.group(2))
    start_y = int(search.group(3))
    end_x = int(search.group(4))
    end_y = int(search.group(5))
    return action, start_x, start_y, end_x, end_y

def part1(puzzle_input):
    instructions = puzzle_input.split('\n')
    lights_on = set()
    for instruction in instructions:
        action, start_x, start_y, end_x, end_y = parse_instruction(instruction)
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                light = (x, y)
                if action == "toggle":
                    if light in lights_on:
                        lights_on.remove(light)
                    else:
                        lights_on.add(light)
                if action.endswith('on'):
                    lights_on.add(light)
                if action.endswith('off'):
                    if light in lights_on:
                        lights_on.remove(light)
    return len(lights_on)

def part2(puzzle_input):
    instructions = puzzle_input.split('\n')
    regex = re.compile(r"^(\w*\s*\w*)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)$")
    lights_on = {}
    for instruction in instructions:
        action, start_x, start_y, end_x, end_y = parse_instruction(instruction)
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                light = "{},{}".format(x, y)
                if action == "toggle":
                    if light in lights_on.keys():
                        lights_on[light] += 2
                    else:
                        lights_on[light] = 2
                if action.endswith('on'):
                    if light in lights_on.keys():
                        lights_on[light] += 1
                    else:
                        lights_on[light] = 1
                if action.endswith('off'):
                    if light in lights_on.keys()and lights_on[light] != 0:
                        lights_on[light] -= 1
    return sum(lights_on.values())
