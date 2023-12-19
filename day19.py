import math

raw_workflows, raw_parts = open("test.txt").read().split("\n\n")
workflows = {n: r.split(",") for n, r in [workflow[:-1].split("{") for workflow in raw_workflows.splitlines()]}
parts = [{k: int(v) for k, v in [eq.split("=") for eq in part[1:-1].split(",")]} for part in raw_parts.splitlines()]


def is_accepted(part: dict):
    cur = "in"
    while cur not in "AR":
        for r in workflows[cur]:
            if ":" not in r:
                cur = r  # r is the 'else' destination
            else:
                expr, dest = r.split(":")
                val1 = part[expr[0]]
                op = expr[1]
                val2 = int(expr[2:])
                if (op == ">" and val1 > val2) or (op == "<" and val1 < val2):
                    cur = dest
                    break
    return cur == "A"


def solution_1():
    return sum(sum(part.values()) for part in parts if is_accepted(part))


def accepted(name: str, ranges: dict, i: int = 0):
    if name == "A":
        return math.prod(b - a + 1 for a, b in ranges.values())
    elif name == "R":
        return 0
    else:
        r = workflows[name][i]
        if ":" not in r:
            return accepted(r, ranges)  # r is the 'else' destination
        else:
            expr, dest = r.split(":")
            n_ranges = ranges.copy()
            op = expr[1]
            val = int(expr[2:])
            n_ranges[expr[0]] = (n_ranges[expr[0]][0], val - 1) if op == "<" else (val + 1, n_ranges[expr[0]][1])
            ranges[expr[0]] = (ranges[expr[0]][0], val) if op == ">" else (val, ranges[expr[0]][1])
            return accepted(dest, n_ranges) + accepted(name, ranges, i + 1)


def solution_2():
    return accepted("in", {k: (1, 4000) for k in "xmas"})


if __name__ == "__main__":
    print(solution_1())
    print(solution_2())
