import networkx as nx

G = nx.Graph()

for l in open("input.txt").read().splitlines():
    start, *ends = l.replace(":", "").split()
    for end in ends:
        G.add_edge(start, end)

cc = nx.spectral_bisection(G)
print(len(cc[0]) * len(cc[1]))
