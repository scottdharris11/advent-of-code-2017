"""utility imports"""
from utilities.runner import runner

A_FACTOR = 16807
B_FACTOR = 48271

@runner("Day 15", "Part 1")
def solve_part1(a: int, b: int) -> int:
    """part 1 solving function"""
    check = int("1"*16,2)
    aligned = 0
    for _ in range(40000000):
        a = generate(a, A_FACTOR)
        b = generate(b, B_FACTOR)
        if a & check == b & check:
            aligned += 1
    return aligned

@runner("Day 15", "Part 2")
def solve_part2(a: int, b: int) -> int:
    """part 2 solving function"""
    return 0

def generate(prev: int, factor: int) -> int:
    """generate next value for a generator"""
    return (prev * factor) % 2147483647

# Part 1
assert solve_part1(65, 8921) == 588
assert solve_part1(873, 583) == 631

# Part 2
assert solve_part2(65, 8921) == 0
assert solve_part2(873, 583) == 0
