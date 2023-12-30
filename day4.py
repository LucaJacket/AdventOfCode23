data = open("input.txt").readlines()
p1 = [0.5] * len(data)
p2 = [1] * len(data)

for i, l in enumerate(data):
    w, h = map(str.split, l.split("|"))
    for j in range(len(set(w) & set(h))):
        p1[i] *= 2
        p2[i + j + 1] += p2[i]

print(sum(map(int, p1)))
print(sum(p2))
