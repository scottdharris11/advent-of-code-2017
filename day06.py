"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 6", "Part 1")
def solve_part1(line: str):
    """part 1 solving function"""
    banks = [int(b) for b in line.split()]
    steps, _ = find_redistribute_loop(banks)
    return steps

@runner("Day 6", "Part 2")
def solve_part2(line: str):
    """part 2 solving function"""
    banks = [int(b) for b in line.split()]
    _, loopsteps = find_redistribute_loop(banks)
    return loopsteps

def find_redistribute_loop(banks: list[int]) -> tuple[int,int]:
    """locate the spot at which the redistribution will loop"""
    mb = 0
    mi = 0
    for i, b in enumerate(banks):
        if b > mb:
            mb = b
            mi = i
    steps = 0
    seen = {}
    while True:
        dist = ",".join(str(b) for b in banks)
        if dist in seen:
            return steps, steps - seen[dist]
        seen[dist] = steps
        banks, mi = redistribute(banks, mi)
        steps += 1

def redistribute(banks: list[int], maxi: int) -> tuple[list[int],int]:
    """redistribute memory"""
    todist = banks[maxi]
    banks[maxi] = 0
    di = maxi
    l = len(banks)
    for _ in range(todist):
        di = (di + 1) % l
        banks[di] += 1
    mb = 0
    mi = 0
    for i, b in enumerate(banks):
        if b > mb:
            mb = b
            mi = i
    return banks, mi

# Data
data = read_lines("input/day06/input.txt")[0]
sample = """0   2   7   0""".splitlines()[0]

# Part 1
assert solve_part1(sample) == 5
assert solve_part1(data) == 12841

# Part 2
assert solve_part2(sample) == 4
assert solve_part2(data) == 8038
