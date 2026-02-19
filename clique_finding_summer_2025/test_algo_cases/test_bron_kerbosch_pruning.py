import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *
from functions.clique_algorithms import *

# 25 Tests and 122 Asserts
class TestBronKerboschPruning(unittest.TestCase):
    """
    Testing max_clique(nx.Graph) algorithm on various edge cases.
    ---THIS IS A PRUNING VARIANT OF THE BRON KERBOSCH ALGORITHM---
    Asserts for each case run through:
        Confirming the clique the algorithm finds is a valid clique
        Confirming all nodes exist within the graph
        A sanity test confirming the clique size is not 0 (unless the graph is empty)
        A sanity test confirming the clique size does not exceed the number of nodes in the graph
        A final check for correct max clique length
    """
# Custom Assertions
    def assertIsClique(self, G, clq):
        """
        Assert that clq is a valid clique.
        Parameters:
            G (networkX.Graph): The graph
            clq (list): List of nodes
        """
        self.assertTrue(is_clique(G, clq), f"{clq} is not a valid clique")
		
    def assertAllValidNodes(self, G, v):
        """
        Assert that clq nodes all exist in G.
        Parameters:
            G (networkX.Graph): The graph
            clq (list): List of nodes
        """
        nodes = set(G.nodes)
        for node in v:
            self.assertIn(node, nodes, f"Node {node} not in graph")


# 1. Basic Structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertEqual(0, len(max_clq))
        
    def test_single_node(self):
        """networkX Graph with 1 node and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(1, len(max_clq))

    def test_two_connected_nodes(self):
        """networkX Graph with 2 nodes and 1 edge"""
        G = nx.Graph()
        G.add_edge(0, 1)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq))

    def test_triangle(self):
        """networkX Graph with 3 nodes and 2 edges"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(3, len(max_clq))
        
    def test_graph_with_no_edges(self):
        """networkX Graph with 5 nodes and 0 edges"""
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3, 4])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(1, len(max_clq))
        
    def test_k4_graph(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(4, len(max_clq))
        
    def test_k5_graph(self):
        """networkX 5-node complete graph"""
        G = nx.complete_graph(5)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(5, len(max_clq))
        
# 2. Further Graph Configurations
    def test_p4_graph(self):
        """networkX 4-node path graph"""
        G = nx.path_graph(4)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq)) # Max Clique should be size 2
        
    def test_c4_graph(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq)) # Max Clique should be size 2
        
    def test_s4_graph(self):
        """networkX 4-node star graph"""
        G = nx.star_graph(4)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq)) # Max Clique should be size 2

    def test_4_node_bipartite_graph(self):
        """networkX 4-node bipartite graph"""
        G = nx.complete_bipartite_graph(2, 2)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq)) # Max Clique should be size 2
            
    def test_domino_graph(self):
        """networkX Graph with 6 nodes and 7 edges - domino layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), 
                          (2, 4), (3, 5), (4, 5)])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq)) # Max Clique should be size 2
        
# 3. Complex Configurations
    def test_triangle_with_tail(self):
        """networkX Graph with 4 nodes and 4 edges - triangle with a tail"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0), (0, 3)])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(3, len(max_clq))
        
    def test_k4_bridged_with_triangle(self):
        """networkX Graph with a 4-clique and a 3-clique with an edge connecting them"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (0, 3), 
                          (1, 2), (1, 3), 
                          (2, 3), 
                          (3, 4),                   # Bridge
                          (4, 5), (4, 6), (5, 6)])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(4, len(max_clq))
        
    def test_triangle_with_isolated_nodes(self):
        """networkX Graph triangle with 3 isolated nodes"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        G.add_nodes_from([3, 4, 5])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(3, len(max_clq))
        
    def test_overlapping_cliques(self):
        """
        networkX Graph with 2 overlapping triangles
            [(0, 1), (1, 2), (0, 2)]
            [(2, 3), (3, 4), (2, 4)]
        """
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), 
                          (0, 2), (1, 3), (2, 4)])          
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(3, len(max_clq))
        
    def test_multiple_cliques_different_sizes(self):
        """networkX Graph with 3 different sized disconnected cliques"""
        G = nx.Graph()
        G.add_edges_from([(0, 1),                                           # Size 2
                          (2, 3), (3, 4), (4, 2),                           # Size 3
                          (5, 6), (5, 7), (5, 8), (6, 7), (6, 8), (7, 8)])  # Size 4
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(4, len(max_clq))
        
    def test_large_clique_with_noise(self):
        """networkX complete 5-node Graph with added nodes and edges"""
        G = nx.complete_graph(5)
        G.add_edges_from([(2, 10), (4, 6), (4, 7), (8, 9)]) # Noise
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(5, len(max_clq))
        
    def test_large_clique_sparse_graph(self):
        """networkX complete 7-node Graph with added nodes and edges"""
        G = nx.complete_graph(7)
        G.add_edges_from([(0, 7), (0, 13), (1, 8), (2, 14), 
                          (4, 8), (6, 9), (6, 14), (9, 10), 
                          (9, 11), (11, 13), (12, 14), (14, 15)])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(7, len(max_clq))

# 4. Large Graphs
    def test_k10_graph(self):
        """networkX complete 10-node Graph"""
        G = nx.complete_graph(10)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(10, len(max_clq)) 

    def test_p10_graph(self):
        """networkX 10-node path Graph"""
        G = nx.path_graph(10)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq)) # Max Clique should be size 2

    def test_c10_graph(self):
        """networkX 10-node cycle Graph"""
        G = nx.cycle_graph(10)
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(2, len(max_clq)) # Max Clique should be size 2

    def test_k5_in_25_node_graph(self):
        """25-node networkX Graph with a 5-node clique"""
        G = nx.complete_graph(5)
        G.add_nodes_from([5, 6, 11, 14])
        G.add_edges_from([(4, 7), (7, 8), (8, 4),
                          (0, 9), (0, 23),
                          (10, 12), (10, 13), (10, 15), (12, 13), (13, 15),
                          (16, 17), (16, 18), (16, 19),
                          (17, 18), (17, 19),
                          (18, 19),
                          (19, 24),
                          (21, 22), (22, 24)])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(5, len(max_clq))

# 5. Varying Input Types
    def test_string_node_labels(self):
        """networkX Graph with strings as node labels"""
        G = nx.Graph()
        G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(3, len(max_clq))

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
        a, b, c = CustomNode('a'), CustomNode('b'), CustomNode('c')

        G = nx.Graph()
        G.add_edges_from([(a, b), (b, c), (c, a)])
        max_clq = max_clique(G)
        
        self.assertIsClique(G, max_clq)
        self.assertAllValidNodes(G, max_clq)
        # Sanity Tests 
        self.assertGreater(len(max_clq), 0)
        self.assertLessEqual(len(max_clq), len(G.nodes))
        # Final Size Correctness Test
        self.assertEqual(3, len(max_clq))

if __name__ == '__main__':
    unittest.main()
