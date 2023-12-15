steps = open("input.txt").read().split(",")


def convert(str):
    i = 0
    for c in str:
        i += ord(c)
        i *= 17
        i %= 256
    return i


def solution_1():
    return sum(convert(step) for step in steps)


boxes = [[] for _ in range(256)]


def init_boxes():
    for step in steps:
        if "=" in step:
            label, power = step.split("=")
            box = convert(label)
            try:
                i = [lens[0] for lens in boxes[box]].index(label)
                boxes[box][i] = (label, int(power))
            except ValueError:
                boxes[box].append((label, int(power)))
        elif "-" in step:
            label = step.split("-")[0]
            box = convert(label)
            try:
                i = [lens[0] for lens in boxes[box]].index(label)
                boxes[box].pop(i)
            except ValueError:
                continue
        else:
            raise ValueError("No '=' or '-' in step")


def solution_2():
    init_boxes()
    return sum(sum((1 + box) * (1 + slot) * boxes[box][slot][1] for slot in range(len(boxes[box])))
               for box in range(256))


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
