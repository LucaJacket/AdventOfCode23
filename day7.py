def f(line: str):
    hand, bid = line.split()
    return max(type(opt) for opt in set(hand.replace("0", c) for c in hand)), hand, int(bid)


def type(hand: str):
    return sum(map(hand.count, hand))


data = open("input.txt").read()
for mask in "ABCDE", "A0CDE":
    print(sum(rank * bid for rank, (_, _, bid) in enumerate(
        sorted(map(f, data.translate(str.maketrans("TJQKA", mask)).splitlines())), 1)))
