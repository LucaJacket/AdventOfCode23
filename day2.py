import re


games = {}


def initialize_games(input):
    global games
    for line in input.split("\n"):
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        items = re.sub("[:,;]", "", line).split()
        for quantity, color in zip(items[2::2], items[3::2]):
            cubes[color] = max(cubes[color], int(quantity))
        games[int(items[1])] = cubes


def solution_1():
    return sum(id for id, cubes in games.items() if
               cubes["red"] <= 12 and cubes["green"] <= 13 and cubes["blue"] <= 14)


def solution_2():
    return sum(cubes["red"] * cubes["green"] * cubes["blue"] for cubes in games.values())


if __name__ == '__main__':
    input = open("input.txt").read()
    initialize_games(input)
    print(solution_1())
    print(solution_2())
