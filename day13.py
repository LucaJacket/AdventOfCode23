tables = list(map(str.split, open("input.txt").read().split("\n\n")))


def f(table: list[str]):
    for r in range(1, len(table)):
        up = "".join(table[:r][::-1])
        down = "".join(table[r:])
        if sum(x != y for x, y in zip(up, down)) == err:
            return r
    return 0


for err in 0, 1:
    print(sum(100 * f(table) + f(list(map("".join, zip(*table)))) for table in tables))
