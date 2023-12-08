import math
import re

moves = ""
nodes = {}


def init_moves_nodes(input):
    global moves
    global nodes
    moves, input = input.split("\n\n")
    nodes = {
        name: {
            "L": left,
            "R": right
        }
        for name, left, right in [line.split() for line in re.sub("[=(,)]", "", input).split("\n")]}


def steps(start, *end):
    count = 0
    while start not in end:
        start = nodes[start][moves[count % len(moves)]]
        count += 1
    return count


def solution_1():
    return steps("AAA", "ZZZ")


def solution_2():
    ends = [node for node in nodes.keys() if node.endswith("Z")]
    return math.lcm(*[steps(node, *ends) for node in nodes.keys() if node.endswith("A")])


if __name__ == "__main__":
    input = open("input.txt").read()
    init_moves_nodes(input)
    print(solution_1())
    print(solution_2())

