with open("non_perfectly_orderable_g6.txt", "r") as f:
    for i, line in enumerate(f):
        g6 = line.strip()
        G = Graph(g6)

        print(f"Graph {i}: {G.degree_sequence()}")
        print(g6)
