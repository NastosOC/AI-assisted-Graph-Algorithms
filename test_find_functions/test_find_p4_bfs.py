import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *

# 15 Tests and 59 Asserts
class TestFindAllP4BFS(unittest.TestCase):
    # Custom Assertion
    def assertIsP4s(self, G, p4_list):
        for p4 in p4_list:
            self.assertTrue(is_p4(G, list(p4)))

    def assertAllValidNodes(self, G, p4_list):
        nodes = set(G.nodes)
        for p4 in p4_list:
            for node in p4:
                self.assertIn(node, nodes, f"Node {node} not in graph")

    def test_empty_graph(self):
        G = nx.Graph()

        actual = find_all_p4_bfs(G)
        expected_p4_list = []

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_too_small_graph(self):
        G = nx.path_graph(3)

        actual = find_all_p4_bfs(G)
        expected_p4_list = []

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_no_p4(self):
        G = nx.complete_graph(10)

        actual = find_all_p4_bfs(G)
        expected_p4_list = []

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_classic_p4(self):
        # Simple Trivial P4 layout - only 4 nodes
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4])
        G.add_edges_from([(1, 2), (2, 3), (3, 4)])

        actual = find_all_p4_bfs(G)
        expected_p4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_one_p4(self):
        # Single P4 among 6 nodes
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (2, 5), (2, 3), (3, 5), (3, 4)])

        actual = find_all_p4_bfs(G)
        expected_p4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_multi_p4(self):
        # Multiple P4's in small graph
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
        G.add_edges_from([(1, 2), (1, 5), (2, 3), (3, 4), (3, 7), (5, 6)])

        actual = find_all_p4_bfs(G)
        expected_p4_list = [(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 7), (1, 2, 5, 6)]

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_domino(self):
        # Domino graph layout
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

        actual = find_all_p4_bfs(G)
        expected_p4_list = [(1, 2, 3, 5), (1, 2, 4, 6), (1, 3, 4, 6), (1, 3, 5, 6), (2, 3, 4, 5), (2, 4, 5, 6)]

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_6_cycle(self):
        # C6 layout
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6)])

        actual = find_all_p4_bfs(G)
        expected_p4_list = [(1, 2, 3, 4), (1, 2, 3, 6), (1, 2, 5, 6), (1, 4, 5, 6), (2, 3, 4, 5), (3, 4, 5, 6)]

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_domino_comp(self):
        # Tests length of domino layout and its complement
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

        GC = nx.complement(G)

        actual_c = find_all_p4_bfs(GC)
        expected_p4_list = [(1, 2, 4, 6), (1, 3, 4, 6), (1, 3, 5, 6), (2, 1, 3, 5), (2, 4, 3, 5), (2, 4, 6, 5)]

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(GC, actual_c)
        self.assertAllValidNodes(G, actual_c)
        self.assertEqual(len(expected), len(actual_c))
        self.assertEqual(set(expected), set(actual_c))

    def test_6_cycle_comp(self):
        # Tests length of C6 layout and its complement
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6)])

        GC = nx.complement(G)

        actual_c = find_all_p4_bfs(GC)
        expected_p4_list = [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6), (4, 5, 6, 1), (5, 6, 1, 2), (6, 1, 2, 3)]

        expected = list(frozenset(p) for p in expected_p4_list)

        self.assertIsP4s(GC, actual_c)
        self.assertAllValidNodes(G, actual_c)
        self.assertEqual(len(expected), len(actual_c))
        self.assertEqual(set(expected), set(actual_c))

    def test_large_path_graph(self):
        G = nx.path_graph(15)

        actual = find_all_p4_bfs(G)
        expected_p4_count = 12

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        # Number of P4s in a path graph is n - 3
        self.assertEqual(expected_p4_count, len(actual))

    def test_multiple_components(self):
        G = nx.Graph()
        
        G.add_edges_from([(1, 2), (2, 3), (3, 4)])  # P4 here
        G.add_edges_from([(5, 6), (6, 7)])  # only 3 nodes: not enough
        G.add_node(8) # isolated

        actual = find_all_p4_bfs(G)
        expected_p4_list = [(1, 2, 3, 4)]

        expected = list(list(frozenset(p) for p in expected_p4_list))

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_multiple_disconnected_p4(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4),
                          (6, 7), (7, 8), (8, 9),
                          (11, 12), (12, 13), (13, 14)])
        
        actual = find_all_p4_bfs(G)
        expected_p4_list = [(1, 2, 3, 4), (6, 7, 8, 9), (11, 12, 13, 14)]

        expected = list(list(frozenset(p) for p in expected_p4_list))

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))
        

    def test_false_positive(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 3)]) # Triangle with a tail

        actual = find_all_p4_bfs(G)
        expected_p4_list = []

        expected = list(list(frozenset(p) for p in expected_p4_list))

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_non_integer_nodes(self):
        G = nx.Graph()
        G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd')])
        
        actual = find_all_p4_bfs(G)
        expected_p4_list = [('a', 'b', 'c', 'd')]

        expected = list(list(frozenset(p) for p in expected_p4_list))

        self.assertIsP4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

if __name__ == '__main__':
    unittest.main()