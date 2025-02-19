"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 9", "Part 1")
def solve_part1(line: str) -> int:
    """part 1 solving function"""
    return score_groups(line)

@runner("Day 9", "Part 2")
def solve_part2(line: str) -> int:
    """part 2 solving function"""
    return len(line)

def score_groups(line: str) -> int:
    """score the supplied line based on groups"""
    group = 0
    garbage = False
    skip = False
    score = 0
    for c in line:
        if skip:
            skip = False
            continue
        if c == '!':
            skip = True
            continue
        if garbage and c != '>':
            continue
        if c == '<':
            garbage = True
        elif c == '>':
            garbage = False
        elif c == '}':
            score += group
            group -= 1
        elif c == '{':
            group += 1
    return score

# Data
data = read_lines("input/day09/input.txt")[0]
assert score_groups("{}") == 1
assert score_groups("{{{}}}") == 6
assert score_groups("{{},{}}") == 5
assert score_groups("{{{},{},{{}}}}") == 16
assert score_groups("{<a>,<a>,<a>,<a>}") == 1
assert score_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert score_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
assert score_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

# Part 1
assert solve_part1(data) == 20530

# Part 2
assert solve_part2(data) == 0
