import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *

# 30 Tests and 149 Asserts
class TestFindAllC4(unittest.TestCase):
    """
    Testing find_all_c4(nx.Graph) function on various edge cases.
    Asserts for each case are either:
        Confirming the function finds all known C4s in a provided graph.
    """
# Custom Assertion
    def assertIsC4s(self, G, c4_list):
        for c4 in c4_list:
            self.assertTrue(is_c4(G, list(c4)), f"{c4} is not a valid C4")

    def assertAllValidNodes(self, G, c4_list):
        nodes = set(G.nodes)
        for c4 in c4_list:
            for node in c4:
                self.assertIn(node, nodes, f"Node {node} not in graph")

    def assertNoDuplicates(self, c4_list):
        self.assertEqual(len(c4_list), len(set(frozenset(p) for p in c4_list)), "Duplicate C4s found")

# 1. Basic Graph Structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_single_node(self):
        G = nx.Graph()
        G.add_node(0)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_k4_graph(self):
        G = nx.complete_graph(4)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_p4_graph(self):
        G = nx.path_graph(4)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))
    
    def test_c4_graph(self):
        G = nx.cycle_graph(4)

        actual = find_all_c4(G)
        expected_c4_list = [(0, 1, 2, 3)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_s4_graph(self):
        G = nx.star_graph(4)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_4_node_bipartite_graph(self):
        G = nx.complete_bipartite_graph(2, 2)

        actual = find_all_c4(G)
        expected_c4_list = [(0, 1, 2, 3)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

# 2. Kn Graphs with Edge (1, 2) Missing
    def test_k4_with_missing_edge(self):
        G = nx.complete_graph(4)
        G.remove_edge(1, 2)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_k5_with_missing_edge(self):
        G = nx.complete_graph(5)
        G.remove_edge(1, 2)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_k6_with_missing_edge(self):
        G = nx.complete_graph(6)
        G.remove_edge(1, 2)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_k7_with_missing_edge(self):
        G = nx.complete_graph(7)
        G.remove_edge(1, 2)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_k8_with_missing_edge(self):
        G = nx.complete_graph(8)
        G.remove_edge(1, 2)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_k9_with_missing_edge(self):
        G = nx.complete_graph(9)
        G.remove_edge(1, 2)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_k10_with_missing_edge(self):
        G = nx.complete_graph(10)
        G.remove_edge(1, 2)

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

# 3. Other Well Known Structures
    def test_house_graph(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4(G)
        expected_c4_list = [(0, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph_chord_varient_1(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 3), (1, 2), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4(G)
        expected_c4_list = [(0, 1, 2, 3)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph_chord_varient_2(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (1, 4), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4(G)
        expected_c4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph_chord_varient_3(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4(G)
        expected_c4_list = [(0, 1, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph_chord_varient_4(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (4, 0)])

        actual = find_all_c4(G)
        expected_c4_list = [(0, 1, 2, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_domino(self):
        # Domino graph layout
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

        actual = find_all_c4(G)
        expected_c4_list = [(1, 2, 4, 3), (3, 4, 6, 5)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))
    
    def test_domino_comp(self):
        # Tests length of domino layout and its complement
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

        GC = nx.complement(G)

        actual_c = find_all_c4(GC)
        expected_c4_list = [(1, 2, 5, 6)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(GC, actual_c)
        self.assertAllValidNodes(G, actual_c)
        self.assertNoDuplicates(actual_c)
        self.assertEqual(len(expected), len(actual_c))
        self.assertEqual(set(expected), set(actual_c))

    def test_6_cycle(self):
        # C6 layout
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6)])

        actual = find_all_c4(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_6_cycle_comp(self):
        # Tests length of C6 layout and its complement
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6)])

        GC = nx.complement(G)

        actual_c = find_all_c4(GC)
        expected_c4_list = [(1, 2, 4, 5), (1, 3, 4, 6), (2, 3, 5, 6)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(GC, actual_c)
        self.assertAllValidNodes(G, actual_c)
        self.assertNoDuplicates(actual_c)
        self.assertEqual(len(expected), len(actual_c))
        self.assertEqual(set(expected), set(actual_c))

# 4. Additional Mid-sized Structures
    def test_grid_graph_c4s(self):
        G = nx.grid_2d_graph(5, 5)  # 5x5 grid has many 4-cycles

        actual = find_all_c4(G)

        # Each 2x2 block is a C4
        expected_c4_count = (5 - 1) * (5 - 1)  # (rows-1)*(cols-1) = 16

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(expected_c4_count, len(actual))

    def test_multiple_components(self):
        G = nx.Graph()
        
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])  # C4 here
        G.add_edges_from([(5, 6), (6, 7)])  # only 3 nodes: not enough
        G.add_node(8) # isolated

        actual = find_all_c4(G)
        expected_c4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_multiple_disconnected_c4(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1),
                          (6, 7), (7, 8), (8, 9), (9, 6),
                          (11, 12), (12, 13), (13, 14), (14, 11)])
        
        actual = find_all_c4(G)
        expected_c4_list = [(1, 2, 3, 4), (6, 7, 8, 9), (11, 12, 13, 14)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_2_layered_c4s(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 5), (1, 2), (1, 3), (1, 5), (2, 4), (3, 5), (4, 5)])

        actual = find_all_c4(G)
        expected_c4_list = [(1, 2, 4, 5)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_2_layered_c4s_varient(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 3), (0, 4), (0, 5), (1, 2), (2, 3), (3, 4), (3, 5)])

        actual = find_all_c4(G)
        expected_c4_list = [(0, 1, 2, 3)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

# 5. Test Input Types
    def test_string_label_nodes(self):
        G = nx.Graph()
        G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')])
        
        actual = find_all_c4(G)
        expected_c4_list = [('a', 'b', 'c', 'd')]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_object_node_labels(self):
        """networkX Graph with objects as node labels"""
        class CustomNode:
            def __init__(self, name):
                self.name = name
            def __repr__(self):
                return f"Node({self.name})"
            def __hash__(self):
                return hash(self.name)
            def __eq__(self, other):
                return isinstance(other, CustomNode) and self.name == other.name
        a, b, c, d = CustomNode('a'), CustomNode('b'), CustomNode('c'), CustomNode('d')

        G = nx.Graph()
        G.add_edges_from([(a, b), (b, c), (c, d), (d, a)])
        
        actual = find_all_c4(G)
        expected_c4_list = [(a, b, c, d)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertNoDuplicates(actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

if __name__ == '__main__':
    unittest.main()