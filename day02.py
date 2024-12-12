"""utility imports"""
from utilities.data import read_lines, parse_integers
from utilities.runner import runner

@runner("Day 2", "Part 1")
def solve_part1(lines: list[str]):
    """part 1 solving function"""
    checksum = 0
    for line in lines:
        nums = parse_integers(line, "\t")
        checksum += max(nums) - min(nums)
    return checksum

@runner("Day 2", "Part 2")
def solve_part2(lines: list[str]):
    """part 2 solving function"""
    checksum = 0
    for line in lines:
        nums = parse_integers(line, "\t")
        length = len(nums)
        for i in range(length):
            found = False
            for j in range(i+1, length, 1):
                x = nums[i]
                y = nums[j]
                if x % y == 0:
                    checksum += int(x/y)
                    found = True
                    break
                if y % x == 0:
                    checksum += int(y/x)
                    found = True
                    break
            if found:
                break
    return checksum

# Data
data = read_lines("input/day02/input.txt")
sample = """5\t1\t9\t5
7\t5\t3
2\t4\t6\t8""".splitlines()
sample2 = """5\t9\t2\t8
9\t4\t7\t3
3\t8\t6\t5""".splitlines()

# Part 1
assert solve_part1(sample) == 18
assert solve_part1(data) == 42299

# Part 2
assert solve_part2(sample2) == 9
assert solve_part2(data) == 277
