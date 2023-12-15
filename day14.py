table = open("input.txt").read().split("\n")
SIZE = len(table)


def tilt():  # tilt east
    global table
    table = ["#".join("".join(sorted(group)) for group in table[r].split("#")) for r in range(SIZE)]


def rotate():  # rotate 90 degrees clockwise
    global table
    table = ["".join(table[i][r] for i in range(SIZE)[::-1]) for r in range(SIZE)]


def solution_1():
    rotate()
    tilt()
    rotate()
    rotate()
    rotate()
    return sum(table[r].count("O") * (SIZE - r) for r in range(SIZE))


def detect_loop(scores, n=3):
    if 2 < n <= scores.count(scores[-1]):
        indexes = [index for index, score in enumerate(scores) if score == scores[-1]]
        distances = [b - a for a, b in zip(indexes, indexes[1:])]
        if len(set(distances)) == 1:
            return distances[0]
    return -1


def solution_2():
    scores = []
    n = 0
    while n < 10 ** 9:
        rotate()
        tilt()
        rotate()
        tilt()
        rotate()
        tilt()
        rotate()
        tilt()
        scores.append(sum(table[r].count("O") * (SIZE - r) for r in range(SIZE)))
        loop = detect_loop(scores, 5)
        if loop != -1:
            start = n
            n += int((10 ** 9 - n) / loop) * loop
            return scores[start - loop + 10 ** 9 - n - 1]
        n += 1
    return scores[-1]


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
