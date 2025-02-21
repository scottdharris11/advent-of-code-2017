"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 13", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    severity = 0
    for depth, size, cycle in parse_scanners(lines):
        if depth % cycle == 0:
            severity += depth * size
    return severity

@runner("Day 13", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    scanners = parse_scanners(lines)
    delay = 0
    while True:
        for depth, _, cycle in scanners:
            if (delay+depth) % cycle == 0:
                break
        else:
            break
        delay += 1
    return delay

def parse_scanners(lines: list[str]) -> list[tuple[int,int]]:
    """parse scanners from input"""
    scanners = []
    for depth, size in [[int(x) for x in line.split(": ")] for line in lines]:
        cycle = (size - 1) * 2
        scanners.append((depth, size, cycle))
    return scanners

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
assert solve_part2(sample) == 10
assert solve_part2(data) == 3878062
