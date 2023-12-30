import math
import re

moves, _, *graph = open("input.txt").read().splitlines()
graph = {n: d for n, *d in [re.findall(r"\w+", l) for l in graph]}


def steps(pos: str):
    i = 0
    while not pos.endswith("Z"):
        move = moves[i % len(moves)]
        pos = graph[pos][move == "R"]
        i += 1
    return i


print(steps("AAA"))
print(math.lcm(*map(steps, [x for x in graph if x.endswith("A")])))

