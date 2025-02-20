"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 11", "Part 1")
def solve_part1(line: str) -> int:
    """part 1 solving function"""
    return steps_away(line.split(","))

@runner("Day 11", "Part 2")
def solve_part2(line: str) -> int:
    """part 2 solving function"""
    return 0

STEPS = {"ne": [0.5, 0.5], "nw": [-0.5, 0.5], "n": [0.0, 1.0],
         "se": [0.5, -0.5], "sw": [-0.5, -0.5], "s": [0.0, -1.0]}

def steps_away(directions: list[str]) -> int:
    """determine how many steps away from current hexagon by folling directions"""
    ew = 0.0
    ns = 0.0
    for d in directions:
        s = STEPS[d]
        ew += s[0]
        ns += s[1]
    return int(abs(ew) + abs(ns))

# Data
data = read_lines("input/day11/input.txt")[0]

# Part 1
assert solve_part1("ne,ne,ne") == 3
assert solve_part1("ne,ne,sw,sw") == 0
assert solve_part1("ne,ne,s,s") == 2
assert solve_part1("se,sw,se,sw,sw") == 3
assert solve_part1(data) == 743

# Part 2
assert solve_part2(data) == 0
