# Connected graphs on 6 vertices with 2 ≤ degree ≤ 4

graphs = list(graphs.nauty_geng("6 -c -d2 -D4"))

print("Number of graphs:", len(graphs))

for G in graphs:
    G.plot().show()