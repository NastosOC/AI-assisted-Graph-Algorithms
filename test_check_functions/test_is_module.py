import networkx as nx
import unittest
import itertools
from functions.check_functions import *

# 29 Tests and 96 Asserts
class TestIsModule(unittest.TestCase):
    """
    Testing is_module(nx.Graph, node_set) check function on various edge cases.
    Asserts for each case are either:
        Confirming provided nodes make a valid Module
        Confirming provided nodes do not make a valid Module
    """
# 1. Basic Structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        self.assertTrue(is_module(G, set()))
        
    def test_single_node(self):
        """networkX Graph with 1 node and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        self.assertTrue(is_module(G, {0}))
        
    def test_two_connected_nodes(self):
        """networkX Graph with 2 nodes and 1 edge"""
        G = nx.Graph()
        G.add_edge(0, 1)
        self.assertTrue(is_module(G, {0}))
        self.assertTrue(is_module(G, {1}))
        
    def test_two_disconnected_nodes(self):
        """networkX Graph with 2 nodes and 0 edges"""
        G = nx.Graph()
        G.add_nodes_from([0, 1])
        self.assertTrue(is_module(G, {0, 1}))
        
    def test_triangle_graph(self):
        """networkX Graph with 3 nodes and 3 edges"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        self.assertTrue(is_module(G, {0, 1}))
        self.assertTrue(is_module(G, {0, 2}))
        self.assertTrue(is_module(G, {1, 2}))
        
    def test_k4_graph(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        # 2-node Modules
        self.assertTrue(is_module(G, {0, 1}))
        self.assertTrue(is_module(G, {1, 2}))
        self.assertTrue(is_module(G, {2, 3}))
        # 3-node Modules
        self.assertTrue(is_module(G, {0, 1, 2}))
        self.assertTrue(is_module(G, {1, 2, 3}))
        self.assertTrue(is_module(G, {0, 2, 3}))
        
    def test_k5_graph(self):
        """networkX 5-node complete graph"""
        G = nx.complete_graph(5)
        # 2-node Modules
        self.assertTrue(is_module(G, {0, 1}))
        self.assertTrue(is_module(G, {1, 2}))
        self.assertTrue(is_module(G, {2, 3}))
        # 3-node Modules
        self.assertTrue(is_module(G, {0, 1, 2}))
        self.assertTrue(is_module(G, {1, 2, 3}))
        self.assertTrue(is_module(G, {0, 2, 3}))
        # 4-node Modules
        self.assertTrue(is_module(G, {0, 1, 2, 3}))
        self.assertTrue(is_module(G, {1, 2, 3, 4}))
        self.assertTrue(is_module(G, {0, 2, 3, 4}))
        
    def test_p4_graph(self):
        """networkX 4-node path graph"""
        G = nx.path_graph(4)
        # Singleton Nodes
        self.assertTrue(is_module(G, {0}))
        self.assertTrue(is_module(G, {3}))
        # Differing Neighbors
        self.assertFalse(is_module(G, {0, 1}))
        self.assertFalse(is_module(G, {1, 2}))

    def test_p5_graph(self):
        """networkX 5-node path graph"""
        G = nx.path_graph(5)
        # Singleton Nodes
        self.assertTrue(is_module(G, {0}))
        self.assertTrue(is_module(G, {3}))
        self.assertTrue(is_module(G, {4}))
        # Differing Neighbors
        self.assertFalse(is_module(G, {0, 1}))
        self.assertFalse(is_module(G, {1, 2}))
        self.assertFalse(is_module(G, {2, 3}))
        
    def test_c4_graph(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertTrue(is_module(G, {0}))      # Singleton
        self.assertFalse(is_module(G, {0, 1}))  # Neighbors differ
        self.assertFalse(is_module(G, {1, 2}))  # Neighbors differ
        self.assertTrue(is_module(G, {0, 2}))  # Opposite nodes
        
    def test_c5_graph(self):
        """networkX 5-node cycle graph"""
        G = nx.cycle_graph(5)
        self.assertTrue(is_module(G, {2}))      # Singleton
        self.assertFalse(is_module(G, {0, 1}))  # Neighbors differ
        self.assertFalse(is_module(G, {1, 2}))  # Neighbors differ
        
    def test_s4_graph(self):
        """networkX 4-node star graph"""
        G = nx.star_graph(4) # 0 -> Central Node
        leaves = {1, 2, 3}
        self.assertTrue(is_module(G, leaves))
        self.assertFalse(is_module(G, {0, 1}))
        
    def test_s5_graph(self):
        """networkX 5-node star graph"""
        G = nx.star_graph(5)
        leaves = {1, 2, 3, 4}
        self.assertTrue(is_module(G, leaves))
        self.assertFalse(is_module(G, {0, 1}))
        
    def test_4_node_bipartite_graph(self):
        """networkX K2,2 complete bipartite graph"""
        G = nx.complete_bipartite_graph(2, 2)
        part1 = {0, 1}
        part2 = {2, 3}
        self.assertTrue(is_module(G, part1))
        self.assertTrue(is_module(G, part2))
        self.assertFalse(is_module(G, {0, 2}))

    def test_5_node_bipartite_graph(self):
        """networkX K3,2 complete bipartite graph"""
        G = nx.complete_bipartite_graph(3, 2)
        part1 = {0, 1, 2}
        part2 = {3, 4}
        self.assertTrue(is_module(G, part1))
        self.assertTrue(is_module(G, part2))
        self.assertFalse(is_module(G, {0, 3}))
        self.assertFalse(is_module(G, {1, 4}))

    def test_k222_complete_multipartite(self):
        """Test K2,2,2 complete multipartite graph modules"""
        G = nx.complete_multipartite_graph(2, 2, 2)
        part1 = {0, 1}
        part2 = {2, 3}
        part3 = {4, 5}

        # Each part should be a module
        self.assertTrue(is_module(G, part1))
        self.assertTrue(is_module(G, part2))
        self.assertTrue(is_module(G, part3))

        # Mixed sets should not be modules
        self.assertFalse(is_module(G, {0, 2}))
        self.assertFalse(is_module(G, {1, 4}))
        self.assertFalse(is_module(G, {0, 1, 2}))
        self.assertFalse(is_module(G, {2, 3, 4}))


# 2. More Complex Structures
    def test_complex_star(self):
        """networkX Graph with 7 nodes and 6 edges"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 5),
                          (5, 6), (6, 7)])
        self.assertTrue(is_module(G, {2, 3, 4}))

    def test_disconnected_module(self):
        """networkX Graph with 6 nodes and 3 edges"""
        G = nx.Graph()
        G.add_edges_from([(1, 24), (2, 24), (3, 24)])   # Star
        G.add_nodes_from([23, 25])                      # Noise
        self.assertTrue(is_module(G, {1, 2, 3}))

    def test_isolated_subset(self):
        """networkX Graph with 5 nodes and 1 edge"""
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 24, 25])
        G.add_edges_from([(24, 25)])  # only outside the subset
        self.assertTrue(is_module(G, {1, 2, 3}))

    def test_large_disconnected_module(self):
        """networkX Graph with 100 nodes and 0 edges"""
        G = nx.Graph()
        G.add_nodes_from(range(100))
        self.assertTrue(is_module(G, set(range(50))))
        self.assertTrue(is_module(G, set(range(90, 100))))

    def test_module_with_isolated_nodes_and_edges(self):
        """networkX Graph with 6 nodes and 3 edges"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (4, 5)])
        G.add_node(6)  # isolated node
        self.assertTrue(is_module(G, {6}))           # isolated node alone
        self.assertFalse(is_module(G, {3, 6}))       # mixed isolated and connected
        self.assertTrue(is_module(G, {4, 5}))        # edge forms module
        self.assertFalse(is_module(G, {2, 4}))       # nodes with inconsistent neighborhoods

# 3. Additional Structures
    def test_non_module(self):
        """networkX Graph with 4 nodes and 5 edges - chorded C4"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
        self.assertFalse(is_module(G, {1, 2}))  # nodes connect differently

    def test_partially_connected_node(self):
        """networkX Graph with 4 nodes and 4 edges - non-cycle and non-path"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])
        self.assertFalse(is_module(G, {2, 3}))

    def test_nodes_with_same_external_neighbors_but_disconnected_internal(self):
        """networkX Graph with 4 nodes and 3 edges"""
        G = nx.Graph()
        G.add_edges_from([(1, 5), (2, 5), (3, 5),
                          (1, 4), (2, 4), (3, 4)])  
        self.assertTrue(is_module(G, {1, 2, 3}))

    def test_all_subsets_in_k4(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        # Singleton Nodes
        self.assertTrue(is_module(G, {0}))
        self.assertTrue(is_module(G, {1}))
        self.assertTrue(is_module(G, {2}))
        self.assertTrue(is_module(G, {3}))
        # 2-node Combinations
        self.assertTrue(is_module(G, {0, 1}))
        self.assertTrue(is_module(G, {0, 2}))
        self.assertTrue(is_module(G, {0, 3}))
        self.assertTrue(is_module(G, {1, 2}))
        self.assertTrue(is_module(G, {1, 3}))
        self.assertTrue(is_module(G, {2, 3}))
        # 3-node Combinations
        self.assertTrue(is_module(G, {0, 1, 2}))
        self.assertTrue(is_module(G, {0, 2, 3}))
        self.assertTrue(is_module(G, {1, 2, 3}))
        # 4-node Combination
        self.assertTrue(is_module(G, {0, 1, 2, 3}))

# 4. Different Inputs
    def test_duplicate_nodes_in_input(self):
        G = nx.complete_graph(3)
        self.assertTrue(is_module(G, [0, 1, 1]))
        self.assertTrue(is_module(G, [2, 2]))

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
        G.add_edges_from([(a, b), (b, c), (c, d)])
        self.assertTrue(is_module(G, [a, b, c, d]))

    def test_string_node_labels(self):
        """networkX Graph with strings as node labels"""
        G = nx.Graph()
        G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D')])
        self.assertTrue(is_module(G, ['A', 'B', 'C', 'D']))

    def test_invalid_input_types(self):
        G = nx.Graph()
        self.assertFalse(is_module(G, None))           
        self.assertFalse(is_module(G, "hello")) 
        self.assertFalse(is_module(G, 123))            
        self.assertFalse(is_module(G, Exception))        
        self.assertFalse(is_module(G, {'a': 1}))           
        self.assertFalse(is_module(G, [1, 1]))       
        self.assertFalse(is_module(G, [1, 'A']))
        self.assertFalse(is_module(G, float("inf"))) 

if __name__ == '__main__':
    unittest.main()
