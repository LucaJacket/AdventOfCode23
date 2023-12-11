import itertools

universe = open("input.txt").read().split("\n")
SIZE = len(universe)

empty_rows = [r for r in range(SIZE) if "#" not in universe[r]]
empty_cols = [c for c in range(SIZE) if "#" not in [universe[r][c] for r in range(SIZE)]]
galaxies = [(r, c) for r in range(SIZE) for c in range(SIZE) if universe[r][c] == "#"]


def distance(galaxy1, galaxy2, expansion):
    exp_rows = sum(1 for r in empty_rows if min(galaxy1[0], galaxy2[0]) < r < max(galaxy1[0], galaxy2[0]))
    exp_cols = sum(1 for c in empty_cols if min(galaxy1[1], galaxy2[1]) < c < max(galaxy1[1], galaxy2[1]))
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1]) + (expansion - 1) * (exp_rows + exp_cols)


def solution_1():
    return sum(distance(galaxy1, galaxy2, 2)
               for galaxy1, galaxy2 in itertools.combinations(galaxies, 2))


def solution_2():
    return sum(distance(galaxy1, galaxy2, 1000000)
               for galaxy1, galaxy2 in itertools.combinations(galaxies, 2))


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
