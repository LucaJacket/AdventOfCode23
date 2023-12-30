seeds, *mappings = open("input.txt").read().split("\n\n")
seeds = [int(x) for x in seeds.split(":")[1].split()]
mappings = [[[int(x) for x in l.split()] for l in mapping.splitlines()[1:]] for mapping in mappings]


def convert(fst: int, lst: int, mapping: list[list[int]]):
    for dst, src, rng in mapping:
        if src <= fst < src + rng and src <= lst < src + rng:
            return {(fst + dst - src, lst + dst - src)}
        elif fst < src + rng <= lst:
            return convert(fst, src + rng - 1, mapping) | convert(src + rng, lst, mapping)
        elif fst < src <= lst:
            return convert(fst, src - 1, mapping) | convert(src, lst, mapping)
    return {(fst, lst)}


for x in set(zip(seeds, seeds)), set(zip(seeds[::2], seeds[1::2])):
    for mapping in mappings:
        x = set.union(*(convert(first, last, mapping) for first, last in x))
    print(min(first for first, _ in x))
