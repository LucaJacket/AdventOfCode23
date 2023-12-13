tables = [table.split("\n") for table in open("input.txt").read().split("\n\n")]


def find_mirror(table, errors):
    for r in range(1, len(table)):
        up = "".join(table[:r][::-1])
        down = "".join(table[r:])
        if sum(x != y for x, y in zip(up, down)) == errors:
            return r
    return 0


def solution_1():
    return sum(100 * find_mirror(table, 0) + find_mirror(["".join(row) for row in list(zip(*table))], 0)
               for table in tables)


def solution_2():
    return sum(100 * find_mirror(table, 1) + find_mirror(["".join(row) for row in list(zip(*table))], 1)
               for table in tables)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
