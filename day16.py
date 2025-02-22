"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 16", "Part 1")
def solve_part1(line: str, count: int) -> str:
    """part 1 solving function"""
    programs = [chr(o) for o in range(ord('a'), ord('a')+count)]
    for move in line.split(","):
        if move[0] == 's':
            programs = spin(programs, int(move[1:]))
        elif move[0] == 'x':
            a, b = map(int,move[1:].split("/"))
            programs = exchange(programs, a, b)
        elif move[0] == 'p':
            a, b = move[1:].split("/")
            programs = partner(programs, a, b)
    return "".join(programs)

@runner("Day 16", "Part 2")
def solve_part2(line: str, count: int) -> int:
    """part 2 solving function"""
    return 0

def spin(programs: list[chr], from_end: int) -> list[chr]:
    """perform the spin move"""
    pivot = len(programs) - from_end
    n = programs[pivot:]
    n.extend(programs[:pivot])
    return n

def exchange(programs: list[chr], a: int, b: int) -> list[chr]:
    """exchange programs at the supplied positions"""
    hold = programs[b]
    programs[b] = programs[a]
    programs[a] = hold
    return programs

def partner(programs: list[chr], a: chr, b: chr) -> list[chr]:
    """swap programs at locations based on id"""
    ai = 0
    bi = 0
    for i, p in enumerate(programs):
        if p == a:
            ai = i
        elif p == b:
            bi = i
    return exchange(programs, ai, bi)

# Data
data = read_lines("input/day16/input.txt")[0]
sample = """s1,x3/4,pe/b""".splitlines()[0]

# Part 1
assert solve_part1(sample, 5) == "baedc"
assert solve_part1(data, 16) == "bkgcdefiholnpmja"

# Part 2
assert solve_part2(sample, 5) == 0
assert solve_part2(data, 16) == 0
