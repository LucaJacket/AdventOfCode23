import math
from collections import deque

modules = {k: v.split(", ") for k, v in (l.split(" -> ") for l in open("input.txt").read().splitlines())}
ff = {}
conj = {}

for k in modules:
    if k.startswith("%"):
        ff[k.strip("%")] = False
    elif k.startswith("&"):
        conj[k.strip("&")] = {m[1:]: False for m in modules if k[1:] in modules[m]}


def handle_pulse(sender, receiver, pulse):
    if receiver in ff:
        if pulse:
            return []
        ff[receiver] = not ff[receiver]
        pulse = ff[receiver]
        return [(receiver, module, pulse) for module in modules["%" + receiver]]
    elif receiver in conj:
        conj[receiver][sender] = pulse
        pulse = not all(conj[receiver][sender] for sender in conj[receiver])
        return [(receiver, module, pulse) for module in modules["&" + receiver]]
    elif receiver in modules:
        return [(receiver, module, pulse) for module in modules[receiver]]
    return []


pulses = {True: 0, False: 0}
min_pushes = {module: -1 for module in conj["th"]}
n = 0
while n < 1000 or -1 in min_pushes.values():
    if n == 1000:
        print(pulses[True] * pulses[False])
    n += 1
    todo = deque([("button", "broadcaster", False)])
    while todo:
        sender, receiver, pulse = todo.popleft()
        pulses[pulse] += 1
        if pulse and sender in min_pushes and min_pushes[sender] == -1:
            min_pushes[sender] = n
        todo.extend(handle_pulse(sender, receiver, pulse))
print(math.lcm(*min_pushes.values()))
