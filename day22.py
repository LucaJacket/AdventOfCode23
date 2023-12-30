from collections import defaultdict
import re


def drop(stack: list[tuple], skip=-1):
    peaks = defaultdict(lambda: 0)
    falls = 0
    for i, (x1, y1, z1, x2, y2, z2) in enumerate(stack):
        if i == skip:
            continue
        area = [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        peak = max(peaks[(x, y)] for x, y in area) + 1
        stack[i] = (x1, y1, peak, x2, y2, peak + z2 - z1)
        for p in area:
            peaks[p] = peak + z2 - z1
        falls += peak < z1
    return falls


stack = sorted([tuple(map(int, re.findall(r"\d+", l))) for l in open("input.txt").readlines()],
               key=lambda b: b[2])

drop(stack)

falls = {i: drop(stack.copy(), i) for i in range(len(stack))}
print(sum(not v for v in falls.values()))
print(sum(falls.values()))
