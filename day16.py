"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 16", "Part 1")
def solve_part1(line: str, count: int) -> str:
    """part 1 solving function"""
    programs = [chr(o) for o in range(ord('a'), ord('a')+count)]
    moves = parse_moves(line)
    programs = dance(programs, moves, count)
    return "".join(programs)

@runner("Day 16", "Part 2")
def solve_part2(line: str, count: int) -> str:
    """part 2 solving function"""
    programs = [chr(o) for o in range(ord('a'), ord('a')+count)]
    moves = parse_moves(line)
    sequence = ["".join(programs)]
    while True:
        after = dance(programs, moves, count)
        a = "".join(after)
        if a == sequence[0]:
            break
        sequence.append(a)
        programs = after
    sequence_count = len(sequence)
    offset = 1000000000 % sequence_count
    return sequence[offset]

def parse_moves(line: str) -> list[tuple]:
    """parse move values from line"""
    moves = []
    for move in line.split(","):
        if move[0] == 's':
            moves.append(('s', int(move[1:])))
        elif move[0] == 'x':
            a, b = map(int,move[1:].split("/"))
            moves.append(('x', a, b))
        elif move[0] == 'p':
            a, b = move[1:].split("/")
            moves.append(('p', a, b))
    return moves

def dance(p: list[chr], moves: list[tuple], count: int) -> list[chr]:
    """follow the dance"""
    for move in moves:
        if move[0] == 's':
            p = spin(p, move[1], count)
        elif move[0] == 'x':
            p = exchange(p, move[1], move[2])
        elif move[0] == 'p':
            p = partner(p, move[1], move[2], count)
    return p

def spin(programs: list[chr], from_end: int, count: int) -> list[chr]:
    """perform the spin move"""
    pivot = count - from_end
    n = programs[pivot:]
    n.extend(programs[:pivot])
    return n

def exchange(programs: list[chr], a: int, b: int) -> list[chr]:
    """exchange programs at the supplied positions"""
    hold = programs[b]
    programs[b] = programs[a]
    programs[a] = hold
    return programs

def partner(programs: list[chr], a: chr, b: chr, count: int) -> list[chr]:
    """swap programs at locations based on id"""
    ai = -1
    bi = -1
    for i in range(count):
        if programs[i] == a:
            ai = i
        elif programs[i] == b:
            bi = i
        if ai >= 0 and bi >= 0:
            break
    hold = programs[bi]
    programs[bi] = programs[ai]
    programs[ai] = hold
    return programs

# Data
data = read_lines("input/day16/input.txt")[0]
sample = """s1,x3/4,pe/b""".splitlines()[0]

# Part 1
assert solve_part1(sample, 5) == "baedc"
assert solve_part1(data, 16) == "bkgcdefiholnpmja"

# Part 2
assert solve_part2(sample, 5) == "abcde"
assert solve_part2(data, 16) == "knmdfoijcbpghlea"
