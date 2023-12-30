G = {complex(i, j): c for i, r in enumerate(open("input.txt").readlines()) for j, c in enumerate(r) if c in '.S'}


def cmod(x: complex, m: int):
    return complex(x.real % m, x.imag % 131)


def f(n: int, a: int, b: int, c: int):
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)


done = []
todo = {x for x in G if G[x] == 'S'}
for s in range(3 * 131):
    if s == 64:
        print(len(todo))
    if s % 131 == 65:
        done.append(len(todo))
    todo = {pos + dir for dir in {1, -1, 1j, -1j} for pos in todo if cmod(pos + dir, 131) in G}
print(f(26501365 // 131, *done))
