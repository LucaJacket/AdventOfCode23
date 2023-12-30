import re
import math

data = open("input.txt").readlines()
symbols = {(i, j): [] for i, l in enumerate(data) for j, c in enumerate(l) if c not in ".0123456789"}

for i, l in enumerate(data):
    for n in re.finditer(r"\d+", l):
        adj = [(r, c) for r in (i - 1, i, i + 1) for c in range(n.start() - 1, n.end() + 1)]
        for pos in adj & symbols.keys():
            symbols[pos].append(int(n.group()))

print(sum(sum(nums) for nums in symbols.values()))
print(sum(math.prod(nums) for nums in symbols.values() if len(nums) == 2))
