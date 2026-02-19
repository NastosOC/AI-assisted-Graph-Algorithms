import networkx as nx
from networkx import *
import matplotlib.pyplot as plt
import itertools 
from itertools import *
import math
import random
from collections import defaultdict

from functions.check_functions import *
from functions.find_functions import *

def branch_and_bound(G):
    """
    AI Generated method.
    Finds the maximum clique in an undirected graph using a branch-and-bound 
    algorithm with pruning based on a greedy coloring heuristic.
    Parameters:
        G (networkx.Graph): The graph.
    Returns:
        best_clique: A set of nodes representing the largest clique found in the G.
    """
    # n = G.number_of_nodes()
    best_clique = []
    order = list(G.nodes)  # Initial order can be simply the node list

    coloring = greedy_coloring_heuristic(G, order)
    
    # Sort nodes by color
    order.sort(key=lambda x: coloring[x])

    def extend(clique, candidates):
        """
        Recursively attempts to grow a clique from the current set of candidates, using 
        branch-and-bound to prune search paths that cannot yield a better solution than 
        the current best.
        Parameters:
            clique: A list of nodes representing the current partial clique being explored.
            candidates:  list of nodes that are potential extensions to the current clique.
        """
        nonlocal best_clique
        if not candidates:
            if len(clique) > len(best_clique):
                best_clique = clique[:]
            return
        
        for node in candidates[:]:
            new_clique = clique + [node]
            new_candidates = [n for n in candidates
                              if G.has_edge(node, n)]
            
            #Prune branched based on greedy coloring
            max_color = max((coloring[n] for n in new_candidates), default = -1)
            if len(new_clique) + max_color + 1 <= len(best_clique):
                continue
                
            # Recur
            extend(new_clique, new_candidates)

    # Initialize recursive search
    extend([], order)
    
    return set(best_clique)

def greedy_coloring_heuristic(G, order):
    """
    AI Generated helper method.
    Assigns colours to each node using a greedy algorithm.
    Parameters:
        G (networkx.Graph): The G.
        order: A list of nodes specifying the order to assign colours.
    Returns:
        coloring: A dictionary mapping each node to its assigned colour (int)
    """
    coloring = {}
    for node in order:
        """
        available_colors = set(range(len(G)))
        for neighbor in G[node]:
            if neighbor in coloring:
                available_colors.discard(coloring[neighbor])
        # Assign the smallest available color
        coloring[node] = min(available_colors)
        """
        # Get colours used by neighbors
        used_colors = {coloring[neighbor]
                       for neighbor in G[node]
                       if neighbor in coloring}
        # Assign smallest unused colour
        color = 0
        while color in used_colors:
            color += 1
        coloring[node] = color

    return coloring

def Bron_Kerbosch(G):
    """
    https://stackoverflow.com/questions/28406314/iterative-version-of-the-bron-kerbosch-algorithm
    Edited with the help of AI
    Finds and prints all maximal cliques in an undirected graph using 
    the iterative Bron–Kerbosch algorithm.
    Parameters:
        G (networkx.Graph): the graph
    Returns:
        maximum (set): A set of all nodes in the maximum clique found.
    """
    candidates = G.nodes()
    search_stack = [] # Stack to simulate recursion

    clique = set()
    excluded_vertices = set()
    search_stack.append((clique, candidates, excluded_vertices))

    maximal_cliques = []

    while search_stack:
        clique, candidates, excluded_vertices = search_stack.pop()

        if not candidates and not excluded_vertices:
            maximal_cliques.append(clique)
            continue
        if candidates:
            vertex = next(iter(candidates)) # Pick vertex from candidates

            search_stack.append((
                clique, # Keep current clique unchanged
                candidates - {vertex}, # Remove vertex from candidates
                excluded_vertices | {vertex} # Add vertex to excleded set
            ))

            search_stack.append((
                clique | {vertex}, # Add vertex to clique
                candidates & set(G.neighbors(vertex)), # Candidates that are neighbors of vertex
                excluded_vertices & set(G.neighbors(vertex)) # Excluded vertices that are neighbors of vertex
            ))

    maximum = max(maximal_cliques, key=len)
    return set(maximum)

