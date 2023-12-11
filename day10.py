import re


table = [list(line) for line in open("input.txt").read().split("\n")]
SIZE = len(table)
path = []


def init_start():
    for i in range(SIZE):
        for j in range(SIZE):
            if table[i][j] == "S":
                if table[i - 1][j] in "|7F":
                    if table[i + 1][j] in "|JL":
                        table[i][j] = "|"
                    elif table[i][j - 1] in "-LF":
                        table[i][j] = "J"
                    elif table[i][j + 1] in "-J7":
                        table[i][j] = "L"
                elif table[i + 1][j] in "|JL":
                    if table[i][j - 1] in "-LF":
                        table[i][j] = "7"
                    elif table[i][j + 1] in "-J7":
                        table[i][j] = "F"
                else:
                    table[i][j] = "-"
                return i, j


def init_path():
    start = init_start()
    path.append(start)
    last = start
    while True:
        r, c = path[-1]
        # north
        if r > 0 and table[r][c] in "|JL" and table[r - 1][c] in "|7F" and (r - 1, c) not in (start, last):
            path.append((r - 1, c))
        # east
        elif c < SIZE - 1 and table[r][c] in "-LF" and table[r][c + 1] in "-J7" and (r, c + 1) not in (start, last):
            path.append((r, c + 1))
        # south
        elif r < SIZE - 1 and table[r][c] in "|7F" and table[r + 1][c] in "|JL" and (r + 1, c) not in (start, last):
            path.append((r + 1, c))
        # west
        elif c > 0 and table[r][c] in "-J7" and table[r][c - 1] in "-LF" and (r, c - 1) not in (start, last):
            path.append((r, c - 1))
        else:
            break
        last = path[-2]
    return path


def solution_1():
    return int(len(path) / 2 + 0.5)


def is_inside(r, c):
    path_to_east = "".join(table[r][(c + 1):])
    path_to_east = re.sub("F-*J", "|", path_to_east)
    path_to_east = re.sub("L-*7", "|", path_to_east)
    return path_to_east.count("|") % 2


def solution_2():
    not_path = {(i, j) for i in range(SIZE) for j in range(SIZE)}.difference(set(path))
    for r, c in not_path:
        table[r][c] = "."
    return sum(is_inside(r, c) for r, c in not_path)


if __name__ == "__main__":
    init_path()
    print(solution_1())
    print(solution_2())
