import re


def f(line: str):
    x = re.findall(r"(\d)", line)
    return int(x[0] + x[-1])


def t(line: str):
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
        line = line.replace(k, v)
    return line


data = open("input.txt").readlines()
print(sum(map(f, data)))
print(sum(map(f, map(t, data))))
