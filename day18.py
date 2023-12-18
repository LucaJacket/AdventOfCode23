def shoelace(polygon: list[complex]):
    pairs = [(polygon[i - 1], polygon[i]) for i in range(len(polygon))]  # (x1,x2), (x2,x3), ..., (xn-1,xn), (xn,x1)
    area = 0.5 * abs(sum(x.real * y.imag - y.real * x.imag for x, y in pairs))
    perimeter = sum(abs(x - y) for x, y in pairs)
    return area + perimeter / 2 + 1


def solution_1():
    trench = [complex(0)]
    char2dir = {
        "R": 1j,
        "D": 1,
        "L": -1j,
        "U": -1,
    }
    for line in open("input.txt").read().splitlines():
        dir, steps, _ = line.split()
        trench.append(trench[-1] + char2dir[dir] * int(steps))
    return shoelace(trench)


def solution_2():
    trench = [complex(0)]
    char2dir = {
        "0": 1j,
        "1": 1,
        "2": -1j,
        "3": -1,
    }
    for line in open("input.txt").read().splitlines():
        data = line.split()[2][2:-1]
        trench.append(trench[-1] + char2dir[data[-1]] * int(data[:-1], 16))
    return shoelace(trench)


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
