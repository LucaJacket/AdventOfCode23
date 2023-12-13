from functools import cache
import re

input = open("input.txt").read().split("\n")


@cache
def combinations(springs, damaged):
    springs = springs.lstrip(".")
    if not damaged:
        return 0 if "#" in springs else 1
    if not springs:
        return 0 if damaged else 1
    if re.match("^#+\\.", springs):
        return combinations(springs[damaged[0] + 1:], damaged[1:] or ()) \
            if re.match("^#{" + str(damaged[0]) + "}\\.", springs) else 0
    return sum(combinations(springs.replace("?", option, 1), damaged) for option in "#.")


def solution_1():
    ways = 0
    for line in input:
        springs, damaged = line.split()
        springs = springs + "."
        damaged = tuple(int(x) for x in damaged.split(","))
        ways += combinations(springs, damaged)
    return ways


def solution_2():
    ways = 0
    for line in input:
        springs, damaged = line.split()
        springs = "?".join([springs] * 5) + "."
        damaged = tuple(int(x) for x in damaged.split(",") * 5)
        ways += combinations(springs, damaged)
    return ways


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
