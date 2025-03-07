"""utility imports"""
from utilities.runner import runner

class ValueRule:
    """value rule structure"""
    def __init__(self, write: int, move: int, next_state: str):
        self.write = write
        self.move = move
        self.next_state = next_state

    def __repr__(self):
        return str((self.write, self.move, self.next_state))

class StateRule:
    """state rule structure"""
    def __init__(self, state: str, zero: ValueRule, one: ValueRule):
        self.state = state
        self.zero = zero
        self.one = one

    def __repr__(self):
        return str((self.state, self.zero, self.one))

@runner("Day 25", "Part 1")
def solve_part1(start: str, steps: int, states: dict[str,StateRule]) -> int:
    """part 1 solving function"""
    on = set()
    rule = states[start]
    loc = 0
    for _ in range(steps):
        v = 1 if loc in on else 0
        vr = rule.one if v == 1 else rule.zero
        if vr.write != v:
            if vr.write == 1:
                on.add(loc)
            else:
                on.remove(loc)
        loc += vr.move
        rule = states[vr.next_state]
    return len(on)

# Data
data = {
    "A": StateRule("A", ValueRule(1,1,"B"), ValueRule(0,-1,"B")),
    "B": StateRule("B", ValueRule(0,1,"C"), ValueRule(1,-1,"B")),
    "C": StateRule("C", ValueRule(1,1,"D"), ValueRule(0,-1,"A")),
    "D": StateRule("D", ValueRule(1,-1,"E"), ValueRule(1,-1,"F")),
    "E": StateRule("E", ValueRule(1,-1,"A"), ValueRule(0,-1,"D")),
    "F": StateRule("F", ValueRule(1,1,"A"), ValueRule(1,-1,"E"))
}
sample = {
    "A": StateRule("A", ValueRule(1,1,"B"), ValueRule(0,-1,"B")),
    "B": StateRule("B", ValueRule(1,-1,"A"), ValueRule(1,1,"A"))
}

# Part 1
assert solve_part1("A", 6, sample) == 3
assert solve_part1("A", 12586542, data) == 3732
