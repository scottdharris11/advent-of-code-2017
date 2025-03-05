"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

DIRECTIONS = [(0,-1),(1,0),(0,1),(-1,0)]

@runner("Day 22", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    infected = parse_input(lines)
    loc = (0,0)
    direction = 0
    count = 0
    for _ in range(10000):
        node_infected = loc in infected
        direction = turn(direction, node_infected)
        if node_infected:
            infected.remove(loc)
        else:
            count += 1
            infected.add(loc)
        adjust = DIRECTIONS[direction]
        loc = (loc[0]+adjust[0], loc[1]+adjust[1])
    return count

@runner("Day 22", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    infected = dict.fromkeys(parse_input(lines), 'I')
    loc = (0,0)
    direction = 0
    count = 0
    for _ in range(10000000):
        match infected.get(loc, 'C'):
            case 'I':
                direction = turn(direction, True)
                infected[loc] = 'F'
            case 'W':
                count += 1
                infected[loc] = 'I'
            case 'F':
                direction = turn(turn(direction, True), True)
                del infected[loc]
            case 'C':
                direction = turn(direction, False)
                infected[loc] = 'W'
        adjust = DIRECTIONS[direction]
        loc = (loc[0]+adjust[0], loc[1]+adjust[1])
    return count

def turn(direction: int, right: bool) -> int:
    """turn from current direction"""
    direction += 1 if right else -1
    if direction < 0:
        direction = len(DIRECTIONS)-1
    elif direction >= len(DIRECTIONS):
        direction = 0
    return direction

def parse_input(lines: list[str]) -> set[tuple[int,int]]:
    """build set of infected nodes"""
    middle = len(lines) // 2
    infected = set()
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            if col == "#":
                infected.add((x-middle,y-middle))
    return infected

# Data
data = read_lines("input/day22/input.txt")
sample = """..#
#..
...""".splitlines()

# Part 1
assert solve_part1(sample) == 5587
assert solve_part1(data) == 5261

# Part 2
assert solve_part2(sample) == 2511944
assert solve_part2(data) == 2511927
