char2dir = {"R": 1j, "D": 1, "L": -1j, "U": -1,
            "0": 1j, "1": 1, "2": -1j, "3": -1}


def shoelace(polygon: list[complex]):
    pairs = [(polygon[i - 1], polygon[i]) for i in range(len(polygon))]  # (x1,x2), (x2,x3), ..., (xn-1,xn), (xn,x1)
    area = 0.5 * abs(sum(x.real * y.imag - y.real * x.imag for x, y in pairs))
    perimeter = sum(abs(x - y) for x, y in pairs)
    return area + perimeter / 2 + 1


t1 = [complex(0)]
t2 = [complex(0)]
for line in open("input.txt").readlines():
    dir, steps, data = line.split()
    t1.append(t1[-1] + char2dir[dir] * int(steps))
    t2.append(t2[-1] + char2dir[data[-2]] * int(data[2:-2], 16))
print(shoelace(t1))
print(shoelace(t2))
