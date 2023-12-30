data = open("input.txt").read().split(",")


def hash(s: str):
    i = 0
    for c in s:
        i = (i + ord(c)) * 17 % 256
    return i


print(sum(map(hash, data)))

boxes = [{} for _ in range(256)]
for step in data:
    match step.strip("-").split("="):
        case [l, p]:
            boxes[hash(l)][l] = int(p)
        case [l]:
            boxes[hash(l)].pop(l, 0)

print(sum(i * j * p for i, box in enumerate(boxes, 1) for j, p in enumerate(box.values(), 1)))
