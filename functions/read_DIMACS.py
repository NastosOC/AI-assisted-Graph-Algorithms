import networkx as nx
import requests
from io import StringIO
import os
import random

def read_dimacs_clq(source):
    """
    Reads a DIMACS .clq graph file and creates a networkx.Graph object.
    Parameters:
        source (str): Path to the .clq file or URL.
    Returns:
        G (networkx.Graph): The resulting graph.
    """
    G = nx.Graph()

    # Determine if source is a URL
    lines = open(source, 'r')

    with lines as f: # Allows python to handle closing
        for line in f:
            if not line or line.startswith('c'):
                continue # Skips comments
            if line.startswith('p'):
                parts = line.strip().split()
                num_vertices = int(parts[2])
                G.add_nodes_from(range(1, num_vertices + 1))
            elif line.startswith('e'):
                parts = line.strip().split()
                u = int(parts[1])
                v = int(parts[2])
                G.add_edge(u, v)
    return G