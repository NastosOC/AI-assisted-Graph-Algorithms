import networkx as nx
from networkx import find_cliques
from networkx.algorithms import bipartite
import unittest
import sys
import os
import atexit
from datetime import datetime as dt
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import *

longer_custom = 0

random_graphs_1000 = []
random_graphs_1200 = []
random_graphs_bipartite = []

# Create 100 1000-vertex graphs with an edge probability between 0.3% and 0.5% (with a preference to the mode 0.4%)
for i in range(100):
    p = random.triangular(0.003, 0.005, 0.004)
    G = nx.erdos_renyi_graph(1000, p)
    random_graphs_1000.append(G)

# Create 100 1200-vertex graphs with an edge probability between 0.03% and 0.05% (with a preference to the mode 0.04%)
for i in range(100):
    p = random.triangular(0.0003, 0.0005, 0.0004)
    G = nx.erdos_renyi_graph(90, p)
    random_graphs_1200.append(G)

# Create 100 bipartite graphs with an edge probability between 5% and 30%
for i in range(100):
    n_top = random.randint(10, 50)
    n_bottom = random.randint(10, 50)
    p = random.uniform(0.05, 0.3)
    G = bipartite.random_graph(n_top, n_bottom, p)
    random_graphs_bipartite.append(G)

# Setting up Results File
log_file_path = "sparse_bipartite_results.txt"
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

        global longer_custom
        # Keeps track of how many instances each algorithm take longer to complete
        if c_runtime > i_runtime:
            print("Custom took longer")
            longer_custom += 1

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

        global longer_custom
        # Keeps track of how many instances each algorithm take longer to complete
        if c_runtime > i_runtime:
            print("Custom took longer")
            longer_custom += 1

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

# Set of 100 1000-vertex erdos_renyi random graphs - built-in first
for i, G in enumerate(random_graphs_1000):
    test_name = f"test_1000v_random_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test(G, i))
    print(f"Added test: {test_name}")


# Set of 100 1000-vertex erdos_renyi random graphs - custom first
for i, G in enumerate(random_graphs_1000):
    test_name = f"test_1000v_swapped_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test_r(G, i))
    print(f"Added test: {test_name}")


# Set of 100 1200-vertex erdos_renyi random graphs - built-in first
for i, G in enumerate(random_graphs_1200):
    test_name = f"test_1200v_random_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test(G, i))
    print(f"Added test: {test_name}")

# Set of 100 1200-vertex erdos_renyi random graphs - custom first
for i, G in enumerate(random_graphs_1200):
    test_name = f"test_1200v_swapped_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test_r(G, i))
    print(f"Added test: {test_name}")

# Set of 100 bipartite random graphs - built-in first
for i, G in enumerate(random_graphs_bipartite):
    test_name = f"test_bipartite_random_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test(G, i))
    print(f"Added test: {test_name}")

# Set of 100 bipartite random graphs - custom first
for i, G in enumerate(random_graphs_bipartite):
    test_name = f"test_bipartite_swapped_{i:03}"  # For make_test()
    setattr(TestRandomPruning, test_name, make_test_r(G, i))
    print(f"Added test: {test_name}")

@atexit.register
def report_longer_custom():
    print(f"\nCustom algorithm took longer in {longer_custom} cases.")

if __name__ == '__main__':
    unittest.main()
