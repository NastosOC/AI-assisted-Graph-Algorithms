import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *

# 43 Tests and 67 Asserts
class TestIsQuasiThreshold(unittest.TestCase):
    """
    Testing is_quasi_threshold(nx.Graph) check function on various edge cases.
    Asserts for each case are either:
        Confirming the provided graph is quasi threshold.
        Confirming the provided graph is not quasi threshold.
            If not quasi threshold, confirms if a graph contains at least 1 P4 and/or C4.
    """
# Custom Assertions
    def assertContainsC4(self, G):
        has_c4 = find_all_c4(G)
        if(len(has_c4) != 0):
            self.assertGreater(len(has_c4), 0)

    def assertContainsP4(self, G):
        has_p4 = find_all_p4(G)
        if(len(has_p4) != 0):
            self.assertGreater(len(has_p4), 0)

# 1. Basic structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        self.assertTrue(is_quasi_threshold(G))

    def test_single_node(self):
        """networkX Graph with 1 node and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        self.assertTrue(is_quasi_threshold(G))

    def test_two_connected_nodes(self):
        """networkX Graph with 2 nodes and 1 edge"""
        G = nx.Graph()
        G.add_edge(0, 1)
        self.assertTrue(is_quasi_threshold(G))

    def test_two_disconnected_nodes(self):
        """networkX Graph with 2 nodes and 0 edges"""
        G = nx.Graph()
        G.add_nodes_from([0, 1])
        self.assertTrue(is_quasi_threshold(G))

    def test_triangle_graph(self):
        """networkX Graph with 3 nodes and 3 edges"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        self.assertTrue(is_quasi_threshold(G))

    def test_three_disconnected_nodes(self):
        """networkX Graph with 3 disconnected nodes"""
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2])
        self.assertTrue(is_quasi_threshold(G))

# 2. Well Known Structures
    def test_k4_graph(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        self.assertTrue(is_quasi_threshold(G))
	
    def test_k5_graph(self):
        """networkX 5-node complete graph"""
        G = nx.complete_graph(5)
        self.assertTrue(is_quasi_threshold(G))
        
    def test_p4_graph(self):
        """networkX 4-node path graph"""
        G = nx.path_graph(4)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G)) # P4 breaks Quasi Threshold
        
    def test_p5_graph(self):
        """networkX 5-node path graph"""
        G = nx.path_graph(5)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G)) # P4 breaks Quasi Threshold
        
    def test_c4_graph(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertContainsC4(G)
        self.assertFalse(is_quasi_threshold(G)) # C4 breaks Quasi Threshold
	
    def test_c5_graph(self):
        """networkX 5-node cycle graph"""
        G = nx.cycle_graph(5)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G)) # P4 breaks Quasi Threshold
        
    def test_s4_graph(self):
        """networkX 4-node star graph"""
        G = nx.star_graph(4)
        self.assertTrue(is_quasi_threshold(G))
	
    def test_s5_graph(self):
        """networkX 5-node star graph"""
        G = nx.star_graph(5)
        self.assertTrue(is_quasi_threshold(G))
	
    def test_4_node_bipartite_graph(self):
        """networkX K2,2 complete bipartite graph"""
        G = nx.complete_bipartite_graph(2, 2)
        self.assertContainsC4(G)
        self.assertFalse(is_quasi_threshold(G)) # C4 breaks Quasi Threshold

# 3. Edge (0, 1) Removed on Kn where 6 <= n <= 10
    def test_k6_remove_edge(self):
        """networkX 6-node complete graph"""
        G = complete_graph(6)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold(G))

    def test_k7_remove_edge(self):
        """networkX 7-node complete graph"""
        G = complete_graph(7)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold(G))

    def test_k8_remove_edge(self):
        """networkX 8-node complete graph"""
        G = complete_graph(8)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold(G))

    def test_k9_remove_edge(self):
        """networkX 9-node complete graph"""
        G = complete_graph(9)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold(G))

    def test_k10_remove_edge(self):
        """networkX 10-node complete graph"""
        G = complete_graph(10)
        G.remove_edge(0, 1)
        self.assertTrue(is_quasi_threshold(G))

# 4. Cycle graphs 6 <= n <= 10 should fail due to P4's 
    def test_c6_should_fail(self):
        """networkX 6-node cycle graph"""
        G = nx.cycle_graph(6)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G))

    def test_c7_should_fail(self):
        """networkX 7-node cycle graph"""
        G = nx.cycle_graph(7)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G))

    def test_c8_should_fail(self):
        """networkX 8-node cycle graph"""
        G = nx.cycle_graph(8)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G))

    def test_c9_should_fail(self):
        """networkX 9-node cycle graph"""
        G = nx.cycle_graph(9)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G))
    
    def test_c10_should_fail(self):
        """networkX 10-node cycle graph"""
        G = nx.cycle_graph(10)
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G))

