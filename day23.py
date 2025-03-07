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
def solve_part2() -> int:
    """part 2 solving function"""
    # to get to this solution, i had to observe the behavior of the command steps.
    # first off was to determine the impact of "a" starting in a non-zero start.
    # what this did was to adjust the "b" and "c" values to higher amounts.
    # The difference between the "b" and "c" values represented the number of times
    # that the outer loop of the commands would execute.  In the base setup the values
    # were initialized to "81" and were equal meaning that only 1 path through the
    # outer loop would occur.  With "a" populated the commands below were executed:
    #
    # mul b 100
    # sub b -100000
    # set c b
    # sub c -17000
    #
    # b = 108100 (81 x 100 + 100000)
    # c = 125100 (b + 17000)
    #
    # Each increment of the outer loop, "b" was adjusted by 17 (sub b -17), so
    # essentially, the outer loop is going to occur 1000 times.
    #
    # Within each outer loop, "h" (the value we care about) would be incremented once
    # if ("d" * "e" was ever equal to "b"). "d" and "e" are incremented in various ways
    # during the outer loop to arrive at the value of "b" which is what makes the
    # program run forever on the large numbers.  So, by reasoning (and observing
    # incrementally starting at low numbers what was happening), noticed that "h" was
    # only not incrementing by 1 every time that "b" was equal to a prime number such
    # that no combination of "d" and "e" during the loop would ever equal it.  Thus my
    # short solution here to increment the values of b by 17 until reaching c and only
    # incrementing "h" when the increment is not a prime number.
    h = 0
    for n in range(108100,125101,17):
        if not prime(n):
            h += 1
    return h

def prime(n):
    """check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
assert solve_part2() == 909
