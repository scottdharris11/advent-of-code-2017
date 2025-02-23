"""utility imports"""
from utilities.runner import runner

@runner("Day 17", "Part 1")
def solve_part1(skip: int) -> int:
    """part 1 solving function"""
    cur = Location(0)
    cur.next = cur
    for i in range(1, 2018):
        cur = insert(cur, Location(i), i+1, skip)
    return cur.next.value

@runner("Day 17", "Part 2")
def solve_part2(skip: int) -> int:
    """part 2 solving function"""
    idx = 0
    ione = None
    for i in range(1, 50000001):
        idx = ((idx + skip) % i) + 1
        if idx == 1:
            ione = i
    return ione

class Location:
    """location definition"""
    def __init__(self, value: int):
        self.value = value
        self.next = None

def insert(cur: Location, ins: Location, count: int, skip: int) -> Location:
    """insert a location in the circle"""
    offset = skip % count
    for _ in range(offset):
        cur = cur.next
    ins.next = cur.next
    cur.next = ins
    return ins

# Part 1
assert solve_part1(3) == 638
assert solve_part1(370) == 1244

# Part 2
assert solve_part2(370) == 11162912
