from heapq import heappush, heappop

map = {complex(i, j): int(c) for i, r in enumerate(open("input.txt")) for j, c in enumerate(r.strip())}


def heat_loss(min_steps, max_steps):
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    seen = set()
    end = [*map][-1]
    x = 0
    while todo:
        loss, _, pos, dir = heappop(todo)
        if pos == end:
            return loss
        if (pos, dir) not in seen:
            seen.add((pos, dir))
            for new_dir in dir * 1j, dir * (-1j):
                for steps in range(min_steps, max_steps + 1):
                    if pos + new_dir * steps in map:
                        new_loss = loss + sum(map[pos + new_dir * i] for i in range(1, steps + 1))
                        x = x + 1
                        heappush(todo, (new_loss, x, pos + new_dir * steps, new_dir))


def solution_1():
    return heat_loss(1, 3)


def solution_2():
    return heat_loss(4, 10)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
