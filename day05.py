"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 5", "Part 1")
def solve_part1(lines: list[str]):
    """part 1 solving function"""
    jumps = [int(l) for l in lines]
    steps = 0
    ji = 0
    while 0 <= ji < len(jumps):
        ni = ji + jumps[ji]
        steps += 1
        jumps[ji] += 1
        ji = ni
    return steps

@runner("Day 5", "Part 2")
def solve_part2(lines: list[str]):
    """part 2 solving function"""
    jumps = [int(l) for l in lines]
    steps = 0
    ji = 0
    while 0 <= ji < len(jumps):
        ni = ji + jumps[ji]
        steps += 1
        if jumps[ji] >= 3:
            jumps[ji] -= 1
        else:
            jumps[ji] += 1
        ji = ni
    return steps

# Data
data = read_lines("input/day05/input.txt")
sample = """0
3
0
1
-3""".splitlines()

# Part 1
assert solve_part1(sample) == 5
assert solve_part1(data) == 358131

# Part 2
assert solve_part2(sample) == 10
assert solve_part2(data) == 25558839
