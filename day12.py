"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 12", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    programs = parse_programs(lines)
    return len(group(0, programs, set()))

@runner("Day 12", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    programs = parse_programs(lines)
    check = list(programs.keys())
    groups = 0
    while len(check) > 0:
        members = group(check[0], programs, set())
        groups += 1
        for m in members:
            check.remove(m)
    return groups

def parse_programs(lines: list[str]) -> dict[int,set[int]]:
    """parse programs"""
    programs = {}
    for line in lines:
        pieces = line.split(" <-> ")
        identifier = int(pieces[0])
        pipes = [int(p) for p in pieces[1].split(",")]
        programs[identifier] = set(pipes)
    return programs

def group(identifier: int, programs: dict[int,set[int]], found: set[int]) -> set[int]:
    """find all the program associations for the supplied identifier"""
    if identifier in found:
        return found
    found.add(identifier)
    for p in programs[identifier]:
        found = group(p, programs, found)
    return found

# Data
data = read_lines("input/day12/input.txt")
sample = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""".splitlines()

# Part 1
assert solve_part1(sample) == 6
assert solve_part1(data) == 130

# Part 2
assert solve_part2(sample) == 2
assert solve_part2(data) == 189
