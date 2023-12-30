from z3 import *
from itertools import combinations

hailstones = [[*map(int, l.replace("@", ",").split(","))] for l in open("input.txt").read().splitlines()]


def intersection(h1, h2):
    h, k = Reals("h k")
    s = Solver()
    s.add(h1[0] + h * h1[3] == h2[0] - k * h2[3])
    s.add(h1[1] + h * h1[4] == h2[1] - k * h2[4])
    s.add(h >= 0)
    s.add(k >= 0)
    s.add(h1[0] + h * h1[3] <= 4e14)
    s.add(h1[0] + h * h1[3] >= 2e14)
    s.add(h1[1] + h * h1[4] <= 4e14)
    s.add(h1[1] + h * h1[4] >= 4e14)
    return s.check() == sat


print(sum(intersection(h1, h2) for h1, h2 in combinations(hailstones, 2)))

a, b, c, u, v, w, x, y, z = Reals("a b c u v w x y z")
s = Solver()
h1, h2, h3 = hailstones[:3]

s.add(a == h1[0] + x * (h1[3] - u))
s.add(b == h1[1] + x * (h1[4] - v))
s.add(c == h1[2] + x * (h1[5] - w))

s.add(a == h2[0] + y * (h2[3] - u))
s.add(b == h2[1] + y * (h2[4] - v))
s.add(c == h2[2] + y * (h2[5] - w))

s.add(a == h3[0] + z * (h3[3] - u))
s.add(b == h3[1] + z * (h3[4] - v))
s.add(c == h3[2] + z * (h3[5] - w))

if s.check() == sat:
    print(s.model()[a].as_long() + s.model()[b].as_long() + s.model()[c].as_long())
