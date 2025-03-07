"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 24", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    magnets = {}
    for i, line in enumerate(lines):
        m = Magnet(i, line)
        for p in m.pins:
            avail = magnets.get(p, [])
            avail.append(m)
            magnets[p] = avail
    max_strength = 0
    for zero in magnets[0]:
        strength = max_chain_strength(zero, 0, magnets, set())
        if max_strength is None or strength > max_strength:
            max_strength = strength
    return max_strength

@runner("Day 24", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    return 0

class Magnet:
    """defines magnet structure"""
    def __init__(self, uid: int, s: str):
        self.uid = uid
        self.pins = [int(p) for p in s.split("/")]
        self.strength = sum(self.pins)

    def __repr__(self) -> str:
        return str((self.uid, self.strength, self.pins))

def max_chain_strength(m: Magnet, prev: int, magnets: dict[int,list[Magnet]], used: set[int]) -> int:
    """find the maximum chain strength for the supplied magnet"""
    used.add(m.uid)
    n = m.pins[0]
    if n == prev:
        n = m.pins[1]
    max_next = 0
    for magnet in magnets[n]:
        if magnet.uid in used:
            continue
        strength = max_chain_strength(magnet, n, magnets, used)
        if max_next is None or strength > max_next:
            max_next = strength
    used.remove(m.uid)
    return m.strength + max_next

# Data
data = read_lines("input/day24/input.txt")
sample = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10""".splitlines()

# Part 1
assert solve_part1(sample) == 31
assert solve_part1(data) == 1859

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
