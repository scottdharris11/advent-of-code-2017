"""utility imports"""
from utilities.data import read_lines, parse_integers
from utilities.runner import runner

@runner("Day 10", "Part 1")
def solve_part1(line: str, size: int) -> int:
    """part 1 solving function"""
    values = list(range(size))
    seqs = parse_integers(line, ",")
    skip = 0
    index = 0
    for seq in seqs:
        a = index
        b = offset(index, seq-1, size)
        for _ in range(seq//2):
            hold = values[a]
            values[a] = values[b]
            values[b] = hold
            a = offset(a, 1, size)
            b = offset(b, -1, size)
        index = offset(index, seq + skip, size)
        skip += 1
    return values[0] *  values[1]

@runner("Day 10", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    return len(lines)

def offset(cur: int, move: int, size: int) -> int:
    """determine new offset for move amount"""
    idx = cur + move
    while idx < 0:
        idx += size
    return idx % size

# Data
data = read_lines("input/day10/input.txt")[0]
sample = """3, 4, 1, 5""".splitlines()[0]

# Part 1
assert solve_part1(sample, 5) == 12
assert solve_part1(data, 256) == 38415

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
