import math

workflows, parts = open("input.txt").read().split("\n\n")
workflows = {n: r.split(",") for n, r in [w[:-1].split("{") for w in workflows.splitlines()]}
parts = [{k: int(v) for k, v in [eq.split("=") for eq in p[1:-1].split(",")]} for p in parts.splitlines()]


def f(rng: dict, name="in", i=0):
    match name:
        case "A":
            return math.prod(b - a + 1 for a, b in rng.values())
        case "R":
            return 0
        case _:
            match workflows[name][i].split(":"):
                case [expr, dest]:
                    val1, gt, val2 = expr[0], expr[1] == ">", int(expr[2:])
                    acc_rng = (val2 + 1, 4000) if gt else (1, val2 - 1)
                    if rng[val1][0] <= rng[val1][1] < acc_rng[0] or acc_rng[1] < rng[val1][0] <= rng[val1][1]:
                        return f(rng, name, i + 1)
                    elif acc_rng[0] <= rng[val1][0] <= rng[val1][1] <= acc_rng[1]:
                        return f(rng, dest)
                    elif rng[val1][0] < acc_rng[0] <= rng[val1][1]:
                        sup = rng.copy()
                        sup[val1] = (acc_rng[0], sup[val1][1])
                        rng[val1] = (rng[val1][0], acc_rng[0] - 1)
                        return f(sup, dest) + f(rng, name, i + 1)
                    elif rng[val1][0] <= acc_rng[1] < rng[val1][1]:
                        inf = rng.copy()
                        inf[val1] = (inf[val1][0], acc_rng[1])
                        rng[val1] = (acc_rng[1] + 1, rng[val1][1])
                        return f(inf, dest) + f(rng, name, i + 1)
                case [dest]:
                    return f(rng, dest)


print(sum(sum(p.values()) for p in parts if f({k: (p[k], p[k]) for k in "xmas"})))
print(f({k: (1, 4000) for k in "xmas"}))
