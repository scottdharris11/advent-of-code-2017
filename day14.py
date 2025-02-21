"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 14", "Part 1")
def solve_part1(key: str) -> int:
    """part 1 solving function"""
    return len(key)

@runner("Day 14", "Part 2")
def solve_part2(key: str) -> int:
    """part 2 solving function"""
    return len(key)

# Part 1
assert solve_part1("flqrgnkx") == 0
assert solve_part1("amgozmfv") == 0

# Part 2
assert solve_part2("flqrgnkx") == 0
assert solve_part2("amgozmfv") == 0
