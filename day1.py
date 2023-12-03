import re


def solution_1(input):
    return sum(int(line[0] + line[-1]) for line in re.sub(r"[A-Za-z]", "", input).split("\n"))


def solution_2(input):
    str2num = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    for k, v in str2num.items():
        input = input.replace(k, v)
    return solution_1(input)


if __name__ == '__main__':
    input = open("input.txt").read()
    print(solution_1(input))
    print(solution_2(input))
