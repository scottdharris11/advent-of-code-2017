"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 9", "Part 1")
def solve_part1(line: str) -> int:
    """part 1 solving function"""
    return score_groups(line)[0]

@runner("Day 9", "Part 2")
def solve_part2(line: str) -> int:
    """part 2 solving function"""
    return score_groups(line)[1]

def score_groups(line: str) -> tuple[int,int]:
    """score the supplied line based on groups"""
    group = 0
    garbage = False
    skip = False
    score = 0
    gcount = 0
    for c in line:
        if skip:
            skip = False
            continue
        if c == '!':
            skip = True
            continue
        if garbage and c != '>':
            gcount += 1
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
    return score, gcount

# Data
data = read_lines("input/day09/input.txt")[0]
assert score_groups("{}")[0] == 1
assert score_groups("{{{}}}")[0] == 6
assert score_groups("{{},{}}")[0] == 5
assert score_groups("{{{},{},{{}}}}")[0] == 16
assert score_groups("{<a>,<a>,<a>,<a>}")[0] == 1
assert score_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
assert score_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
assert score_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3
assert score_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3
assert score_groups("<>")[1] == 0
assert score_groups("<random characters>")[1] == 17
assert score_groups("<<<<>")[1] == 3
assert score_groups("<{!>}>")[1] == 2
assert score_groups("<!!>")[1] == 0
assert score_groups("<!!!>>")[1] == 0
assert score_groups('<{o"i!a,<{i<a>')[1] == 10

# Part 1
assert solve_part1(data) == 20530

# Part 2
assert solve_part2(data) == 9978
