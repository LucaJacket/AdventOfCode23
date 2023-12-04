def solution_1(input):
    sum = 0
    for line in input:
        winning, nums = map(str.split, line.split(":")[1].split("|"))
        sum += int(2 ** (len(set(winning) & set(nums)) - 1))
    return sum


def solution_2(input):
    scratchcards = {i: 0 for i in range(200)}
    for current, line in enumerate(input):
        winning, nums = map(str.split, line.split(":")[1].split("|"))
        points = len(set(winning) & set(nums))
        scratchcards[current] += 1
        for next in range(current + 1, current + 1 + points):
            scratchcards[next] += scratchcards[current]
    return sum(scratchcards.values())


if __name__ == "__main__":
    input = open("input.txt").readlines()
    print(solution_1(input))
    print(solution_2(input))
