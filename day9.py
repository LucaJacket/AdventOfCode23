data = [list(map(int, l.split())) for l in open("input.txt").readlines()]


def f(seq: list[int]):
    diffs = [y - x for x, y in zip(seq, seq[1:])]
    return seq[-1] + f(diffs) if diffs else 0


print(sum(f(seq) for seq in data))
print(sum(f(seq[::-1]) for seq in data))