def max_clique(G, nodes=None):
    """
    AI Generated method.
    Finds the maximum clique in an undirected graph using a bron-kerbosch 
    algorithm with pruning based on a bounding function.
    Parameters:
        G (networkx.Graph): The graph.
        nodes (list): optional
    Returns:
        set(max_clique): A set of nodes representing the largest clique found in the G.
    """
    if len(G) == 0:
        return set()

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = nodes[:] if nodes is not None else []
    cand = set(G)

    # If user provided initial clique nodes, verify they form a clique
    for node in Q:
        if node not in cand:
            raise ValueError(f"The given `nodes` {nodes} do not form a clique")
        cand &= adj[node] # Intersect candidates with neighbors of current node

    # If no candidates left - return what we have in Q
    if not cand:
        return set(Q[:])

    subg = cand.copy()
    stack = [] # Stack to simulate recursion

    Q.append(None) # Place holder for new nodes

    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    max_clique = Q[:-1]

    try:
        while True:
            if ext_u:
                # Pick a node from ext_u to try adding to clique
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q 

                adj_q = adj[q] 
                subg_q = subg & adj_q 

                if not subg_q:
                    if len(Q) > len(max_clique):
                        max_clique = Q[:] # Found larger clique
                else:
                    # Reduce candidate set to only neighbors of q
                    cand_q = cand & adj_q

                    if len(Q) + len(cand_q) > len(max_clique):
                        stack.append((subg, cand, ext_u))
                        Q.append(None)

                        #Update state for recursive call
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                # Backtrack: no more extension nodes to try
                Q.pop()
                if not stack:
                    break 
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

    return set(max_clique)

def max_clique_with_steps(G, nodes=None):
    """
    AI Generated method.
    Finds the maximum clique in an undirected graph using a bron-kerbosch 
    algorithm with pruning based on a bounding function.
    Additionally keeps track of the steps taken by the algorithm.
    Parameters:
        G (networkx.Graph): The graph.
        nodes (list): optional
    Returns:
        set(max_clique): A set of nodes representing the largest clique found in the G.
        step_count (int): The number of steps taken by the algorithm.
    """
    if len(G) == 0:
        return set(), 0

    adj = {u: {v for v in G[u] if v != u} for u in G}

    Q = nodes[:] if nodes is not None else []
    cand = set(G)

    # If user provided initial clique nodes, verify they form a clique
    for node in Q:
        if node not in cand:
            raise ValueError(f"The given `nodes` {nodes} do not form a clique")
        cand &= adj[node] # Intersect candidates with neighbors of current node

    # If no candidates left - return what we have in Q
    if not cand:
        return set(Q[:]), 0

    subg = cand.copy()
    stack = [] # Stack to simulate recursion

    Q.append(None) # Place holder for new nodes

    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    max_clique = Q[:-1]  
    step_count = 0

    try:
        while True:
            step_count += 1
            if ext_u:
                # Pick a node from ext_u to try adding to clique
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q 

                adj_q = adj[q] 
                subg_q = subg & adj_q 

                if not subg_q:
                    if len(Q) > len(max_clique):
                        max_clique = Q[:] # Found larger clique
                else:
                    # Reduce candidate set to only neighbors of q
                    cand_q = cand & adj_q

                    if len(Q) + len(cand_q) > len(max_clique):
                        stack.append((subg, cand, ext_u))
                        Q.append(None)

                        #Update state for recursive call
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                # Backtrack: no more extension nodes to try
                Q.pop()
                if not stack:
                    break 
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

    return set(max_clique), step_count

def custom_with_greedy(G, str_mode, nodes=None):
    """
    Based off the AI Generated method max_clique().
    Finds the maximum clique in an undirected graph using a bron-kerbosch 
    algorithm with pruning based on a greedy colouring function provided by networkX.
    Parameters:
        G (networkx.Graph): The graph.
        str_mode (string): The colouring strategy used by the greedy colouring function.
        nodes (list): optional
    Returns:
        set(max_clique): A set of nodes representing the largest clique found in the G.
    """
    if len(G) == 0:
        return set()

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = nodes[:] if nodes is not None else []
    cand = set(G)

    # If user provided initial clique nodes, verify they form a clique
    for node in Q:
        if node not in cand:
            raise ValueError(f"The given `nodes` {nodes} do not form a clique")
        cand &= adj[node] # Intersect candidates with neighbors of current node

    # If no candidates left - return what we have in Q
    if not cand:
        return set(Q[:])

    subg = cand.copy()
    stack = [] # Stack to simulate recursion

    Q.append(None) # Place holder for new nodes

    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    max_clique = Q[:-1]

    try:
        while True:
            if ext_u:
                # Pick a node from ext_u to try adding to clique
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q 

                adj_q = adj[q] 
                subg_q = subg & adj_q 

                if not subg_q:
                    if len(Q) > len(max_clique):
                        max_clique = Q[:] # Found larger clique
                else:
                    # Reduce candidate set to only neighbors of q
                    cand_q = cand & adj_q

                    if len(Q) + max(greedy_color(G.subgraph(cand_q), strategy=str_mode).values(), default=-1) + 1 > len(max_clique):
                        stack.append((subg, cand, ext_u))
                        Q.append(None)

                        #Update state for recursive call
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                # Backtrack: no more extension nodes to try
                Q.pop()
                if not stack:
                    break 
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

    return set(max_clique)

