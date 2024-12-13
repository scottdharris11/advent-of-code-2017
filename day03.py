"""utility imports"""
from utilities.runner import runner

directions = [(1,0),(0,-1),(-1,0),(0,1)]

@runner("Day 3", "Part 1")
def solve_part1(loc: int):
    """part 1 solving function"""
    point = (0,0)
    m = 0
    d = 0
    for _ in range(loc-1):
        npoint = (point[0] + directions[d][0], point[1] + directions[d][1])
        if npoint[0] > m or npoint[0] < -m or npoint[1] > m or npoint[1] < -m:
            if d == 0:
                m += 1
                d = (d + 1) % 4
            else:
                d = (d + 1) % 4
                npoint = (point[0] + directions[d][0], point[1] + directions[d][1])
        point = npoint
    return abs(point[0]) + abs(point[1])

@runner("Day 3", "Part 2")
def solve_part2(loc: int):
    """part 2 solving function"""
    return 0

# Data
data = 368078

# Part 1
assert solve_part1(1) == 0
assert solve_part1(12) == 3
assert solve_part1(23) == 2
assert solve_part1(1024) == 31
assert solve_part1(data) == 371

# Part 2
assert solve_part2(1) == 0
assert solve_part2(data) == 0
