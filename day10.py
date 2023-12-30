import re

dirs = {
    "|": (-1, 1),
    "-": (1j, -1j),
    "L": (-1, 1j),
    "J": (-1, -1j),
    "7": (1, -1j),
    "F": (1, 1j),
    ".": ()
}

maze = {complex(i, j): c for i, l in enumerate(open("input.txt").read().splitlines()) for j, c in enumerate(l)}
start = [k for k, v in maze.items() if v == "S"][0]
maze[start] = [sub for sub in "LJ7F-|" if all(-dir in dirs[maze[start + dir]] for dir in dirs[sub])][0]

path = set()
todo = [start]
while todo:
    pos = todo.pop()
    if pos not in path:
        path.add(pos)
        for dir in dirs[maze[pos]]:
            todo.append(pos + dir)


def inside(pos: complex):
    l = "".join(maze[complex(pos.real, j)] for j in range(0, int(pos.imag)) if complex(pos.real, j) in path)
    return bool(len(re.findall(r"(\|)|(F-*J)|(L-*7)", l)) % 2)


print(len(path) // 2)
print(sum(map(inside, set(maze.keys()) - path)))
