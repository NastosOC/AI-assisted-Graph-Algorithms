import sys, collections
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt
from networkx.algorithms.clique import find_cliques

# Prefered not to use.
def __DISABLED__bors_kerbosch_naive(R, P, X, G, C):
    """
    From: https://github.com/alanmc-zz/python-bors-kerbosch/blob/master/bors-kerbosch.py
    Recursive implementation of the naive Bron–Kerbosch algorithm for finding all maximal cliques in an undirected graph.
    Parameters:
        R (set): The current growing clique (initially empty).
        P (set): The set of potential candidates to add to the clique (initially all graph nodes).
        X (set): The set of nodes already processed (to avoid duplicates).
        G (dict): The graph represented as an adjacency list (dictionary of sets).
        C (list): The list to store all discovered maximal cliques (each as a sorted list of nodes).
    """
    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            C.append(sorted(R))
        return 
    
    for v in P.union(set([])):
        bors_kerbosch_naive(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)

# Prefered not to use
def __DISABLED__bors_kerbosch_optimized(R, P, X, G, C):
    """
    From: https://github.com/alanmc-zz/python-bors-kerbosch/blob/master/bors-kerbosch.py
    Optimized recursive implementation of the Bron–Kerbosch algorithm using pivoting 
    to reduce the number of recursive calls when finding all maximal cliques.
    Parameters:
        R (set): The current growing clique (initially empty).
        P (set): The set of potential candidates to add to the clique (initially all graph nodes).
        X (set): The set of nodes already processed (to avoid duplicates).
        G (dict): The graph represented as an adjacency list (dictionary of sets).
        C (list): The list to store all discovered maximal cliques (each as a sorted list of nodes).
    """
    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            C.append(sorted(R))            
        return

    (d, pivot) = max([(len(G[v]), v) for v in P.union(X)])
                     
    for v in P.difference(G[pivot]):
        bors_kerbosch_optimized(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)

def __DISABLED__Bron_Kerbosch_Pivoting(G):
    """
    https://stackoverflow.com/questions/76141667/iterative-version-of-the-bron-kerbosch-algorithm-with-pivoting -ttnphns
    Translated with the help of AI for understanding variables.
    Finds and prints all maximal cliques in an undirected graph using 
    the iterative Bron–Kerbosch algorithm.
    Parameters:
        G (networkx.Graph): The graph.
    Returns:
        maximal_cliques (list): A list of all maximal cliques found.
    """
    nodes = set(G.nodes()) # A set of nodes of G
    clique = set() # A set to store the nodes of a clique
    excluded = set() # A set to store the nodes to be excluded
    pivot = None

    stack = []
    maximal_cliques = []

    stack.append((clique, nodes, excluded, pivot))

    while stack: # While stack is not empty
        clique, nodes, excluded, pivot = stack.pop()
        if not nodes and not excluded: # If nodes and excluded are both empty
            maximal_cliques.append(clique) # Set clique as a maximal clique
        else:
            nodes_U_excluded = nodes.union(excluded)
            if nodes_U_excluded:
                pivot_node = random.choice(list(nodes_U_excluded))
                pivot_neighbors = set(G.neighbors(pivot_node))
            else:
                pivot_node = None
                pivot_neighbors = set()

            diff = nodes - pivot_neighbors

            if diff:
                vertex = random.choice(list(diff))
                # EXCLUDE vertex (still the same clique)
                stack.append((clique, nodes - {vertex}, excluded.union({vertex}), pivot_node))

                # INCLUDE vertex (grow the clique)
                vertex_neighbors = set(G.neighbors(vertex))
                stack.append((clique.union({vertex}), nodes.intersection(vertex_neighbors), excluded.intersection(vertex_neighbors), pivot_node))

    return maximal_cliques

def __DISABLED__testing_subgraph(G, v):
    """
    Check if the nodes in list v form a clique in graph G.
    Parameters:
        G (networkx.Graph): The graph.
        v (list): List of nodes to check.   
    Returns:
        bool: True if v forms a clique, False otherwise.
    """
    # Better to be induced_subgraph
    subgraph = G.subgraph(v)
    print(G)
    draw_graph(G)
    
    print(subgraph)
    draw_graph(subgraph)
    G.add_edge(50, 51)

    print(G)
    draw_graph(G)

