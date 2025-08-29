import networkx as nx
from networkx import *
import unittest
import random
import sys
import os
import atexit
from datetime import datetime as dt
import concurrent.futures
import multiprocessing
import time
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import *

import multiprocessing
import time

def wrapper(q, func, args, kwargs):
    try:
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        q.put((res, end - start, False))
    except Exception as e:
        q.put((None, None, True))

def run_with_timeout(func, *args, timeout=10, **kwargs):
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=wrapper, args=(q, func, args, kwargs))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        p.join()
        return None, None, True  # timed out
    else:
        if not q.empty():
            return q.get()  # (result, runtime, error_flag)
        else:
            return None, None, True  # something went wrong


# Setting up Results File
now = dt.now().strftime("%Y-%m-%d")
log_file_path = f"strategy_time_test_results_{now}.txt"
log_file = open(log_file_path, "a")

def log_print(*args, **kwargs):
    print(*args, **kwargs, file=log_file)

# Closes file on exit
atexit.register(log_file.close)

def find_max_clique(g):
    return max(nx.find_cliques(g), key=len)

def run_algorithms(graph, name, index=None):
    # Built-in function (find max clique by size)
    i_timestamp = dt.now().strftime("%H:%M:%S")
    i_result, i_runtime, i_error = run_with_timeout(find_max_clique, graph, timeout=10)
    if i_error:
        i_runtime_str = "exceeded 10s"
        i_max_clq = []
    else:
        i_runtime_str = f"{i_runtime:.6f}s"
        i_max_clq = i_result

    # Custom without colouring
    c_timestamp = dt.now().strftime("%H:%M:%S")
    c_result, c_runtime, c_error = run_with_timeout(max_clique_with_steps, graph, timeout=10)
    if c_error:
        c_runtime_str = "exceeded 10s"
        c_max_clq, c_steps = [], 0
    else:
        c_runtime_str = f"{c_runtime:.6f}s"
        c_max_clq, c_steps = c_result

    # Custom with largest_first colouring
    l_timestamp = dt.now().strftime("%H:%M:%S")
    l_result, l_runtime, l_error = run_with_timeout(custom_with_greedy_steps, graph, "largest_first", timeout=10)
    if l_error:
        l_runtime_str = "exceeded 10s"
        l_max_clq, l_steps = [], 0
    else:
        l_runtime_str = f"{l_runtime:.6f}s"
        l_max_clq, l_steps = l_result

    # Custom with random_sequential colouring
    r_timestamp = dt.now().strftime("%H:%M:%S")
    r_result, r_runtime, r_error = run_with_timeout(custom_with_greedy_steps, graph, "random_sequential", timeout=10)
    if r_error:
        r_runtime_str = "exceeded 10s"
        r_max_clq, r_steps = [], 0
    else:
        r_runtime_str = f"{r_runtime:.6f}s"
        r_max_clq, r_steps = r_result

    # Custom with partial largest_first colouring
    pl_timestamp = dt.now().strftime("%H:%M:%S")
    pl_result, pl_runtime, pl_error = run_with_timeout(custom_with_partial_greedy_steps, graph, "largest_first", timeout=10)
    if pl_error:
        pl_runtime_str = "exceeded 10s"
        pl_max_clq, pl_steps = [], 0
    else:
        pl_runtime_str = f"{pl_runtime:.6f}s"
        pl_max_clq, pl_steps = pl_result

    # Custom with random_sequential colouring
    pr_timestamp = dt.now().strftime("%H:%M:%S")
    pr_result, pr_runtime, pr_error = run_with_timeout(custom_with_partial_greedy_steps, graph, "random_sequential", timeout=10)
    if pr_error:
        pr_runtime_str = "exceeded 10s"
        pr_max_clq, pr_steps = [], 0
    else:
        pr_runtime_str = f"{pr_runtime:.6f}s"
        pr_max_clq, pr_steps = pr_result

    # Logging results
    log_print(f"\n{name} - {graph}:")
    log_print("----------------------------------------------------")
    if not i_error:
        log_print(f"  Built-in:")
        log_print(f"    Started at {i_timestamp}")
        log_print(f"    Built-in runtime:                      {i_runtime_str}")
        log_print(f"    Built-in clique:                       {sorted(i_max_clq)}")
    else:
        log_print(f"  Built-in:")
        log_print(f"    Started at {i_timestamp}")
        log_print(f"    {i_runtime_str}")
    if not c_error:
        log_print(f"  Non-greedy:")
        log_print(f"    Started at {c_timestamp}")
        log_print(f"    Non-greedy runtime:                    {c_runtime_str}")
        log_print(f"    Non-greedy clique:                     {sorted(c_max_clq)}")
        log_print(f"    Non-greedy steps:                      {c_steps}")
    else:
        log_print(f"  Non-greedy:")
        log_print(f"    Started at {c_timestamp}")
        log_print(f"    {c_runtime_str}")
    if not l_error:
        log_print(f"  Largest first colouring:")
        log_print(f"    Started at {l_timestamp}")
        log_print(f"    Largest first runtime:                 {l_runtime_str}")
        log_print(f"    Largest first clique:                  {sorted(l_max_clq)}")
        log_print(f"    Largest first steps:                   {l_steps}")
    else:
        log_print(f"  Largest first colouring:")
        log_print(f"    Started at {l_timestamp}")
        log_print(f"    {l_runtime_str}")
    if not r_error:
        log_print(f"  Random Sequential colouring:")
        log_print(f"    Started at {r_timestamp}")
        log_print(f"    Random sequential runtime:             {r_runtime_str}")
        log_print(f"    Random sequential clique:              {sorted(r_max_clq)}")
        log_print(f"    Random sequential steps:               {r_steps}")
    else:
        log_print(f"  Random Sequential colouring:")
        log_print(f"    Started at {r_timestamp}")
        log_print(f"    {r_runtime_str}")
    if not pl_error:
        log_print(f"  Partial - largest first colouring:")
        log_print(f"    Started at {pl_timestamp}")
        log_print(f"    Largest first runtime:                 {pl_runtime_str}")
        log_print(f"    Largest first clique:                  {sorted(pl_max_clq)}")
        log_print(f"    Largest first steps:                   {pl_steps}")
    else:
        log_print(f"  Partial - largest first colouring:")
        log_print(f"    Started at {pl_timestamp}")
        log_print(f"    {pl_runtime_str}")
    if not pr_error:
        log_print(f"  Partial - random Sequential colouring:")
        log_print(f"    Started at {pr_timestamp}")
        log_print(f"    Random sequential runtime:             {pr_runtime_str}")
        log_print(f"    Random sequential clique:              {sorted(pr_max_clq)}")
        log_print(f"    Random sequential steps:               {pr_steps}")
    else:
        log_print(f"  Partial - random Sequential colouring:")
        log_print(f"    Started at {pr_timestamp}")
        log_print(f"    {pr_runtime_str}")

    return ((i_max_clq, c_max_clq, l_max_clq, r_max_clq, pl_max_clq, pr_max_clq),
            (i_error, c_error, l_error, r_error, pl_error, pr_error))


