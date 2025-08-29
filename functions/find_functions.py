import networkx as nx
from networkx import *
import matplotlib.pyplot as plt
import itertools 
from itertools import *
import math
import inspect

from functions.check_functions import *

def find_all_p4(G):
    """
    Checks every combination of 4 nodes in a graph for if they are P4s. If the combo is a P4 it's 
    added to the list, else ignored.
    Parameters:
        G (networkx.Graph): The graph.  
    Returns:
        p4_list (list): A list of all P4s found in the graph.
    """
    p4_list = []

    combos = list(itertools.combinations(G.nodes(), r=4))

    for c in combos:
        if is_p4(G, c):
            p4_list.append(frozenset(c))
    
    return p4_list

def find_all_p4_bfs(G):
    """
    Parameters:
        G (networkx.Graph): The graph.  
    Returns:
        p4_list (list): A list of all P4s found in the graph.
    """
    p4_list = []
    for e in G.edges():
        x, y = e

        left_set = set(G.neighbors(x)) - set(G.neighbors(y)) - {y}
        right_set = set(G.neighbors(y)) - set(G.neighbors(x)) - {x}

        for v in left_set:
            for w in right_set:
                if not G.has_edge(v, w):
                    p4 = frozenset([v, x, y, w])
                    p4_list.append(p4)

    return p4_list

def find_all_c4(G):
    """
    Checks every combination of 4 nodes in a graph for if they are C4s. If the combo is a C4 it's 
    added to the list, else ignored.
    Parameters:
        G (networkx.Graph): The graph.  
    Returns:
        c4_list (list): A list of all C4s found in the graph.
    """
    c4_list = []

    combos = list(itertools.combinations(G.nodes(), r=4))

    for c in combos:
        if is_c4(G, c):
            c4_list.append(frozenset(c))
    
    return c4_list

def find_all_c4_bfs_broken(G_original):
    """
    Parameters:
        G (networkx.Graph): The graph.  
    Returns:
        c4_list (list): A list of all C4s found in the graph.
    """
    G = G_original.copy()
    c4_list = []
    
    for e in G.edges():
        x, y = e

        left_set = set(G.neighbors(x)) - set(G.neighbors(y)) - {y}
        right_set = set(G.neighbors(y)) - set(G.neighbors(x)) - {x}

        for v in left_set:
            for w in right_set:
                if G.has_edge(v, w):
                    c4 = frozenset([v, x, y, w])
                    c4_list.append(c4)

        G.remove_edge(x, y) # This is an error because it can create C4s

    return c4_list