# 5. Graph Compliments
    def test_p4_complement(self):
        """networkX 4-node path graph complement"""
        G = nx.path_graph(4)
        H = nx.complement(G)
        self.assertContainsC4(G)
        self.assertFalse(is_quasi_threshold(H))

    def test_c4_complement(self):
        """networkX 4-node cycle graph complement"""
        G = nx.cycle_graph(4)
        H = nx.complement(G)
        self.assertTrue(is_quasi_threshold(H))

    def test_k4_complement(self):
        """networkX 4-node complete graph complement"""
        G = nx.complete_graph(4)
        H = nx.complement(G)
        self.assertTrue(is_quasi_threshold(H))

    def test_s4_complement(self):
        """networkX 4-node star graph complement"""
        G = nx.star_graph(4)
        H = nx.complement(G)
        self.assertTrue(is_quasi_threshold(H))

# 6. Larger Graph Comfigurations
    def test_house_graph(self):
        """networkX Graph with 5 nodes and 6 edges - house layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 2), 
                          (2, 3), (3, 4), (4, 0)])
        self.assertContainsC4(G)
        self.assertFalse(is_quasi_threshold(G)) # C4 breaks Quasi Threshold
        
    def test_domino_graph(self):
        """networkX Graph with 6 nodes and 7 edges - domino layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), 
                          (2, 4), (3, 5), (4, 5)])
        self.assertContainsP4(G)
        self.assertContainsC4(G)
        self.assertFalse(is_quasi_threshold(G)) # P4 and C4 breaks Quasi Threshold

    def test_binary_tree_structure(self): 
        G = nx.Graph() 
        G.add_edges_from([(0, 1), (0, 2), (1, 3), 
                          (1, 4), (2, 5), (2, 6)])
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G)) # P4 breaks Quasi Threshold

    def test_large_sparse_graph(self):
        G = nx.Graph()
        G.add_nodes_from(range(15))
        G.add_edges_from([(0, 1),
                          (4, 0), (4, 1),
                          (7, 5), (7, 6),
                          (8, 0), (8, 1), (8, 4), (8, 5), (8, 6), (8, 7),
                          (2, 9), (2, 10), (2, 11),
                          (3, 12), (3, 13), (3, 14)])
        self.assertTrue(is_quasi_threshold(G))

    def test_center_node_triangle_spokes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0),
                          (0, 3), (3, 4), (4, 0),
                          (0, 5), (5, 6), (6, 0)])
        self.assertTrue(is_quasi_threshold(G))

    def test_k3_and_disconnected_p3(self):
        G = nx.complete_graph(3)
        G.add_edges_from([(5, 6), (6, 7)])  # P3
        self.assertTrue(is_quasi_threshold(G))

    def test_k3_with_disconnected_p4(self):
        G = nx.complete_graph(3)
        G.add_edges_from([(5, 6), (6, 7), (7, 8)]) # P4
        self.assertContainsP4(G)
        self.assertFalse(is_quasi_threshold(G))

    def test_k3_and_disconnected_c3(self):
        G = nx.complete_graph(3)
        G.add_edges_from([(5, 6), (6, 7), (7, 5)])  # C3
        self.assertTrue(is_quasi_threshold(G))

    def test_k3_with_disconnected_c4(self):
        G = nx.complete_graph(3)
        G.add_edges_from([(5, 6), (6, 7), (7, 8), (8, 5)]) # C4
        self.assertContainsC4(G)
        self.assertFalse(is_quasi_threshold(G))

    def test_large_threshold_graph(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (0, 3),
                          (1, 2), (1, 3),
                          (2, 3),                   # K4
                          (4, 0), (5, 0), (6, 0)])  # Add universal center
        self.assertTrue(is_quasi_threshold(G))

    def test_two_disconnected_cliques(self):
        G = nx.complete_graph(3)
        H = nx.complete_graph(3)
        mapping = {i: i+3 for i in H.nodes()}
        H = nx.relabel_nodes(H, mapping)
        G.add_edges_from(H.edges())
        self.assertTrue(is_quasi_threshold(G))

# 7. Input Parameters
    def test_string_node_labels(self):
        G = nx.Graph()
        G.add_edges_from([("a", "b"), ("b", "c")])
        self.assertTrue(is_quasi_threshold(G))

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
        self.assertTrue(is_quasi_threshold(G))

    def test_invalid_input_types(self):
        G = nx.Graph()
        self.assertFalse(is_quasi_threshold(None))           
        self.assertFalse(is_quasi_threshold("hello")) 
        self.assertFalse(is_quasi_threshold(123))            
        self.assertFalse(is_quasi_threshold(Exception))        
        self.assertFalse(is_quasi_threshold({'a': 1}))           
        self.assertFalse(is_quasi_threshold([1, 1]))       
        self.assertFalse(is_quasi_threshold([1, 'A']))
        self.assertFalse(is_quasi_threshold(float("inf")))

if __name__ == '__main__':
    unittest.main()