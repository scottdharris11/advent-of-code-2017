"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 13", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    severity = 0
    for line in lines:
        depth, size = (int(x) for x in line.split(": "))
        if caught(depth, size):
            severity += depth * size
    return severity

@runner("Day 13", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    return len(lines)

def caught(pico: int, size: int) -> bool:
    """determine if the scanner will catch you"""
    every = (size - 1) * 2
    return pico % every == 0

# Data
data = read_lines("input/day13/input.txt")
sample = """0: 3
1: 2
4: 4
6: 4""".splitlines()

# Part 1
assert solve_part1(sample) == 24
assert solve_part1(data) == 3184

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
