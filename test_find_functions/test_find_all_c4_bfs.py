import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *

# 29 Tests and 101 Asserts
class TestFindAllC4BFS(unittest.TestCase):
    
    # Custom Assertion
    def assertIsC4s(self, G, c4_list):
        for c4 in c4_list:
            self.assertTrue(is_c4(G, list(c4)), f"{c4} is not a valid C4")

    def assertAllValidNodes(self, G, c4_list):
        nodes = set(G.nodes)
        for c4 in c4_list:
            for node in c4:
                self.assertIn(node, nodes, f"Node {node} not in graph")

    def test_empty_graph(self):
        G = nx.Graph()

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_too_small_graph(self):
        G = nx.cycle_graph(3)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_no_c4(self):
        G = nx.complete_graph(10)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_classic_c4(self):
        # Simple Trivial C4 layout - only 4 nodes
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4])
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_one_c4(self):
        # Single C4 among 6 nodes
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (4, 5), (5, 6)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_multi_c4(self):
        # Multiple C4's in small graph
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9])
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1),
                          (5, 6), (6, 7), (7, 8), (8, 5),
                          (4, 9), (5, 9)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 3, 4), (5, 6, 7, 8)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_domino(self):
        # Domino graph layout
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 4, 3), (3, 4, 6, 5)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_6_cycle(self):
        # C6 layout
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_domino_comp(self):
        # Tests length of domino layout and its complement
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6)])

        GC = nx.complement(G)

        actual_c = find_all_c4_bfs_broken(GC)
        expected_c4_list = [(1, 2, 5, 6)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(GC, actual_c)
        self.assertAllValidNodes(G, actual_c)
        self.assertEqual(len(expected), len(actual_c))
        self.assertEqual(set(expected), set(actual_c))

    def test_6_cycle_comp(self):
        # Tests length of C6 layout and its complement
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6])
        G.add_edges_from([(1, 2), (1, 6), (2, 3), (3, 4), (4, 5), (5, 6)])

        GC = nx.complement(G)

        actual_c = find_all_c4_bfs_broken(GC)
        expected_c4_list = [(1, 2, 4, 5), (1, 3, 4, 6), (2, 3, 5, 6)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(GC, actual_c)
        self.assertAllValidNodes(G, actual_c)
        self.assertEqual(len(expected), len(actual_c))
        self.assertEqual(set(expected), set(actual_c))

    def test_grid_graph_c4s(self):
        G = nx.grid_2d_graph(5, 5)  # 5x5 grid has many 4-cycles

        actual = find_all_c4_bfs_broken(G)

        # Each 2x2 block is a C4
        expected_c4_count = (5 - 1) * (5 - 1)  # (rows-1)*(cols-1) = 16

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(expected_c4_count, len(actual))

    def test_multiple_components(self):
        G = nx.Graph()
        
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])  # C4 here
        G.add_edges_from([(5, 6), (6, 7)])  # only 3 nodes: not enough
        G.add_node(8) # isolated

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_multiple_disconnected_p4(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1),
                          (6, 7), (7, 8), (8, 9), (9, 6),
                          (11, 12), (12, 13), (13, 14), (14, 11)])
        
        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 3, 4), (6, 7, 8, 9), (11, 12, 13, 14)]

        expected = list(frozenset(p) for p in expected_c4_list)


        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))
        

    def test_false_positive(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)]) # Triangle breaking C4

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_non_integer_nodes(self):
        G = nx.Graph()
        G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('a', 'd')])
        
        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [('a', 'b', 'c', 'd')]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertIsC4s(G, actual)
        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_K4_missing_edge(self):
        G = nx.complete_graph(4)
        G.remove_edge(0, 1)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_K5_missing_edge(self):
        G = nx.complete_graph(5)
        G.remove_edge(0, 1)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))
    
    def test_K6_missing_edge(self):
        G = nx.complete_graph(6)
        G.remove_edge(0, 1)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_K7_missing_edge(self):
        G = nx.complete_graph(7)
        G.remove_edge(0, 1)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_K8_missing_edge(self):
        G = nx.complete_graph(8)
        G.remove_edge(0, 1)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_K9_missing_edge(self):
        G = nx.complete_graph(9)
        G.remove_edge(0, 1)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_K10_missing_edge(self):
        G = nx.complete_graph(10)
        G.remove_edge(0, 1)

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = []

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(0, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))


    def test_house_graph_chord_varient_1(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 3), (1, 2), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(0, 1, 2, 3)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph_chord_varient_2(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (1, 4), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph_chord_varient_3(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (1, 3), (2, 3), (3, 4), (4, 0)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(0, 1, 3, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_house_graph_chord_varient_4(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (4, 0)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(0, 1, 2, 4)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_2_layered_c4s(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 5), (1, 2), (1, 3), (1, 5), (2, 4), (3, 5), (4, 5)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(1, 2, 4, 5)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

    def test_2_layered_c4s_varient(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 3), (0, 4), (0, 5), (1, 2), (2, 3), (3, 4), (3, 5)])

        actual = find_all_c4_bfs_broken(G)
        expected_c4_list = [(0, 1, 2, 3)]

        expected = list(frozenset(p) for p in expected_c4_list)

        self.assertAllValidNodes(G, actual)
        self.assertEqual(len(expected), len(actual))
        self.assertEqual(set(expected), set(actual))

if __name__ == '__main__':
    unittest.main()