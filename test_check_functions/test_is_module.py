import networkx as nx
import unittest
import itertools
from functions.check_functions import *

# 26 Tests and 56 Asserts
class TestIsModule(unittest.TestCase):

# 1. Trivial Cases
    def test_empty_set(self):
        G = nx.path_graph(5)
        self.assertTrue(is_module(G, set()))

    def test_single_node_set(self):
        G = nx.path_graph(5)
        self.assertTrue(is_module(G, {0})) 

    def test_full_graph_subset(self):
        G = nx.complete_graph(3)
        self.assertTrue(is_module(G, set(G.nodes())))

# 2. Valid Modules in Common Structures
    def test_star_graph(self):
        G = nx.star_graph(4)  # center = 0, leaves = 1–4
        leaves = {1, 2, 3, 4}
        # All leaves together are a module
        self.assertTrue(is_module(G, leaves))
        # Any proper subset of leaves is also a module
        self.assertTrue(is_module(G, {1, 2}))
        self.assertTrue(is_module(G, {3}))
        self.assertTrue(is_module(G, {4}))
        # Mixed leaf and center is not a module
        self.assertFalse(is_module(G, {0, 1}))
        self.assertFalse(is_module(G, {0, 2, 3}))

    def test_complex_star(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5),
                          (5, 6), (6, 7)])
        self.assertTrue(is_module(G, {2, 3, 4}))

    def test_disconnected_module(self):
        G = nx.Graph()
        G.add_edges_from([(1, 24), (2, 24), (3, 24)])  # All connect only to 24
        self.assertTrue(is_module(G, {1, 2, 3}))

    def test_isolated_subset(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 24, 25])
        G.add_edges_from([(24, 25)])  # only outside the subset
        self.assertTrue(is_module(G, {1, 2, 3}))

    def test_module_with_isolated_node(self):
        G = nx.Graph()
        G.add_edges_from([(1, 24), (2, 24)])
        G.add_node(26)  # isolated node
        self.assertTrue(is_module(G, {26}))
        self.assertTrue(is_module(G, {1, 2}))

    def test_non_integer_node_labels(self):
        G = nx.Graph()
        G.add_edges_from([('apple', 'banana'), ('banana', 'cherry'), 
                          ('apple', 'cherry')])
        self.assertTrue(is_module(G, {'apple', 'banana'})) 
        self.assertTrue(is_module(G, {'banana', 'cherry'}))

    def test_repeated_nodes(self):
        G = nx.complete_graph(3)  # Nodes 0,1,2
        self.assertTrue(is_module(G, [0, 0, 1]))  # duplicates shouldn't affect

# 3. Invalid Modules (Structural Reasons)
    def test_non_module(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
        self.assertFalse(is_module(G, {1, 2}))  # nodes connect differently

    def test_nbr_overlap(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])
        # 1 connects to both, 4 only to 3 -> no module
        self.assertFalse(is_module(G, {2, 3}))

    def test_partially_connected_node(self):
        G = nx.Graph()
        G.add_edges_from([
            (1, 2), (1, 3),
            (2, 3), (3, 4)])
        self.assertFalse(is_module(G, {2, 3}))

# 4. Invalid Subset Inputs (Node Membership)
    def test_subset_not_in_graph(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3)])
        self.assertFalse(is_module(G, {4, 5}))
        self.assertFalse(is_module(G, {2, 999}))

# 5. Input Validation (Type and None Checks)
    def test_invalid_module_inputs(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3)])
        self.assertFalse(is_module(None, {1}))
        self.assertFalse(is_module("not a graph", {1}))
        self.assertFalse(is_module(G, None))
        self.assertFalse(is_module(G, 123))
        self.assertFalse(is_module(G, 1))
        self.assertFalse(is_module(G, [[1], [2]]))
        self.assertFalse(is_module(G, [1, '1']))       # mixed types
        self.assertFalse(is_module(G, {26}))          # node not in graph

# 6. Parameterized / Bulk Tests for Coverage
    def test_all_subsets_in_clique_are_modules(self):
        G = nx.complete_graph(5)
        nodes = list(G.nodes)
        for i in range(1, 6):
            for subset in itertools.combinations(nodes, i):
                with self.subTest(subset=subset):
                    self.assertTrue(is_module(G, set(subset)))

    def test_large_disconnected_module(self):
        G = nx.empty_graph(100)
        self.assertTrue(is_module(G, set(range(50))))
        self.assertTrue(is_module(G, set(range(90, 100))))

# 7. Edge Case Tests
    def test_self_loops_do_not_break_module(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3)])
        G.add_edge(2, 2)  # self-loop on node 2
        self.assertTrue(is_module(G, {2}))
        self.assertFalse(is_module(G, {1, 2}))

# 8. Additional Explicit Test Cases
    def test_module_with_isolated_nodes_and_edges(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (4, 5)])
        G.add_node(6)  # isolated node
        self.assertTrue(is_module(G, {6}))           # isolated node alone
        self.assertFalse(is_module(G, {3, 6}))       # mixed isolated and connected
        self.assertTrue(is_module(G, {4, 5}))        # edge forms module
        self.assertFalse(is_module(G, {2, 4}))       # nodes with inconsistent neighborhoods

    def test_module_with_subsets_in_path_graph(self):
        G = nx.path_graph(5)  # 0-1-2-3-4
        self.assertTrue(is_module(G, {0}))            # single node
        self.assertFalse(is_module(G, {0, 1}))        # neighbors differ
        self.assertFalse(is_module(G, {1, 2}))        # neighbors differ
        self.assertFalse(is_module(G, {2, 3, 4}))     # mixed neighbors

    def test_module_with_overlapping_neighborhoods(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
        self.assertFalse(is_module(G, {1, 2}))        # neighborhood differs
        self.assertTrue(is_module(G, {2, 3, 4}))

    def test_module_with_non_hashable_node_fails(self):
        G = nx.Graph()
        G.add_node(1)
        self.assertFalse(is_module(G, [{1}])) # TypeError handled in function and returns false

    def test_module_empty_graph(self):
        G = nx.Graph()
        self.assertTrue(is_module(G, set()))
        self.assertFalse(is_module(G, {1}))
        self.assertTrue(is_module(G, set()))

    def test_module_non_node_types(self):
        G = nx.path_graph(3)
        self.assertFalse(is_module(G, [None]))
        self.assertFalse(is_module(G, [object()]))
        self.assertFalse(is_module(G, [{1}]))

    def test_module_with_duplicate_nodes_in_list(self):
        G = nx.complete_graph(4)
        self.assertTrue(is_module(G, [0, 1, 1, 2]))  # duplicates ignored
        self.assertTrue(is_module(G, [3, 3]))

    def test_module_single_node_in_disconnected_graph(self):
        G = nx.empty_graph(3)
        self.assertTrue(is_module(G, {1}))
        self.assertTrue(is_module(G, {0, 1}))  # all isolated nodes form modules

if __name__ == '__main__':
    unittest.main()
