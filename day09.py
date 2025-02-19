"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 9", "Part 1")
def solve_part1(line: str) -> int:
    """part 1 solving function"""
    return len(line)

@runner("Day 9", "Part 2")
def solve_part2(line: str) -> int:
    """part 2 solving function"""
    return len(line)

# Data
data = read_lines("input/day09/input.txt")[0]
sample = """""".splitlines()[0]

# Part 1
assert solve_part1(sample) == 0
assert solve_part1(data) == 0

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
