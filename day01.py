"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 1", "Part 1")
def solve_part1(line: str):
    """part 1 solving function"""
    length = len(line)
    total = 0
    for i in range(length):
        compi = i+1
        if i == length-1:
            compi = 0
        if line[i] == line[compi]:
            total += int(line[i])
    return total

@runner("Day 1", "Part 2")
def solve_part2(line: str):
    """part 2 solving function"""
    length = len(line)
    steps = int(length/2)
    total = 0
    for i in range(length):
        compi = i+steps
        if compi >= length:
            compi = compi - length
        if line[i] == line[compi]:
            total += int(line[i])
    return total

# Data
data = read_lines("input/day01/input.txt")[0]

# Part 1
assert solve_part1("1122") == 3
assert solve_part1("1111") == 4
assert solve_part1("1234") == 0
assert solve_part1("91212129") == 9
assert solve_part1(data) == 1044

# Part 2
assert solve_part2("1212") == 6
assert solve_part2("1221") == 0
assert solve_part2("123425") == 4
assert solve_part2("123123") == 12
assert solve_part2("12131415") == 4
assert solve_part2(data) == 1054
