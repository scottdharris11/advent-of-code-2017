"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 18", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    registers = {}
    cmd = 0
    while True:
        offset = 1
        command = lines[cmd]
        match command[:3]:
            case "snd":
                r = value(command[4:], registers)
                if r != 0:
                    registers["sound"] = r
            case "set":
                set_command(command, registers)
            case "add":
                add_command(command, registers)
            case "mul":
                mul_command(command, registers)
            case "mod":
                mod_command(command, registers)
            case "rcv":
                r = value(command[4:], registers)
                if r != 0:
                    return registers.get("sound",0)
            case "jgz":
                offset = jump_command(command, registers)
        cmd += offset

@runner("Day 18", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    a_registers = {"p": 0}
    a_queue = []
    b_registers = {"p": 1}
    b_queue = []
    a_cmd = 0
    b_cmd = 0
    while True:
        a_offset = execute_command(lines[a_cmd], a_registers, b_queue, a_queue)
        b_offset = execute_command(lines[b_cmd], b_registers, a_queue, b_queue)
        if a_offset == 0 and b_offset == 0:
            return b_registers.get("send",0)
        a_cmd += a_offset
        b_cmd += b_offset

def execute_command(command: str, registers: dict[str,int], sq: list[int], rq: list[int]) -> int:
    """execute command against the supplied registers"""
    offset = 1
    match command[:3]:
        case "snd":
            sq.append(value(command[4:], registers))
            registers["send"] = registers.get("send",0) + 1
        case "set":
            set_command(command, registers)
        case "add":
            add_command(command, registers)
        case "mul":
            mul_command(command, registers)
        case "mod":
            mod_command(command, registers)
        case "rcv":
            if len(rq) == 0:
                return 0
            registers[command[4:]] = rq[0]
            del rq[0]
        case "jgz":
            offset = jump_command(command, registers)
    return offset

def set_command(command: str, registers: dict[str,int]):
    """set command execution"""
    r, y = command[4:].split()
    registers[r] = value(y, registers)

def add_command(command: str, registers: dict[str,int]):
    """add command execution"""
    r, y = command[4:].split()
    registers[r] = registers.get(r,0) + value(y, registers)

def mul_command(command: str, registers: dict[str,int]):
    """multiply command execution"""
    r, y = command[4:].split()
    registers[r] = registers.get(r,0) * value(y, registers)

def mod_command(command: str, registers: dict[str,int]):
    """modulus command execution"""
    r, y = command[4:].split()
    registers[r] = registers.get(r,0) % value(y, registers)

def jump_command(command: str, registers: dict[str,int]) -> int:
    """jump command execution"""
    offset = 1
    x, y = command[4:].split()
    if value(x, registers) > 0:
        offset = value(y, registers)
    return offset

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
sample2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""".splitlines()

# Part 1
assert solve_part1(sample) == 4
assert solve_part1(data) == 2951

# Part 2
assert solve_part2(sample2) == 3
assert solve_part2(data) == 7366
