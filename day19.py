"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 19", "Part 1")
def solve_part1(lines: list[str]) -> str:
    """part 1 solving function"""
    diagram = Diagram(lines)
    return follow_route(diagram)[0]

@runner("Day 19", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    diagram = Diagram(lines)
    return follow_route(diagram)[1]

UP = (0,-1)
DOWN = (0,1)
RIGHT = (1,0)
LEFT = (-1,0)

class Diagram:
    """diagram structure"""
    def __init__(self, lines: list[str]):
        self.grid = lines
        self.height = len(lines)
        self.width = 0
        for l in lines:
            self.width = max(self.width, len(l))
        self.start = None
        for i, c in enumerate(lines[0]):
            if c == '|':
                self.start = (i,0)
                break

    def point(self, loc: tuple[int,int]) -> chr:
        """point value of location"""
        row = self.grid[loc[1]]
        if loc[0] >= len(row):
            return ' '
        return row[loc[0]]

    def off_diagram(self, loc: tuple[int,int]) -> bool:
        """determine if location is off diagram"""
        return loc[0] < 0 or loc[1] < 0 or loc[0] > self.width or loc[1] > self.height

def follow_route(d: Diagram) -> tuple[str,int]:
    """follow route till the end"""
    route = ""
    steps = 1
    loc = d.start
    move = DOWN
    while True:
        loc = (loc[0] + move[0], loc[1] + move[1])
        if d.off_diagram(loc):
            break
        p = d.point(loc)
        if p == ' ':
            break
        steps += 1
        match p:
            case '|' | '-':
                continue
            case '+':
                check = [RIGHT, LEFT]
                if move in check:
                    check = [UP, DOWN]
                for m in check:
                    t = (loc[0]+m[0], loc[1]+m[1])
                    if d.off_diagram(t):
                        continue
                    if d.point(t) == ' ':
                        continue
                    move = m
                    break
            case _:
                route += p
    return route, steps

# Data
data = read_lines("input/day19/input.txt")
sample = """     |
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
""".splitlines()

# Part 1
assert solve_part1(sample) == "ABCDEF"
assert solve_part1(data) == "RYLONKEWB"

# Part 2
assert solve_part2(sample) == 38
assert solve_part2(data) == 16016
