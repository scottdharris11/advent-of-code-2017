"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 16", "Part 1")
def solve_part1(line: str, count: int) -> str:
    """part 1 solving function"""
    return ""

@runner("Day 16", "Part 2")
def solve_part2(line: str, count: int) -> int:
    """part 2 solving function"""
    return 0

# Data
data = read_lines("input/day16/input.txt")[0]
sample = """s1,x3/4,pe/b""".splitlines()[0]

# Part 1
assert solve_part1(sample, 5) == "baedc"
assert solve_part1(data, 16) == ""

# Part 2
assert solve_part2(sample, 5) == 0
assert solve_part2(data, 16) == 0