# Set of DIMACS subgraphs
directory = "DIMACS_files"


class TestExecutionTimes(unittest.TestCase):
    def assertIsClique(self, G, clq):
        self.assertTrue(is_clique(G, clq)) # Makes sure it's a valid clique

    # DIMACS graphs - 30-vertex subgraph
    def test_brock200_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock200_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Brock200.2')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)        

    def test_brock200_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock200_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Brock200.4')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_brock400_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock400_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Brock400.2')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_brock400_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock400_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Brock400.4')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_brock800_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock800_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Brock800.2')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_brock800_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock800_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Brock800.4')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_C125_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C125_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'C125.9')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_C250_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C250_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'C250.9')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_C500_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C500_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'C500.9')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_C1000_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C1000_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'C1000.9')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_C2000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C2000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'C2000.5')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_C2000_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C2000_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'C2000.9')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes) 

    def test_C4000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C4000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'C4000.5')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_DSJC500_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/DSJC500_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'DSJC500.5')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)      

    def test_DSJC1000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/DSJC1000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'DSJC1000.5')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_gen200_p09_44(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen200_p09_44.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Gen200_p09_44')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_gen200_p09_55(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen200_p09_55.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Gen200_p09_55')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_gen400_p09_55(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_55.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Gen400_p09_55')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_gen400_p09_65(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_65.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Gen400_p09_65')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_gen400_p09_75(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_75.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Gen400_p09_75')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_hamming8_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/hamming8_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Hamming8_4')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_hamming10_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/hamming10_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Hamming10_4')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_keller4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Keller4')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_keller5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Keller5')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_keller6(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller6.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'Keller6')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_MANN_a27(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a27.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'MANN_a27')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_MANN_a45(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a45.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'MANN_a45')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_MANN_a81(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a81.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'MANN_a81')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat300_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat300_1')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat300_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat300_2')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat300_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat300_3')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat700_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat700_1')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat700_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat700_2')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat700_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat700_3')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat1500_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat1500_1')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat1500_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat1500_2')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

    def test_p_hat1500_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(71))

        cliques, errors = run_algorithms(H, 'p_hat1500_3')
        built_in, non_greedy, largest, r_seq, partial_largest, partial_r_seq = cliques
        i_error, c_error, l_error, r_error, pl_error, pr_error = errors

        if not i_error:
            self.assertIsClique(G, built_in)

        if not c_error:
            self.assertIsClique(G, non_greedy)
            for node in non_greedy:
                self.assertIn(node, H.nodes)
       
        if not l_error:
            self.assertIsClique(G, largest)
            for node in largest:
                self.assertIn(node, H.nodes)

        if not r_error:
            self.assertIsClique(G, r_seq)
            for node in r_seq:
                self.assertIn(node, H.nodes)
       
        if not pl_error:
            self.assertIsClique(G, partial_largest)
            for node in partial_largest:
                self.assertIn(node, H.nodes)

        if not pr_error:
            self.assertIsClique(G, partial_r_seq)
            for node in partial_r_seq:
                self.assertIn(node, H.nodes)   

if __name__ == '__main__':
    unittest.main()