from functools import cache


tiles = {complex(i, j): c for i, r in enumerate(open("input.txt").read().split("\n")) for j, c in enumerate(r)}


@cache
def next_tile(pos: complex, dir: complex):
    pos += dir
    if pos in tiles:
        next_tile = tiles.get(pos)
        if next_tile == "|" and dir.imag:
            dirs = 1, -1
        elif next_tile == "-" and dir.real:
            dirs = 1j, -1j
        elif next_tile == "\\":
            dirs = dir.conjugate() * 1j,
        elif next_tile == "/":
            dirs = dir.conjugate() * -1j,
        else:
            dirs = dir,
    else:
        dirs = ()
    return tuple((pos, dir) for dir in dirs)


def energized(pos: complex, dir: complex):
    energized = set()
    next_tiles = list(next_tile(pos, dir))
    while next_tiles:
        tile = next_tiles.pop(0)
        if tile not in energized:
            energized.add(tile)
            next_tiles.extend(next_tile(*tile))
    return len(set(pos for pos, dir in energized))


def solution_1():
    return energized(-1j, 1j)


def solution_2():
    start_points = [(pos - dir, dir) for dir in (1j, -1j, 1, -1) for pos in tiles if pos - dir not in tiles]
    return max(energized(*tile) for tile in start_points)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