def __DISABLED__make_neighbor_function_nx(G):
    """
    Helper function created with the help of AI.
    Wraps a networkX Graph object and returns a function that, when called
    with a vertex, returns its neighbors as a set.
    Parameters:
        G (networkx.Graph): The graph.
    Returns:
        Callable: A function that takes a vertex and returns a set of neighbors.
    """
    def neighbor_function(v):
        return set(G.neighbors(v))  # uses G from the outer function
    return neighbor_function

def __DISABLED__Bron_Kerbosch_Pivoting(G):
    """
    https://stackoverflow.com/questions/28406314/iterative-version-of-the-bron-kerbosch-algorithm  -Janne Karila
    Edited with the help of AI to include pivoting.
    Finds and prints all maximal cliques in an undirected graph using 
    the iterative Bron–Kerbosch algorithm.
    Parameters:
        candidates (set): A set of all vertices in the graph.
        neighbor_function (Callable): A function that takes a vertex and
        returns a set of its neighboring vertices. Used to determine clique
        connectivity.
    Returns:
        maximal_cliques (list): A list of all maximal cliques found.
    """
    candidates = G.nodes()
    search_stack = []
    clique = set()
    excluded = set()
    search_stack.append((clique, candidates, excluded))

    maximal_cliques = []

    while search_stack:
        clique, candidates, excluded = search_stack.pop()

        if not candidates and not excluded:
            maximal_cliques.append(clique)
            continue

        # Pivot selection: vertex with max neighbors in candidates ∪ excluded
        pivot_candidates = candidates | excluded
        if pivot_candidates:
            pivot = max(pivot_candidates, key=lambda u: len(set(G.neighbors(u))))
        else:
            pivot = None

        # Explore vertices not connected to pivot to reduce branching
        ext_candidates = candidates - (set(G.neighbors(pivot)) if pivot else set())

        for vertex in ext_candidates:
            new_clique = clique | {vertex}
            new_candidates = candidates & set(G.neighbors(vertex))
            new_excluded = excluded & set(G.neighbors(vertex))
            search_stack.append((new_clique, new_candidates, new_excluded))

            #candidates.remove(vertex)
            excluded.add(vertex)

    return maximal_cliques

# Unnecessary
def __DISABLED__create_complement(G):
    return nx.complement(G)

def __DISABLED__find_all_p4_bfs_old(G):
    """
    Created with suggestions for improvement by AI.
    Uses BFS on a graph to build a list of P4s. If a 4-chain of nodes is found and it passes the
    P4 check it's added to the list, else ignored.
    Parameters:
        G (networkx.Graph): The graph.  
    Returns:
        p4_list (list): A list of all P4s found in the graph.
    """
    nodes = list(G.nodes()) # List of nodes in graph
    p4_list = []
    
    for node in nodes:
        queued = [[node]] #AI recommendation - keeping a list of a list of nodes
        while queued:
            path = queued.pop(0)

            # Checks if current path is a P4
            if len(path) == 4:
                if is_p4(G, path):
                    p4_list.append(path)
                continue

            last_node = path[-1]
            # Checks all neighbors of the last node in the path
            for nbr in G.neighbors(last_node):
                if nbr not in path:
                    new_path = path + [nbr]
                    queued.append(new_path)

    return p4_list

def __DISABLED__find_cliques_with_step(G, nodes=None):
    """
    Copied source code for find_cliques() and added in step_count variable to track the number of steps taken.
    Modified yeild lines to yeild both clique and 
    """
    if len(G) == 0:
        return

    adj = {u: {v for v in G[u] if v != u} for u in G}

    # Initialize Q with the given nodes and subg, cand with their nbrs
    Q = nodes[:] if nodes is not None else []
    cand = set(G)
    for node in Q:
        if node not in cand:
            raise ValueError(f"The given `nodes` {nodes} do not form a clique")
        cand &= adj[node]
    
    step_count = 0

    if not cand:
        yield Q[:], step_count
        return

    subg = cand.copy()
    stack = []
    Q.append(None)

    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]

    try:
        while True:
            step_count += 1
            if ext_u:
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q
                adj_q = adj[q]
                subg_q = subg & adj_q
                if not subg_q:
                    yield Q[:], step_count
                else:
                    cand_q = cand & adj_q
                    if cand_q:
                        stack.append((subg, cand, ext_u))
                        Q.append(None)
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                Q.pop()
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass