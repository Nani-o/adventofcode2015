[![Build Status](https://travis-ci.org/Nani-o/adventofcode2015.svg?branch=master)](https://travis-ci.org/Nani-o/adventofcode2015)

Advent of code 2018
===================

This repo contains my solution for the [Advent of code 2015](https://adventofcode.com/2015/), little late to the party, started with 2018 edition.

Usage
-----

I run aoc.py as a package, which act as a launcher to run the solutions from a file per day with a function per part, the inputs are in a folder named for each day, it's a less sophisticated version of what I saw on this [repo](https://github.com/LinusCDE/AdventOfCode2018).

```
$ python -m aoc.aoc -h
usage: adventofcode.py [-h] [--day DAY] [--part PART]

optional arguments:
  -h, --help            show this help message and exit
  --day DAY, -d DAY     Day of the puzzle to run
  --part PART, -p PART  Part of the puzzle of the day to run

$ python -m aoc.aoc -d 1 -p 1
Day 1 - part 1
==============

solution : 435
time : 0.5951 ms
```

License
-------

MIT

Author Information
------------------

Sofiane MEDJKOUNE
