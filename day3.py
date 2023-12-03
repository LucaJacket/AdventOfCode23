import re
import math


symbols = {}


def init_symbols(input):
    for row in range(140):
        for col in range(140):
            if input[row][col] not in ".0123456789":
                symbols[(row, col)] = []
    for i, line in enumerate(input):
        for n in re.finditer(r"\d+", line):
            adjacent_positions = [(row, col) for row in (i - 1, i, i + 1) for col in range(n.start() - 1, n.end() + 1)]
            for position in adjacent_positions & symbols.keys():
                symbols[position].append(int(n.group()))


def solution_1():
    return sum([sum(n_list) for n_list in symbols.values()])


def solution_2():
    return sum([math.prod(n_list) for n_list in symbols.values() if len(n_list) == 2])


if __name__ == "__main__":
    input = open("input.txt").readlines()
    init_symbols(input)
    print(solution_1())
    print(solution_2())
