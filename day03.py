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
    point = (0,0)
    m = 0
    d = 0
    grid = [[1]]
    gm = 0
    lastval = 0
    while True:
        npoint = (point[0] + directions[d][0], point[1] + directions[d][1])
        if npoint[0] > m or npoint[0] < -m or npoint[1] > m or npoint[1] < -m:
            if d == 0:
                m += 1
                for row in grid:
                    row.insert(0, 0)
                    row.append(0)
                grid.insert(0, [0]*((m*2)+1))
                grid.append([0]*((m*2)+1))
                gm += 2
                d = (d + 1) % 4
            else:
                d = (d + 1) % 4
                npoint = (point[0] + directions[d][0], point[1] + directions[d][1])
        point = npoint
        gpoint = (m + point[0], m + point[1])
        val = 0
        for a in [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]:
            mpoint = (gpoint[0] + a[0], gpoint[1] + a[1])
            if mpoint[0] > gm or mpoint[0] < 0 or mpoint[1] > gm or mpoint[1] < 0:
                continue
            val += grid[mpoint[1]][mpoint[0]]
        lastval = val
        grid[gpoint[1]][gpoint[0]] = val
        if lastval > loc:
            break
    return lastval

# Data
data = 368078

# Part 1
assert solve_part1(1) == 0
assert solve_part1(12) == 3
assert solve_part1(23) == 2
assert solve_part1(1024) == 31
assert solve_part1(data) == 371

# Part 2
assert solve_part2(10) == 11
assert solve_part2(362) == 747
assert solve_part2(data) == 369601
