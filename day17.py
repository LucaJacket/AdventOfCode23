from heapq import heappush, heappop

map = {complex(i, j): int(c) for i, r in enumerate(open("input.txt").read().splitlines()) for j, c in enumerate(r)}


def f(min_steps, max_steps):
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    seen = set()
    end = [*map][-1]
    x = 0
    while todo:
        val, _, pos, dir = heappop(todo)
        if pos == end:
            return val
        if (pos, dir) not in seen:
            seen.add((pos, dir))
            for new_dir in dir * 1j, dir * (-1j):
                for steps in range(min_steps, max_steps + 1):
                    if pos + new_dir * steps in map:
                        new_val = val + sum(map[pos + new_dir * i] for i in range(1, steps + 1))
                        heappush(todo, (new_val, (x := x + 1), pos + new_dir * steps, new_dir))


for min_steps, max_steps in (1, 3), (4, 10):
    print(f(min_steps, max_steps))