def custom_with_partial_greedy(G, str_mode, nodes=None):
    """
    Based off the AI Generated method max_clique().
    Finds the maximum clique in an undirected graph using a bron-kerbosch 
    algorithm with pruning based on a greedy colouring function provided by networkX.
    Greedy colouring function only runs every 3 iterations.
    Parameters:
        G (networkx.Graph): The graph.
        str_mode (string): The colouring strategy used by the greedy colouring function.
        nodes (list): optional
    Returns:
        set(max_clique): A set of nodes representing the largest clique found in the G.
    """
    if len(G) == 0:
        return set()

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = nodes[:] if nodes is not None else []
    cand = set(G)

    # If user provided initial clique nodes, verify they form a clique
    for node in Q:
        if node not in cand:
            raise ValueError(f"The given `nodes` {nodes} do not form a clique")
        cand &= adj[node] # Intersect candidates with neighbors of current node

    # If no candidates left - return what we have in Q
    if not cand:
        return set(Q[:])

    subg = cand.copy()
    stack = [] # Stack to simulate recursion

    Q.append(None) # Place holder for new nodes

    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    max_clique = Q[:-1]

    try:
        while True:
            if ext_u:
                # Pick a node from ext_u to try adding to clique
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q 

                adj_q = adj[q] 
                subg_q = subg & adj_q 

                if not subg_q:
                    if len(Q) > len(max_clique):
                        max_clique = Q[:] # Found larger clique
                else:
                    # Reduce candidate set to only neighbors of q
                    cand_q = cand & adj_q

                    if len(Q) % 3 == 0:
                        if len(Q) + max(greedy_color(G.subgraph(cand_q), strategy=str_mode).values(), default=-1) + 1 > len(max_clique):
                            stack.append((subg, cand, ext_u))
                            Q.append(None)

                            #Update state for recursive call
                            subg = subg_q
                            cand = cand_q
                            u = max(subg, key=lambda u: len(cand & adj[u]))
                            ext_u = cand - adj[u]
                    else:
                        if len(Q) + len(cand_q) > len(max_clique):
                            stack.append((subg, cand, ext_u))
                            Q.append(None)

                            #Update state for recursive call
                            subg = subg_q
                            cand = cand_q
                            u = max(subg, key=lambda u: len(cand & adj[u]))
                            ext_u = cand - adj[u]
            else:
                # Backtrack: no more extension nodes to try
                Q.pop()
                if not stack:
                    break 
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

    return set(max_clique)

def custom_with_greedy_steps(G, str_mode, nodes=None):
    """
    Based off the AI Generated method max_clique().
    Finds the maximum clique in an undirected graph using a bron-kerbosch 
    algorithm with pruning based on a greedy colouring function provided by networkX.
    Additionally keeps track of the steps taken by the algorithm.
    Parameters:
        G (networkx.Graph): The graph.
        str_mode (string): The colouring strategy used by the greedy colouring function.
        nodes (list): optional
    Returns:
        set(max_clique): A set of nodes representing the largest clique found in the G.
        step_count (int): The number of steps taken by the algorithm.
    """
    if len(G) == 0:
        return set(), 0

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = nodes[:] if nodes is not None else []
    cand = set(G)

    # If user provided initial clique nodes, verify they form a clique
    for node in Q:
        if node not in cand:
            raise ValueError(f"The given `nodes` {nodes} do not form a clique")
        cand &= adj[node] # Intersect candidates with neighbors of current node

    # If no candidates left - return what we have in Q
    if not cand:
        return set(Q[:]), 0

    subg = cand.copy()
    stack = [] # Stack to simulate recursion

    Q.append(None) # Place holder for new nodes

    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    max_clique = Q[:-1]

    steps = 0
    try:
        while True:
            steps += 1
            if ext_u:
                # Pick a node from ext_u to try adding to clique
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q 

                adj_q = adj[q] 
                subg_q = subg & adj_q 

                if not subg_q:
                    if len(Q) > len(max_clique):
                        max_clique = Q[:] # Found larger clique
                else:
                    # Reduce candidate set to only neighbors of q
                    cand_q = cand & adj_q

                    if len(Q) + max(greedy_color(G.subgraph(cand_q), strategy=str_mode).values(), default=-1) + 1 > len(max_clique):
                        stack.append((subg, cand, ext_u))
                        Q.append(None)

                        #Update state for recursive call
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                # Backtrack: no more extension nodes to try
                Q.pop()
                if not stack:
                    break 
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

    return set(max_clique), steps

