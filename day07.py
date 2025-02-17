"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 7", "Part 1")
def solve_part1(lines: list[str]) -> str:
    """part 1 solving function"""
    programs = parse_programs(lines)
    for _, p in programs.items():
        if p.parent is None:
            return p.id
    return "unknown"

@runner("Day 7", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    programs = parse_programs(lines)
    for _, p in programs.items():
        if p.parent is None:
            _, off = program_weight(p.id, programs)
            return off
    return 0

class Program:
    """defines a program structure"""
    def __init__(self, line: str):
        pieces = line.split(" ")
        self.id = pieces[0]
        self.weight = int(pieces[1][1:-1])
        self.parent = None
        self.children = []
        if len(pieces) > 2:
            for i in range(3, len(pieces)):
                self.children.append(pieces[i].replace(",",""))

    def __repr__(self):
        return str((self.id, self.weight, self.parent, self.children))

def parse_programs(lines: list[str]) -> dict[str,Program]:
    """parse and associate programs"""
    programs = {}
    for line in lines:
        p = Program(line)
        programs[p.id] = p
    for i, p in programs.items():
        for c in p.children:
            cp = programs[c]
            cp.parent = i
    return programs

def program_weight(p: str, programs: dict[str,Program]) -> tuple[int,int]:
    """get a program weight or the balance weight needed"""
    p = programs[p]
    if len(p.children) == 0:
        return p.weight, 0
    children = 0
    cweights = []
    for c in p.children:
        cw, off = program_weight(c, programs)
        if off > 0:
            return 0, off
        cweights.append(cw)
        children += cw
    mc = min(cweights)
    for i, cw in enumerate(cweights):
        if cw != mc:
            return 0, programs[p.children[i]].weight - (cw - mc)
    return p.weight + children, 0

# Data
data = read_lines("input/day07/input.txt")
sample = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".splitlines()

# Part 1
assert solve_part1(sample) == "tknk"
assert solve_part1(data) == "mwzaxaj"

# Part 2
assert solve_part2(sample) == 60
assert solve_part2(data) == 1219
