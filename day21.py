"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 21", "Part 1")
def solve_part1(lines: list[str], iterations: int) -> int:
    """part 1 solving function"""
    patterns = parse_patterns(lines)
    size, image = on_points(".#./..#/###")
    for _ in range(iterations):
        size, image = adjust_image(size, image, patterns)
    return len(image)

@runner("Day 21", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    patterns = parse_patterns(lines)
    size, image = on_points(".#./..#/###")
    for _ in range(18):
        size, image = adjust_image(size, image, patterns)
    return len(image)

class Pattern:
    """pattern structure"""
    def __init__(self, line: str):
        i, o = line.split(" => ")
        s, on = on_points(i)
        self.in_patterns = alt_patterns(s, on)
        self.in_size = s
        s, on = on_points(o)
        self.out_points = on
        self.out_size = s

    def __repr__(self):
        return str((self.in_size, tuple(self.in_patterns), self.out_size, self.out_points))

    def match(self, points: set[tuple[int,int]]) -> bool:
        """determine if points match the pattern"""
        for p in self.in_patterns:
            if p == points:
                return True
        return False

    def chunk(self, x_offset: int, y_offset: int, points: set[tuple[int,int]]) -> tuple[int,int]:
        """build chunked set of on points based on a size and offset"""
        c = set()
        for y in range(self.in_size):
            for x in range(self.in_size):
                p = (x+x_offset,y+y_offset)
                if p in points:
                    c.add((x,y))
        return c

    def on_pixels(self, x_offset: int, y_offset: int) -> set[tuple[int,int]]:
        """build set of on pixels based on offset"""
        on = set()
        for p in self.out_points:
            on.add((p[0]+x_offset, p[1]+y_offset))
        return on

def adjust_image(size: int, image: set[tuple[int,int]], patterns: list[Pattern]) -> tuple[int,set[tuple[int,int]]]:
    """adjust an image based on current size, on pixels, and supplied patterns"""
    adjusted = set()
    cs = 3
    if size % 2 == 0:
        cs = 2
    chunks = size // cs
    ps = None
    for y in range(chunks):
        y_offset = y * cs
        for x in range(chunks):
            x_offset = x * cs
            for p in patterns[cs]:
                if p.match(p.chunk(x_offset, y_offset, image)):
                    ps = p.out_size
                    adjusted.update(p.on_pixels(x*ps, y*ps))
                    break
    return chunks * ps, adjusted

def on_points(pattern: str) -> tuple[int,set[tuple[int,int]]]:
    """determine the points that are on in the supplied pattern"""
    size = 0
    on = set()
    for y, row in enumerate(pattern.split("/")):
        size += 1
        for x, col in enumerate(row):
            if col == '#':
                on.add((x,y))
    return size, on

def alt_patterns(size: int, points: set[tuple[int,int]]) -> list[set[tuple[int,int]]]:
    """build full set of patterns (rotate/flip) to match"""
    patterns = []
    patterns.append(points)
    for _ in range(3):
        points = rotate(size, points)
        patterns.append(points)
    if size > 2:
        points = flip(size, patterns[0])
        patterns.append(points)
        for _ in range(3):
            points = rotate(size, points)
            patterns.append(points)
    return patterns

def rotate(size: int, points: set[tuple[int,int]]) -> set[tuple[int,int]]:
    """rotate the supplied set of points clockwise"""
    r = set()
    for y in range(size):
        for x in range(size):
            if (x,y) in points:
                r.add((size-y-1, x))
    return r

def flip(size: int, points: set[tuple[int,int]]) -> set[tuple[int,int]]:
    """rotate the supplied set of points clockwise"""
    r = set()
    for y in range(size):
        for x in range(size):
            if (x,y) in points:
                r.add((x, size-y-1))
    return r

def parse_patterns(lines: list[str]) -> dict[int,Pattern]:
    """parse patterns from the input"""
    patterns = {}
    for line in lines:
        p = Pattern(line)
        group = patterns.get(p.in_size, [])
        group.append(p)
        patterns[p.in_size] = group
    return patterns

# Data
data = read_lines("input/day21/input.txt")
sample = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""".splitlines()

# Part 1
assert solve_part1(sample, 2) == 12
assert solve_part1(data, 5) == 186

# Part 2
assert solve_part2(data) == 3018423
