tiles = {complex(i, j): c for i, r in enumerate(open("input.txt").read().splitlines()) for j, c in enumerate(r)}


def next(pos: complex, dir: complex):
    pos += dir
    if pos not in tiles:
        return tuple()
    match tiles[pos]:
        case "|":
            return (pos, 1), (pos, -1)
        case "-":
            return (pos, 1j), (pos, -1j)
        case "\\":
            return (pos, dir.conjugate() * 1j),
        case "/":
            return (pos, dir.conjugate() * -1j),
        case _:
            return (pos, dir),


def f(start: tuple[complex, complex]):
    seen = set()
    todo = [start,]
    while todo:
        pos, dir = todo.pop()
        seen.add((pos, dir))
        todo.extend(set(next(pos, dir)) - seen)
    return len(set(map(lambda t: t[0], seen))) - 1


print(f((-1j, 1j)))
print(max(map(f, [(pos - dir, dir) for dir in (1j, -1j, 1, -1) for pos in tiles if pos - dir not in tiles])))
