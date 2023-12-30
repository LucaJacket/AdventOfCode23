import re

games = {}

for i, l in enumerate(open("input.txt").readlines(), 1):
    bag = {"r": 0, "g": 0, "b": 0}
    for quantity, color in re.findall(r"(\d+) (\w)", l):
        bag[color] = max(bag[color], int(quantity))
    games[i] = bag

print(sum(i for i, bag in games.items() if bag["r"] <= 12 and bag["g"] <= 13 and bag["b"] <= 14))
print(sum(bag["r"] * bag["g"] * bag["b"] for bag in games.values()))
