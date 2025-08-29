import networkx as nx
from networkx import find_cliques
import unittest
import sys
import os
import atexit
from datetime import datetime as dt
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import *

graphs = []
random_graphs_75 = []
random_graphs_90 = []
random_graphs_110 = []

G_1 = nx.erdos_renyi_graph(120, 0.5)
G_2 = nx.erdos_renyi_graph(100, 0.7)
G_3 = nx.erdos_renyi_graph(80, 0.9)

graphs.append(G_1)
graphs.append(G_2)
graphs.append(G_3)

# Create 100 75-vertex graphs with an edge probability between 50% and 90% (with a preference to the mode 70%)
for i in range(100):
    p = round(random.triangular(0.5, 0.9, 0.7), 1)
    G = nx.erdos_renyi_graph(75, p)
    random_graphs_75.append(G)

# Create 100 90-vertex graphs with an edge probability between 50% and 70% (with a preference to the mode 60%)
for i in range(100):
    p = round(random.triangular(0.5, 0.7, 0.6), 1)
    G = nx.erdos_renyi_graph(90, p)
    random_graphs_90.append(G)

# Create 100 110-vertex graphs with an edge probability between 40% and 60% (with a preference to the mode 50%)
for i in range(100):
    p = round(random.triangular(0.4, 0.6, 0.5), 1)
    G = nx.erdos_renyi_graph(110, p)
    random_graphs_110.append(G)

# Setting up Results File
log_file_path = "random_pruning_results.txt"
log_file = open(log_file_path, "a")

def log_print(*args, **kwargs):
    print(*args, **kwargs, file=log_file)

atexit.register(log_file.close)

# Dynamically creates test cases when called
def make_test(graph, index):
    def test(self):
        # Built-in function
        t_1 = dt.now()
        i_max_clq = max(nx.find_cliques(graph), key=len)
        i_runtime = dt.now() - t_1

        # Custom function
        t_2 = dt.now()
        c_max_clq = max_clique(graph)
        c_runtime = dt.now() - t_2

        # Keeps track of how many instances each algorithm take longer to complete
        if c_runtime > i_runtime:
            print("Custom took longer")

        # Print the results to a file
        log_print(f"\n{graph} - Built-in First:")
        log_print(f"----------------------------------------------------")
        log_print(f"  Built-in runtime: {i_runtime.total_seconds():.6f}s")
        log_print(f"  Custom runtime:   {c_runtime.total_seconds():.6f}s")
        log_print(f"\n  Built-in clique:  {sorted(i_max_clq)}")
        log_print(f"  Custom clique:    {sorted(c_max_clq)}")

        # If the clique found by custom is not a clique -> fail test
        if not is_clique(graph, c_max_clq):
            self.fail(f"Graph {index}: Custom result is not a valid clique.")
        # Check the length of the clique found by custom against the built-in function
        self.assertEqual(len(i_max_clq), len(c_max_clq))
    return test

# Dynamically creates test cases when called
def make_test_r(graph, index):
    def test(self):
        # Custom function
        t_2 = dt.now()
        c_max_clq = max_clique(graph)
        c_runtime = dt.now() - t_2

        # Built-in function
        t_1 = dt.now()
        i_max_clq = max(nx.find_cliques(graph), key=len)
        i_runtime = dt.now() - t_1

        # Keeps track of how many instances each algorithm take longer to complete
        if c_runtime > i_runtime:
            print("Custom took longer")

        # Print the results to a file
        log_print(f"\n{graph} - Custom First:")
        log_print(f"----------------------------------------------------")
        log_print(f"  Built-in runtime: {i_runtime.total_seconds():.6f}s")
        log_print(f"  Custom runtime:   {c_runtime.total_seconds():.6f}s")
        log_print(f"\n  Built-in clique:  {sorted(i_max_clq)}")
        log_print(f"  Custom clique:    {sorted(c_max_clq)}")

        # If the clique found by custom is not a clique -> fail test
        if not is_clique(graph, c_max_clq):
            self.fail(f"Graph {index}: Custom result is not a valid clique.")
        # Check the length of the clique found by custom against the built-in function
        self.assertEqual(len(i_max_clq), len(c_max_clq))
    return test

class TestRandomPruning(unittest.TestCase):
    pass


# Jim's suggested graphs - built-in first
for i, G in enumerate(graphs):
    test_name = f"test_jim_random_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test(G, i))
    print(f"Added test: {test_name}")


# Jim's suggested graphs custom first
for i, G in enumerate(graphs):
    test_name = f"test_jim_swapped_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test_r(G, i))
    print(f"Added test: {test_name}")


# Set of 100 75-vertex erdos_renyi random graphs - built-in first
for i, G in enumerate(random_graphs_75):
    test_name = f"test_75v_random_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test(G, i))
    print(f"Added test: {test_name}")


# Set of 100 75-vertex erdos_renyi random graphs - custom first
for i, G in enumerate(random_graphs_75):
    test_name = f"test_75v_swapped_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test_r(G, i))
    print(f"Added test: {test_name}")


# Set of 100 90-vertex erdos_renyi random graphs - built-in first
for i, G in enumerate(random_graphs_90):
    test_name = f"test_90v_random_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test(G, i))
    print(f"Added test: {test_name}")

# Set of 100 90-vertex erdos_renyi random graphs - custom first
for i, G in enumerate(random_graphs_90):
    test_name = f"test_90v_swapped_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test_r(G, i))
    print(f"Added test: {test_name}")

# Set of 100 110-vertex erdos_renyi random graphs - built-in first
for i, G in enumerate(random_graphs_110):
    test_name = f"test_110v_random_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test(G, i))
    print(f"Added test: {test_name}")

# Set of 100 110-vertex erdos_renyi random graphs - custom first
for i, G in enumerate(random_graphs_110):
    test_name = f"test_110v_swapped_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test_r(G, i))
    print(f"Added test: {test_name}")

if __name__ == '__main__':
    unittest.main()
