import networkx as nx
import requests
from io import StringIO
import os
import random

def generate_trivially_perfect_graph(n, seed=None):
    """
    AI generated method, based on wikipedia article: https://en.wikipedia.org/wiki/Trivially_perfect_graph
    Generate a random trivially perfect graph with up to n nodes.
    Nodes are labeled with integers from 0 to n-1.
    
    Parameters:
        n (int): Approximate number of nodes in the graph.
        seed (int or None): Optional random seed for reproducibility.

    Returns:
        G (networkx.Graph): A trivially perfect graph.
    """
    if seed is not None:
        random.seed(seed)

    node_counter = [0]  # Mutable counter to assign unique node labels

    def build_subgraph(size):
        if size == 1:
            G = nx.Graph()
            G.add_node(node_counter[0])
            node_counter[0] += 1
            return G
        
        op = random.choice(["union", "join"])
        if op == "union":
            # Randomly split the size between two components
            left_size = random.randint(1, size - 1)
            right_size = size - left_size
            G1 = build_subgraph(left_size)
            G2 = build_subgraph(right_size)
            return nx.disjoint_union(G1, G2)
        
        elif op == "join":
            # Create a new root node and attach it to a smaller trivially perfect graph
            G_sub = build_subgraph(size - 1)
            G = G_sub.copy()
            new_node = node_counter[0]
            G.add_node(new_node)
            node_counter[0] += 1
            for v in G_sub.nodes:
                G.add_edge(new_node, v)
            return G

    return build_subgraph(n)