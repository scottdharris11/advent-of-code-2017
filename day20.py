"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 20", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    m = None
    idx = -1
    for i, line in enumerate(lines):
        p = Particle(line)
        a = p.accel()
        if m is None or m > a:
            m = a
            idx = i
    return idx

@runner("Day 20", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    return 0

class Particle:
    """particle structure definition"""
    def __init__(self, s: str):
        pieces = s.split(", ")
        self.position = ([int(x) for x in pieces[0][3:-1].split(",")])
        self.velocity = ([int(x) for x in pieces[1][3:-1].split(",")])
        self.acceleration = ([int(x) for x in pieces[2][3:-1].split(",")])

    def __repr__(self):
        return str((self.position, self.velocity, self.acceleration))

    def accel(self):
        """compute the aggregate velocity for the particle"""
        return sum([abs(x) for x in self.acceleration])

# Data
data = read_lines("input/day20/input.txt")
sample = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""".splitlines()

# Part 1
assert solve_part1(sample) == 0
assert solve_part1(data) == 258

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
