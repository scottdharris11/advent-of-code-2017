"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 18", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    registers = {}
    cmd = 0
    while True:
        done, offset, recovered = execute(lines[cmd], registers)
        if done:
            return recovered
        cmd += offset

@runner("Day 18", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    return 0

def execute(command: str, registers: dict[str,int]) -> tuple[bool,int,int]:
    """execute the given command"""
    offset = 1
    done = False
    recovered = None
    match command[:3]:
        case "snd":
            r = value(command[4:], registers)
            if r != 0:
                registers["sound"] = r
        case "set":
            r, y = command[4:].split()
            registers[r] = value(y, registers)
        case "add":
            r, y = command[4:].split()
            registers[r] = registers.get(r,0) + value(y, registers)
        case "mul":
            r, y = command[4:].split()
            registers[r] = registers.get(r,0) * value(y, registers)
        case "mod":
            r, y = command[4:].split()
            registers[r] = registers.get(r,0) % value(y, registers)
        case "rcv":
            r = value(command[4:], registers)
            if r != 0:
                recovered = registers.get("sound",0)
                done = True
        case "jgz":
            x, y = command[4:].split()
            if value(x, registers) > 0:
                offset = value(y, registers)
    return done, offset, recovered

def value(s: str, registers: dict[str,int]):
    """get value for register or constant variable"""
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return int(s)
    return registers.get(s,0)

# Data
data = read_lines("input/day18/input.txt")
sample = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""".splitlines()

# Part 1
assert solve_part1(sample) == 4
assert solve_part1(data) == 2951

# Part 2
assert solve_part2(sample) == 0
assert solve_part2(data) == 0
