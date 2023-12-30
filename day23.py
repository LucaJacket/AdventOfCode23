from collections import deque, defaultdict

char2dirs = {".": (-1, 1j, 1, -1j), "<": (-1j,), ">": (1j,), "v": (1,), "^": (-1,)}
G = {complex(i, j): c for i, r in enumerate(open("input.txt").readlines()) for j, c in enumerate(r) if c in ".<>v^"}


def dirs(pos: complex, from_dir: complex, slopes=True):
    return set(dir for dir in (char2dirs[G[pos]] if slopes else (-1, 1, -1j, 1j)) if pos + dir in G) - {-from_dir}


def collapse(slopes=True):
    graph = defaultdict(lambda: {})
    todo = deque([(1j, 1)])
    while todo:
        head, dir = todo.popleft()
        tail = head + dir
        steps = 1
        while len(n_dirs := dirs(tail, dir, slopes)) == 1:
            steps += 1
            dir = n_dirs.pop()
            tail += dir
        if tail not in graph[head]:
            graph[head][tail] = steps
            for n_dir in n_dirs:
                todo.append((tail, n_dir))
    return graph


def dfs(graph, start, seen=None, steps=0):
    if seen is None:
        seen = set()
    if start not in graph:
        return steps
    max_steps = []
    for end in graph[start]:
        if end not in seen:
            max_steps.append(dfs(graph, end, seen | {end}, steps + graph[start][end]))
    return max(max_steps, default=0)


for slopes in True, False:
    print(dfs(collapse(slopes), 1j))
