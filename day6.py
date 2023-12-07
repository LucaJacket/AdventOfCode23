import math


def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        return (- b - math.sqrt(discriminant)) / (2 * a), (- b + math.sqrt(discriminant)) / (2 * a)
    else:
        return 0.0, 0.0


def calculate_ways(time, distance):
    first, last = solve_quadratic_equation(1, -time, distance)
    return math.floor(last - 0.0001) - math.ceil(first + 0.0001) + 1


def solution_1(input):
    times, distances = [[int(x) for x in line.split(":")[1].split()] for line in input]
    return math.prod(calculate_ways(time, distance) for time, distance in zip(times, distances))


def solution_2(input):
    time, distance = [int("".join(line.split(":")[1].split())) for line in input]
    return calculate_ways(time, distance)


if __name__ == "__main__":
    input = open("input.txt").readlines()
    print(solution_1(input))
    print(solution_2(input))

