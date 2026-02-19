import networkx as nx
from networkx import *
import matplotlib.pyplot as plt
import itertools
from itertools import *
import math

def is_clique(G, v):
    """
    Check if the nodes in list v form a clique in graph G.
    Parameters:
        G (networkx.Graph): The graph.
        v (list): List of nodes to check.   
    Returns:
        bool: True if v forms a clique, False otherwise.
    """
    # Validate input: must be list/tuple/set
    if not isinstance(v, (list, tuple, set)):
        return False
    # Reject duplicate nodes
    try:
        if len(v) != len(set(v)):
            return False
    except TypeError:
        return False
    # Validate each node: must be in G and hashable
    try:
        for node in v:
            if node not in G:
                return False
    except TypeError:
        return False
    # Check if is_clique
    subgraph = G.subgraph(v)
    n = len(v)
    expected_edges = n * (n - 1) // 2

    if subgraph.number_of_edges() == expected_edges:
        return True
    else:
        return False
    
def is_prime(G):
    """
    Created with the help of AI.
    Determines whether a graph is prime with respect to modular decomposition.
    A graph is considered prime if it contains no non-trivial modules.
    That is, every proper subset of nodes (with size ≥ 2 and < n)
    Parameters:
        G (networkx.Graph): The graph.
    Returns: 
        bool: True if the graph is prime, False otherwise.
    """
    # Validate G is a NetworkX graph
    if not isinstance(G, nx.Graph):
        return False

    nodes = list(G.nodes())
    n = len(nodes)

    if len(nodes) < 2:
        return False
    
    if not nx.is_connected(G):
        return False

    for subset_size in range(2, n):
        for subset in combinations(nodes, subset_size):
            subset_set = set(subset)
            if is_module(G, subset_set):
                return False # Found non-trivial module
    
    return True

def is_module(G, subset):
    """
    Created with the help of AI.
    Checks if a given subset of nodes forms a module in the graph G.
    Parameters:
        G (networkx.Graph): The graph.
        subset (set): A set of nodes to check.
    Returns:
        bool: True if the subset is a module, False otherwise.
    """
    # Validate G
    if not isinstance(G, nx.Graph):
        return False

    # Validate subset
    if not isinstance(subset, (set, list, tuple)):
        return False

    try:
        subset = set(subset)  # Make sure it's a set
        if not subset.issubset(G.nodes):
            return False
    except TypeError:
        return False  # e.g., unhashable elements in subset
    
    outside_subset = set(G.nodes()) - subset
    for vertex in outside_subset:
        neighbors_in_subset = subset & set(G.neighbors(vertex))
        if 0 < len(neighbors_in_subset) < len(subset):
            return False # vertex treats some nodes differntly
    
    return True # All outside nodes treat the subset uniformly

def is_split(G):
    """
    Checks if a given graph is split by checking if both the 
    graph and its complement are chordal.
    Parameters:
        G (networkx.Graph): The graph.
    Returns:
        Bool: True if both the graph and its compliment are 
        chordal, False otherwise.
    """
    if not isinstance(G, nx.Graph):
        return False
    
    G_Comp = nx.complement(G)

    if is_chordal(G) and is_chordal(G_Comp):
        return True
    return False

def is_p4(G, v):
    """
    Check if the nodes in list v form a P4 in graph G.
    Parameters:
        G (networkx.Graph): The graph.
        v (list): List of nodes to check.   
    Returns:
        bool: True if v forms a P4, False otherwise.
    """
    if not isinstance(G, nx.Graph):
        return False

    if not isinstance(v, (list, tuple, set)):
        return False

    if len(v) != 4:
        return False

    subgraph = G.subgraph(v)
    degrees = sorted([d for _, d in subgraph.degree()])
    
    if len(subgraph.edges) != 3:
        return False

    if (degrees == [1, 1, 2, 2]):
        return True
    
    return False

def is_c4(G, v):
    """
    Check if the nodes in list v form a C4 in graph G.
    Parameters:
        G (networkx.Graph): The graph.
        v (list): List of nodes to check.   
    Returns:
        bool: True if v forms a C4, False otherwise.
    """
    if not isinstance(G, nx.Graph):
        return False
    if not isinstance(v, (list, tuple, set)):
        return False

    if len(v) != 4:
        return False

    try:
        if len(set(v)) != 4:
            return False
    except TypeError:
        # Unhashable nodes in v
        return False

    try:
        for node in v:
            hash(node)
            if node not in G:
                return False
    except TypeError:
        return False

    subgraph = G.subgraph(v)

    for node in subgraph.nodes():
        if subgraph.degree(node) != 2:
            return False

    return True


def is_quasi_threshold(G, certifying=None):
    from functions.find_functions import find_all_c4, find_all_p4_bfs
    """
    Determines whether G is a quasi-threshold graph by checking for induced P4s and C4s.
    Parameters:
        G (networkx.Graph): The input graph.
    Returns:
        bool: True if G is quasi-threshold, False otherwise.
    """
    if not isinstance(G, nx.Graph):
        return False
    
    p4_list = find_all_p4_bfs(G)
    c4_list = find_all_c4(G)
    
    if not p4_list and not c4_list:
        return True
    
    if certifying:
        print(f"P4 List: {p4_list} \nC4 List: {c4_list}")

    return False

def is_quasi_threshold_2(G):
    """
    Determines whether G is a quasi-threshold graph by checking for induced P4s and C4s.
    Parameters:
        G (networkx.Graph): The input graph.
    Returns:
        bool: True if G is quasi-threshold, False otherwise.
    """
    if not isinstance(G, nx.Graph):
        return False
    
    for e in G.edges():
        x, y = e

        left_set = set(G.neighbors(x)) - set(G.neighbors(y)) - {y}
        right_set = set(G.neighbors(y)) - set(G.neighbors(x)) - {x}
    
        if len(left_set) > 0 and len(right_set) > 0:
            return False
        
    return True
