#!/usr/bin/env python

def get_next_coordinate(coordinate, movement):
        x = coordinate[0]
        y = coordinate[1]
        if movement == "^":
            y += 1
        elif movement == "v":
            y -= 1
        elif movement == ">":
            x += 1
        elif movement == "<":
            x -= 1
        return (x, y)

def part1(puzzle_input):
    movements = puzzle_input.rstrip("\n")
    coordinate = (0, 0)
    houses = set()
    houses.add(coordinate)
    for movement in movements:
        coordinate = get_next_coordinate(coordinate, movement)
        houses.add(coordinate)
    return len(houses)

def part2(puzzle_input):
    movements = puzzle_input.rstrip("\n")
    coordinate_santa = (0, 0)
    coordinate_robot = (0, 0)
    houses = set()
    houses.add(coordinate_santa)
    for movement_santa, movement_robot in zip(movements[::2], movements[1::2]):
        coordinate_santa = get_next_coordinate(coordinate_santa, movement_santa)
        houses.add(coordinate_santa)
        coordinate_robot = get_next_coordinate(coordinate_robot, movement_robot)
        houses.add(coordinate_robot)
    return len(houses)
