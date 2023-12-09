histories = [[int(x) for x in line.split()] for line in open("input.txt").readlines()]


def find_next_element(sequence):
    differences = [y - x for x, y in zip(sequence, sequence[1:])]
    return sequence[-1] + find_next_element(differences) if differences else 0


def solution_1():
    return sum(find_next_element(history) for history in histories)


def solution_2():
    return sum(find_next_element(history[::-1]) for history in histories)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
