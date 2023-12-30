import itertools

galaxies = [(x, y) for x, l in enumerate(open("input.txt").read().splitlines()) for y, c in enumerate(l) if c == "#"]
galaxies_rows = set(map(lambda g: g[0], galaxies))
galaxies_cols = set(map(lambda g: g[1], galaxies))


def distance(g1: tuple[int, int], g2: tuple[int, int]):
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + (exp - 1) * (
        len(set(range(min(g1[0], g2[0]), max(g1[0], g2[0]) + 1)) - galaxies_rows) +
        len(set(range(min(g1[1], g2[1]), max(g1[1], g2[1]) + 1)) - galaxies_cols))


for exp in 2, 1_000_000:
    print(sum(distance(g1, g2) for g1, g2 in itertools.combinations(galaxies, 2)))
