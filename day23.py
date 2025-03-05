"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 23", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    registers = {"mul": 0}
    cmd = 0
    while 0 <= cmd < len(lines):
        offset = execute_command(lines[cmd], registers)
        cmd += offset
    return registers["mul"]

@runner("Day 23", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    return 0

def execute_command(command: str, registers: dict[str,int]) -> int:
    """execute command against the supplied registers"""
    offset = 1
    match command[:3]:
        case "set":
            set_command(command, registers)
        case "sub":
            sub_command(command, registers)
        case "mul":
            mul_command(command, registers)
        case "jnz":
            offset = jump_command(command, registers)
    return offset

def set_command(command: str, registers: dict[str,int]):
    """set command execution"""
    x, y = command[4:].split()
    registers[x] = value(y, registers)

def sub_command(command: str, registers: dict[str,int]):
    """add command execution"""
    x, y = command[4:].split()
    registers[x] = registers.get(x,0) - value(y, registers)

def mul_command(command: str, registers: dict[str,int]):
    """multiply command execution"""
    x, y = command[4:].split()
    registers["mul"] = registers.get("mul",0) + 1
    registers[x] = registers.get(x,0) * value(y, registers)

def jump_command(command: str, registers: dict[str,int]) -> int:
    """jump command execution"""
    offset = 1
    x, y = command[4:].split()
    if value(x, registers) != 0:
        offset = value(y, registers)
    return offset

def value(s: str, registers: dict[str,int]):
    """get value for register or constant variable"""
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return int(s)
    return registers.get(s,0)

# Data
data = read_lines("input/day23/input.txt")

# Part 1
assert solve_part1(data) == 6241

# Part 2
assert solve_part2(data) == 0
