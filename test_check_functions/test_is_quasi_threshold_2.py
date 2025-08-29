import networkx as nx
import unittest
from functions.check_functions import *

# 27 Tests and 27 Asserts
class TestIsQuasiThreshold2(unittest.TestCase):

# 1. Simple structures
    def test_empty_graph(self):
        G = nx.Graph()
        self.assertTrue(is_quasi_threshold_2(G))

    def test_single_node(self):
        G = nx.Graph()
        G.add_node(0)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_two_connected_nodes(self):
        G = nx.Graph()
        G.add_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_three_connected_nodes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2)])
        self.assertTrue(is_quasi_threshold_2(G))

    def test_triangle_connected_nodes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        self.assertTrue(is_quasi_threshold_2(G))

    def test_p4_should_fail(self):
        G = nx.path_graph(4)
        self.assertFalse(is_quasi_threshold_2(G))

    def test_c4_should_fail(self):
        G = nx.cycle_graph(4)
        self.assertFalse(is_quasi_threshold_2(G))

    def test_k4_should_pass(self):
        G = complete_graph(4)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_s4_should_pass(self):
        G = star_graph(4)
        self.assertTrue(is_quasi_threshold_2(G))

# 2. Edge (0, 1) Removed on Kn where 4 <= n <= 10
    def test_k4_remove_edge(self):
        G = complete_graph(4)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_k5_remove_edge(self):
        G = complete_graph(5)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_k6_remove_edge(self):
        G = complete_graph(6)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_k7_remove_edge(self):
        G = complete_graph(7)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_k8_remove_edge(self):
        G = complete_graph(8)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_k9_remove_edge(self):
        G = complete_graph(9)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

    def test_k10_remove_edge(self):
        G = complete_graph(10)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold_2(G))

# 3. Additional Graph Configurations
    def test_center_node_triangle_spokes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0),
                          (0, 3), (3, 4), (4, 0),
                          (0, 5), (5, 6), (6, 0)])
        self.assertTrue(is_quasi_threshold_2(G))

    def test_k4_with_disconnected_p4(self):
        G = nx.complete_graph(4)
        G.add_edges_from([(5, 6), (6, 7), (7, 8)])
        self.assertFalse(is_quasi_threshold_2(G))

    def test_k4_with_disconnected_c4(self):
        G = nx.complete_graph(4)
        G.add_edges_from([(5, 6), (6, 7), (7, 8), (8, 5)])
        self.assertFalse(is_quasi_threshold_2(G))

    def test_complete_bipartite_graph(self):
        G = nx.complete_bipartite_graph(3, 3)
        self.assertFalse(is_quasi_threshold_2(G))

    def test_long_path_should_fail(self):
        G = nx.path_graph(5)
        self.assertFalse(is_quasi_threshold_2(G))

    def test_long_cycle_should_fail(self):
        G = nx.cycle_graph(5)
        self.assertFalse(is_quasi_threshold_2(G))

    def test_disconnected_quasi_threshold_components_pass(self):
        G = nx.Graph()
        G.add_edges_from(nx.complete_graph(3).edges()) # Add K3 Component
        G.add_edges_from(nx.star_graph(4).edges()) # Add Disconnected S4 Component
        self.assertTrue(is_quasi_threshold_2(G))

# 4. Graph Complements
    def test_p4_complement(self):
        G = nx.path_graph(4)
        H = nx.complement(G)
        self.assertFalse(is_quasi_threshold_2(H))

    def test_k4_complement(self):
        G = nx.complete_graph(4)
        H = nx.complement(G)
        self.assertTrue(is_quasi_threshold_2(H))

# 5. Non-numerical Inputs
    def test_string_node_labels(self):
        G = nx.Graph()
        G.add_edges_from([("a", "b"), ("b", "c")])
        self.assertTrue(is_quasi_threshold_2(G))

    def test_object_node_labels(self):
        class CustomNode:
            def __init__(self, name):
                self.name = name
            def __repr__(self):
                return f"Node({self.name})"
            def __hash__(self):
                return hash(self.name)
            def __eq__(self, other):
                return isinstance(other, CustomNode) and self.name == other.name

        a, b, c = CustomNode('a'), CustomNode('b'), CustomNode('c')

        G = nx.Graph()
        G.add_edges_from([(a, b), (b, c)])  # Simple P3 (should be quasi-threshold)
        self.assertTrue(is_quasi_threshold_2(G))


if __name__ == '__main__':
    unittest.main()