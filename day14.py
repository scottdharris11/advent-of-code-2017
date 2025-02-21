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
    disk = build_disk(key)
    regions = 0
    cataloged = set()
    for y, row in enumerate(disk):
        for x, b in enumerate(row):
            if b == '0':
                continue
            if (x,y) in cataloged:
                continue
            regions += 1
            explore_region(disk, (x,y), cataloged)
    return regions

def build_disk(key: str) -> list[str]:
    """build disk layout from supplied key"""
    disk = []
    for x in range(128):
        seqs = [ord(c) for c in (key + "-" + str(x))]
        seqs.extend([17, 31, 73, 47, 23])
        sparse = knot_hash(seqs, 256, 64)
        dense = dense_hash(sparse)
        disk.append(hex_to_binary(to_hex(dense)))
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

def to_hex(values: list[int]) -> str:
    """convert array of decimal values into a hex representation"""
    h = ""
    for v in values:
        o = hex(v)[2:]
        if len(o) == 1:
            o = "0" + o
        h += o
    return h

def hex_to_binary(s: str) -> str:
    """bits for the supplied hex char"""
    b = ""
    for v in s:
        b += bin(int(v,16))[2:].zfill(4)
    return b

def explore_region(disk: list[str], loc: tuple[int,int], cataloged: set[tuple[int,int]]):
    """catalog adjacent used spots of disk from supplied loc"""
    if loc in cataloged:
        return
    cataloged.add(loc)
    for m in [(1,0),(-1,0),(0,-1),(0,1)]:
        x = loc[0] + m[0]
        y = loc[1] + m[1]
        if x < 0 or x >= 128 or y < 0 or y >= 128:
            continue
        if disk[y][x] == '1':
            explore_region(disk, (x,y), cataloged)

# Part 1
assert solve_part1("flqrgnkx") == 8108
assert solve_part1("amgozmfv") == 8222

# Part 2
assert solve_part2("flqrgnkx") == 1242
assert solve_part2("amgozmfv") == 1086
