"""utility imports"""
from utilities.data import read_lines, parse_integers
from utilities.runner import runner

@runner("Day 10", "Part 1")
def solve_part1(line: str, size: int) -> int:
    """part 1 solving function"""
    seqs = parse_integers(line, ",")
    values = knot_hash(seqs, size, 1)
    return values[0] *  values[1]

@runner("Day 10", "Part 2")
def solve_part2(line: str) -> str:
    """part 2 solving function"""
    seqs = [ord(c) for c in line]
    seqs.extend([17, 31, 73, 47, 23])
    sparse = knot_hash(seqs, 256, 64)
    dense = dense_hash(sparse)
    return to_hex(dense)

def knot_hash(seqs: list[int], size: int, rounds: int) -> list[int]:
    """compute the knot hash using the sequences for the supplied rount count"""
    values = list(range(size))
    skip = 0
    index = 0
    for _ in range(rounds):
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
    return values

def offset(cur: int, move: int, size: int) -> int:
    """determine new offset for move amount"""
    idx = cur + move
    while idx < 0:
        idx += size
    return idx % size

def dense_hash(sparse: list[int]) -> list[int]:
    """reduce the sparse hash to dense"""
    dense = []
    for i in range(0,255,16):
        d = sparse[i]
        for o in range(1,16):
            d ^= sparse[i+o]
        dense.append(d)
    return dense

def to_hex(values: list[int]) -> str:
    """convert array of decimal values into a hex representation"""
    h = ""
    for v in values:
        o = hex(v)[2:]
        if len(o) == 1:
            o = "0" + o
        h += o
    return h

# Data
data = read_lines("input/day10/input.txt")[0]
sample = """3, 4, 1, 5""".splitlines()[0]

# Part 1
assert solve_part1(sample, 5) == 12
assert solve_part1(data, 256) == 38415

# Part 2
assert solve_part2("") == "a2582a3a0e66e6e86e3812dcb672a272"
assert solve_part2("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
assert solve_part2("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
assert solve_part2("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"
assert solve_part2(data) == "9de8846431eef262be78f590e39a4848"
