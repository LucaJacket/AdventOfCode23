def tilt(table: list[str]):  # tilt east
    return list("#".join(map("".join, map(sorted, r.split("#")))) for r in table)


def rotate(table: list[str]):  # rotate 90 degrees clockwise
    return list(map("".join, zip(*table[::-1])))


def load(table: list[str]):
    return sum(r.count("O") * (100 - i) for i, r in enumerate(table))


table = open("input.txt").read().splitlines()
print(load(rotate(rotate(rotate(tilt(rotate(table)))))))

mem = []
for _ in range(1_000_000_000):
    quad = tuple(load(table := tilt(rotate(table))) for _ in range(4))
    try:
        i = mem.index(quad)
        print(mem[i + (999_999_999 - i) % (len(mem) - i)][-1])
        break
    except ValueError:
        mem.append(quad)
