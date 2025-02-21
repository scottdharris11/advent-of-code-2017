"""utility imports"""
from utilities.runner import runner

@runner("Day 14", "Part 1")
def solve_part1(key: str) -> int:
    """part 1 solving function"""
    disk = build_disk(key)
    used = 0
    for row in disk:
        for b in row:
            if b == '1':
                used += 1
    return used

@runner("Day 14", "Part 2")
def solve_part2(key: str) -> int:
    """part 2 solving function"""
    return len(key)

def build_disk(key: str) -> list[str]:
    """build disk layout from supplied key"""
    disk = []
    for x in range(128):
        seqs = [ord(c) for c in (key + "-" + str(x))]
        seqs.extend([17, 31, 73, 47, 23])
        sparse = knot_hash(seqs, 256, 64)
        dense = dense_hash(sparse)
        disk.append(to_binary(dense))
    return disk

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

def to_binary(values: list[int]) -> str:
    """bits for the supplied hex char"""
    b = ""
    for v in values:
        b += bin(v)[2:].zfill(4)
    return b

# Part 1
assert solve_part1("flqrgnkx") == 8108
assert solve_part1("amgozmfv") == 8222

# Part 2
assert solve_part2("flqrgnkx") == 0
assert solve_part2("amgozmfv") == 0
