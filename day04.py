"""utility imports"""
from utilities.data import read_lines
from utilities.runner import runner

@runner("Day 4", "Part 1")
def solve_part1(lines: list[str]):
    """part 1 solving function"""
    valid = 0
    for line in lines:
        if no_duplicates(line):
            valid += 1
    return valid

@runner("Day 4", "Part 2")
def solve_part2(lines: list[str]):
    """part 2 solving function"""
    valid = 0
    for line in lines:
        if no_duplicates(line) and no_anagrams(line):
            valid += 1
    return valid

def no_duplicates(pp: str) -> bool:
    """validate a passphrase"""
    words = set()
    for w in pp.split(" "):
        if w in words:
            return False
        words.add(w)
    return True

def no_anagrams(pp: str) -> bool:
    """validate a passphrase"""
    words = set()
    for w in pp.split(" "):
        letters = [0] * 26
        for l in w:
            i = ord(l) - ord('a')
            letters[i] += 1
        lc = "".join(str(x) for x in letters)
        if lc in words:
            return False
        words.add(lc)
    return True

# Data
data = read_lines("input/day04/input.txt")
assert no_duplicates("aa bb cc dd ee") is True
assert no_duplicates("aa bb cc dd aa") is False
assert no_duplicates("aa bb cc dd aaa") is True
assert no_anagrams("abcde fghij") is True
assert no_anagrams("abcde xyz ecdab") is False
assert no_anagrams("a ab abc abd abf abj") is True
assert no_anagrams("iiii oiii ooii oooi oooo") is True
assert no_anagrams("oiii ioii iioi iiio") is False

# Part 1
assert solve_part1(data) == 386

# Part 2
assert solve_part2(data) == 208