def custom_with_partial_greedy_steps(G, str_mode, nodes=None):
    """
    Based off the AI Generated method max_clique().
    Finds the maximum clique in an undirected graph using a bron-kerbosch 
    algorithm with pruning based on a greedy colouring function provided by networkX.
    Greedy colouring function only runs every 3 iterations.
    Additionally keeps track of the steps taken by the algorithm.
    Parameters:
        G (networkx.Graph): The graph.
        str_mode (string): The colouring strategy used by the greedy colouring function.
        nodes (list): optional
    Returns:
        set(max_clique): A set of nodes representing the largest clique found in the G.
        step_count (int): The number of steps taken by the algorithm.
    """
    if len(G) == 0:
        return set(), 0

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = nodes[:] if nodes is not None else []
    cand = set(G)

    # If user provided initial clique nodes, verify they form a clique
    for node in Q:
        if node not in cand:
            raise ValueError(f"The given `nodes` {nodes} do not form a clique")
        cand &= adj[node] # Intersect candidates with neighbors of current node

    # If no candidates left - return what we have in Q
    if not cand:
        return set(Q[:]), 0

    subg = cand.copy()
    stack = [] # Stack to simulate recursion

    Q.append(None) # Place holder for new nodes

    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    max_clique = Q[:-1]

    steps = 0
    try:
        while True:
            steps += 1
            if ext_u:
                # Pick a node from ext_u to try adding to clique
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q 

                adj_q = adj[q] 
                subg_q = subg & adj_q 

                if not subg_q:
                    if len(Q) > len(max_clique):
                        max_clique = Q[:] # Found larger clique
                else:
                    # Reduce candidate set to only neighbors of q
                    cand_q = cand & adj_q

                    if len(Q) % 3 == 0:
                        if len(Q) + max(greedy_color(G.subgraph(cand_q), strategy=str_mode).values(), default=-1) + 1 > len(max_clique):
                            stack.append((subg, cand, ext_u))
                            Q.append(None)

                            #Update state for recursive call
                            subg = subg_q
                            cand = cand_q
                            u = max(subg, key=lambda u: len(cand & adj[u]))
                            ext_u = cand - adj[u]
                    else:
                        if len(Q) + len(cand_q) > len(max_clique):
                            stack.append((subg, cand, ext_u))
                            Q.append(None)

                            #Update state for recursive call
                            subg = subg_q
                            cand = cand_q
                            u = max(subg, key=lambda u: len(cand & adj[u]))
                            ext_u = cand - adj[u]
            else:
                # Backtrack: no more extension nodes to try
                Q.pop()
                if not stack:
                    break 
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass

    return set(max_clique), steps


"""
divanc() and edge_niche_centrality() require further investigation and possible rewriting.
Due to being more theoritical ideas - docstrings haven't been fully filled out.
"""
def divanc(G):
    G = G.copy()
    while any(nx.diameter(G.subgraph(c)) > 2 for c in nx.connected_components(G)):
        enc = edge_niche_centrality(G)
        emax = max(enc, key=enc.get)
        G.remove_edge(*emax)
    return [G.subgraph(c).copy() for c in nx.connected_components(G)]


def edge_niche_centrality(G):
    """Compute edge niche centrality for each edge in G."""
    enc = {}
    triangle_counts = defaultdict(int)
    for u in G:
        for v in G[u]:
            if u < v:
                common = set(G[u]) & set(G[v])
                triangle_counts[(u,v)] = len(common)

    for u, v in G.edges():
        neighbors_u = set(G[u]) - {v}
        neighbors_v = set(G[v]) - {u}
        p4_count = sum(1 for x in neighbors_u for y in neighbors_v if x != y and not G.has_edge(x, y))
        deg_term = min(len(G[u]) - 1, len(G[v]) - 1)
        triangles = triangle_counts.get((u, v), triangle_counts.get((v, u), 0))
        enc[(u, v)] = (p4_count + deg_term) / (triangles + 1)
    return enc
