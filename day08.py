"""utility imports"""
import re
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 8", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    operations = [Operation(l) for l in lines]
    registers = {}
    for o in operations:
        registers = o.execute(registers)
    mr = None
    for r in registers.values():
        if mr == None or r > mr:
            mr = r
    return mr

@runner("Day 8", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    return len(lines)

OP_PARSE = re.compile(r'([a-z]+) (inc|dec) ([-\d]+) if ([a-z]+) (<|>|==|!=|<=|>=) ([-\d]+)')

class Operation:
    """operation structure"""
    def __init__(self, line: str):
        match = OP_PARSE.match(line)
        self.op_register = match.group(1)
        self.op_amount = int(match.group(3))
        if match.group(2) == "dec":
            self.op_amount *= -1
        self.check_register = match.group(4)
        self.check_condition = match.group(5)
        self.check_amount = int(match.group(6))

    def __repr__(self):
        return str((self.op_register, self.op_amount,
                    self.check_register, self.check_condition, self.check_amount))

    def execute(self, registers: dict[str,int]) -> dict[str,int]:
        """apply operation to supplied registers"""
        value = registers.get(self.op_register, 0)
        cvalue = registers.get(self.check_register, 0)
        match self.check_condition:
            case ">":
                if cvalue <= self.check_amount:
                    return registers
            case "<":
                if cvalue >= self.check_amount:
                    return registers
            case "==":
                if cvalue != self.check_amount:
                    return registers
            case "!=":
                if cvalue == self.check_amount:
                    return registers
            case ">=":
                if cvalue < self.check_amount:
                    return registers
            case "<=":
                if cvalue > self.check_amount:
                    return registers
        registers[self.op_register] = value + self.op_amount
        return registers

# Data
data = read_lines("input/day08/input.txt")
sample = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".splitlines()

# Part 1
assert solve_part1(sample) == 1
assert solve_part1(data) == 4567

# Part 2
assert solve_part2(sample) == -1
assert solve_part2(data) == -1
