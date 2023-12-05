seeds_1 = seeds_2 = maps = []


def init_seeds_maps(input):
    global seeds_1
    global seeds_2
    global maps
    raw_seeds, *raw_maps = input.split("\n\n")
    seeds_1 = [int(x) for x in raw_seeds.split(":")[1].split()]
    seeds_2 = [(first, first + quantity - 2) for first, quantity in zip(seeds_1[0::2], seeds_1[1::2])]
    maps = [[[int(x) for x in line.split()] for line in raw_map.split("\n")[1:]] for raw_map in raw_maps]


def convert_single(x, map):
    for dst, src, rng in map:
        if x in range(src, src + rng):
            return x + dst - src
    return x


def solution_1():
    result = set(seeds_1)
    for map in maps:
        result = set(convert_single(x, map) for x in result)
    return min(result)


def convert_range(first, last, map):
    for dst, src, rng in map:
        if first in range(src, src + rng) and last in range(src, src + rng):
            return {(first + dst - src, last + dst - src)}
        elif first < src + rng <= last:
            return set.union(convert_range(first, src + rng - 1, map), convert_range(src + rng, last, map))
        elif first < src <= last:
            return set.union(convert_range(first, src - 1, map), convert_range(src, last, map))
    return {(first, last)}


def solution_2():
    result = set(seeds_2)
    for map in maps:
        result = set.union(*(convert_range(first, last, map) for first, last in result))
    return min(set(first for first, last in result))


if __name__ == "__main__":
    input = open("input.txt").read()
    init_seeds_maps(input)
    print(solution_1())
    print(solution_2())

