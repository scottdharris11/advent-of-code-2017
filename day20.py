"""utility imports"""
import math
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 20", "Part 1")
def solve_part1(lines: list[str]) -> int:
    """part 1 solving function"""
    m = None
    idx = -1
    for i, line in enumerate(lines):
        # find index of particle that has the lowest aggregate acceleration
        # and assume in an infinite world it will be the closest to 0,0,0
        p = Particle(line)
        a = p.accel()
        if m is None or m > a:
            m = a
            idx = i
    return idx

@runner("Day 20", "Part 2")
def solve_part2(lines: list[str]) -> int:
    """part 2 solving function"""
    particles = {}
    for i, line in enumerate(lines):
        particles[i] = Particle(line)
    # This is pretty ugly but achieving the right answer.  Look
    # to potentially optimize.  logic path:
    #
    # Start with Particle map by index
    # Remain = 0
    # check collisions = true
    # While particle map is not empty
	#    if check collisions is true
	#	    check collisions = false
	#   	compare each particle to determine if collision is possible
	#   	for each particle where not collision possible
	#   		increase “remain”
	#   		remove from particle map
	#   move particles to next time step and look for collisions (position equal)
	#   if at least one collision
	#   	check collisions = true (also check every so often if no collision)
	#   	for each collision
	#   		remove from particle map
    remain = 0
    col_check = True
    clock = 0
    times_since_col = 0
    while len(particles) > 0:
        clock += 1
        if col_check:
            col_check = False
            c = set()
            for a, p1 in particles.items():
                for b, p2 in particles.items():
                    if b <= a:
                        continue
                    if can_collide(p1, p2):
                        c.add(a)
                        c.add(b)
            delete = set()
            for i in particles:
                if i in c:
                    continue
                delete.add(i)
                remain += 1
            for d in delete:
                del particles[d]
        times_since_col += 1
        positions = {}
        for i, p in particles.items():
            pos = p.tick()
            cur = positions.get(pos, [])
            cur.append(i)
            positions[pos] = cur
        for _, p in positions.items():
            if len(p) == 1:
                continue
            times_since_col = 0
            col_check = True
            for i in p:
                del particles[i]
        if times_since_col > 25:
            times_since_col = 0
            col_check = True
    return remain

class Particle:
    """particle structure definition"""
    def __init__(self, s: str):
        pieces = s.split(", ")
        self.p = ([int(x) for x in pieces[0][3:-1].split(",")])
        self.v = ([int(x) for x in pieces[1][3:-1].split(",")])
        self.a = ([int(x) for x in pieces[2][3:-1].split(",")])

    def __repr__(self) -> str:
        return str((self.p, self.v, self.a))

    def accel(self) -> int:
        """compute the aggregate velocity for the particle"""
        return sum(abs(x) for x in self.a)

    def tick(self) -> tuple[int,int,int]:
        """adjust location and velocity"""
        x, y, z = self.p
        vx, vy, vz = self.v
        ax, ay, az = self.a
        vx += ax
        vy += ay
        vz += az
        self.v = (vx, vy, vz)
        self.p = (x + vx, y + vy, z + vz)
        return self.p

def can_collide(p1: Particle, p2: Particle) -> bool:
    """determine if the two particles could collide in the future"""
    if not could_intersect(p1.p[0], p1.v[0], p1.a[0], p2.p[0], p2.v[0], p2.a[0]):
        return False
    if not could_intersect(p1.p[1], p1.v[1], p1.a[1], p2.p[1], p2.v[1], p2.a[1]):
        return False
    if not could_intersect(p1.p[2], p1.v[2], p1.a[2], p2.p[2], p2.v[2], p2.a[2]):
        return False
    return True

def could_intersect(p1: int, v1: int, a1: int, p2: int, v2: int, a2: int) -> bool:
    """determine if the two particle paths could possibly intersect in future"""
    # bust out if velocity and acceleration are equal
    if v1 == v2 and a1 == a2:
        return p1 == p2

    # Coefficients for quadratic equation: A*t^2 + B*t + C = 0 (thanks chatgtp)
    a = 0.5 * (a1 - a2)
    b = v1 - v2
    c = p1 - p2

    # Compute the discriminant
    discriminant = b**2 - 4*a*c

    # Check for real solutions
    if discriminant < 0:
        return False

    # Compute possible times of intersection
    t1 = (-b + math.sqrt(discriminant)) / (2 * a) if a != 0 else -c / b
    t2 = (-b - math.sqrt(discriminant)) / (2 * a) if a != 0 else None

    # Filter only valid (non-negative) times
    return (t1 is not None and t1 >= 0) or (t2 is not None and t2 >= 0)

# Data
data = read_lines("input/day20/input.txt")
sample = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""".splitlines()
sample2 = """p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< -7,0,0>, v=<-1,0,0>, a=< 0,0,0>""".splitlines()

# Part 1
assert solve_part1(sample) == 0
assert solve_part1(data) == 258

# Part 2
assert solve_part2(sample2) == 1
assert solve_part2(data) == 707
