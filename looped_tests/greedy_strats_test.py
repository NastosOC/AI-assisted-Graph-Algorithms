import networkx as nx
import unittest
import random
import sys
import os
import atexit
from networkx import find_cliques
from networkx.algorithms import bipartite
from datetime import datetime as dt
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import *

# Random sets of Graphs
random_80 = []
for i in range(100):
    p = random.uniform(0.6, 0.9) # Random range between 60% to 90%
    G = nx.erdos_renyi_graph(80, p)
    random_80.append(G)

random_90 = []
for i in range(100):
    p = random.uniform(0.6, 0.9) # Random range between 60% to 90%
    G = nx.erdos_renyi_graph(90, p)
    random_90.append(G)

# Set of DIMACS subgraphs
directory = "DIMACS_files"

DIMACS_75 = []
DIMACS_80 = []
DIMACS_85 = []

for index, file in enumerate(os.listdir(directory)):
    filepath = os.path.join(directory, file)
    if os.path.isfile(filepath):
        G = read_dimacs_clq(filepath)
        H = G.subgraph(range(76))
        DIMACS_75.append(H)
        I = G.subgraph(range(81))
        DIMACS_80.append(I)
        J = G.subgraph(range(86))
        DIMACS_85.append(J)


# Setting up Results File
log_file_path = "greedy_strats_results_2.txt"
log_file = open(log_file_path, "a")

def log_print(*args, **kwargs):
    print(*args, **kwargs, file=log_file)

# Closes file on exit
atexit.register(log_file.close)

# Dynamically creates test cases when called
def make_test(graph, index, cat):
    """
    Parameters:
        graph (networkX.Graph()): The graph
        index (int): List position of the graph
        cat (str): Indicate if the graph is DIMACS, random, etc.
    """
    def test(self):
        try:
            # Built-in function
            t_1 = dt.now()
            i_max_clq = max(nx.find_cliques(graph), key=len)
            i_runtime = dt.now() - t_1

            # Custom without colouring function
            t_2 = dt.now()
            c_max_clq, c_steps = max_clique(graph)
            c_runtime = dt.now() - t_2

            # Custom with largest_first colouring function
            t_3 = dt.now()
            gl_max_clq, gl_steps = custom_with_greedy(graph, "largest_first")
            gl_runtime = dt.now() - t_3

            # Custom with random_sequential colouring function
            t_4 = dt.now()
            gr_max_clq, gr_steps = custom_with_greedy(graph, "random_sequential")
            gr_runtime = dt.now() - t_4

            # Print the results to a file
            log_print(f"\n{graph}:")
            log_print(f"This graph is a {cat} graph")
            log_print(f"----------------------------------------------------")
            log_print(f"  Built-in runtime:                          {i_runtime.total_seconds():.6f}s")
            log_print(f"  Custom non-greedy runtime:                 {c_runtime.total_seconds():.6f}s")
            log_print(f"  Largest first colouring runtime:           {gl_runtime.total_seconds():.6f}s")
            log_print(f"  Random sequential colouring runtime:       {gr_runtime.total_seconds():.6f}s")
            log_print(f"\n Cliques:")
            log_print(f"  Built-in clique:                           {sorted(i_max_clq)}")
            log_print(f"  Custom non-greedy clique:                  {sorted(c_max_clq)}")
            log_print(f"  Largest first colouring clique:            {sorted(gl_max_clq)}")
            log_print(f"  Random sequential colouring clique:        {sorted(gr_max_clq)}")
            log_print(f"\n Steps:")
            log_print(f"  Built-in steps:                            NOT YET AVAILABLE")
            log_print(f"  Custom non-greedy steps:                   {c_steps}")
            log_print(f"  Largest first colouring steps:             {gl_steps}")
            log_print(f"  Random sequential colouring steps:         {gr_steps}")

            if not is_clique(graph, gl_max_clq):
                raise AssertionError(f"Graph {index}: Custom result (largest_first) is not a valid clique.")
            self.assertEqual(len(i_max_clq), len(gl_max_clq))

            if not is_clique(graph, gr_max_clq):
                raise AssertionError(f"Graph {index}: Custom result (random_sequential) is not a valid clique.")
            self.assertEqual(len(i_max_clq), len(gr_max_clq))

        except Exception as e:
            graph6 = nx.to_graph6_bytes(graph).decode().strip()
            # Logs a detailed summary of failure
            with open("test_failures.txt", "a") as log_file:
                log_file.write(f"\n--- Test Failure for Graph {index} ---\n")
                log_file.write(f"Graph6: {graph6}\n")
                log_file.write(f"Error: {str(e)}\n")
                log_file.write("--------------------------------------\n")

            # Save only Graph6 string to a separate file
            with open("failed_graphs.txt", "a") as g6_file:
                g6_file.write(f"{graph6}\n")
                              
            raise  # Important: keep this so unittest marks it as failed

    return test

class TestRandomStrats(unittest.TestCase):
    pass

# 100 tests on 80-verticies w/ random edge probability
for i, G in enumerate(random_80):
    test_name = f"test_80v_random_{i:03}"
    setattr(TestRandomStrats, test_name, make_test(G, i, "Random"))

# 100 tests on 900-verticies w/ random edge probability
for i, G in enumerate(random_90):
    test_name = f"test_90v_random_{i:03}"
    setattr(TestRandomStrats, test_name, make_test(G, i, "Random"))

# 32 tests on 75-verticies DIMACS subgraph
for i, G in enumerate(DIMACS_75):
    test_name = f"test_75v_DIMACS_{i:03}"
    setattr(TestRandomStrats, test_name, make_test(G, i, "DIMACS"))

# 32 tests on 80-verticies DIMACS subgraph
for i, G in enumerate(DIMACS_80):
    test_name = f"test_80v_DIMACS_{i:03}"
    setattr(TestRandomStrats, test_name, make_test(G, i, "DIMACS"))

# 32 tests on 85-verticies DIMACS subgraph
for i, G in enumerate(DIMACS_85):
    test_name = f"test_85v_DIMACS_{i:03}"
    setattr(TestRandomStrats, test_name, make_test(G, i, "DIMACS"))

if __name__ == '__main__':
    unittest.main()
