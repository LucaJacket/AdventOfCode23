import math


def ways(time: int, distance: int):  # a = 1, b = -time, c = distance
    if (d := time ** 2 - 4 * distance) < 0:
        return 0
    return math.floor((time + math.sqrt(d)) / 2) - math.floor((time - math.sqrt(d)) / 2)


times, distances = [l.split(":")[1].split() for l in open("input.txt").readlines()]
print(math.prod(ways(time, distance) for time, distance in zip(map(int, times), map(int, distances))))
print(ways(int("".join(times)), int("".join(distances))))
