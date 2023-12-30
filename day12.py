from functools import cache


def combinations(line: str):
    springs, damaged = line.split()
    springs = "?".join([springs] * rep) + "."
    damaged = tuple(map(int, damaged.split(","))) * rep

    @cache
    def dp(s: int, d: int, r=0):
        if s == len(springs):
            return d == len(damaged)
        if springs[s] in ".?":
            r += dp(s + 1, d)
        try:
            q = s + damaged[d]
            if "." not in springs[s:q] and springs[q] != "#":
                r += dp(q + 1, d + 1)
        except IndexError:
            pass
        return r

    return dp(0, 0)


data = open("input.txt").read().splitlines()
for rep in 1, 5:
    print(sum(map(combinations, data)))
