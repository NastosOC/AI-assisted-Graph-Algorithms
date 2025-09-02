import unittest
import networkx as nx
from functions.check_functions import *

# 36 Tests and 97 Asserts
class TestIsPrime(unittest.TestCase):
    """
    Testing is_prime(nx.Graph) check function on various edge cases.
    Asserts for each case confirm whether a graph is modularly prime.
        If not prime - Confirms the presence of a non-trivial module.
    Additionally confirms when a graph is connected or disconnected because disconnected graphs cannot be prime.
    """
    def assertContainsModule(self, G):
        """Assert that G contains at least one nontrivial module"""
        nodes = list(G.nodes())
        n = len(nodes)
        module_list = []
        # Check all nontrivial subsets (not singleton, not full graph)
        for r in range(2, n):
            for subset in combinations(nodes, r):
                if is_module(G, set(subset)):
                    module_list.append(set(subset))
        self.assertGreater(len(module_list), 0)
                    
# 1. Basic Structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_single_node(self):
        """networkX Graph with 1 node and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_two_connected_nodes(self):
        """networkX Graph with 2 nodes and 1 edge"""
        G = nx.Graph()
        G.add_edge(0, 1)
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_two_disconnected_nodes(self):
        """networkX Graph with 2 nodes and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        G.add_node(1)
        self.assertEqual(is_connected(G), False)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_triangle(self):
        """networkX Graph with 3 nodes and 3 edges"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (1, 3)])
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_disconnected_three_nodes(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3])
        self.assertEqual(is_connected(G), False)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

# 2. Well Known Structures
    def test_k4_graph(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_k5_graph(self):
        """networkX 5-node complete graph"""
        G = nx.complete_graph(5)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_p4_graph(self):
        """networkX 4-node path graph"""
        G = nx.path_graph(4)
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_p5_graph(self):
        """networkX 5-node path graph"""
        G = nx.path_graph(5)
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_p6_graph(self):
        """networkX 6-node path graph"""
        G = nx.path_graph(6)
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_c4_graph(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_c5_graph(self):
        """networkX 5-node cycle graph"""
        G = nx.cycle_graph(5)
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_c6_graph(self):
        """networkX 6-node cycle graph"""
        G = nx.cycle_graph(6)
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_s4_graph(self):
        """networkX 4-node star graph"""
        G = nx.star_graph(4)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_4_node_bipartite_graph(self):
        """networkX K2,2 complete bipartite graph"""
        G = nx.complete_bipartite_graph(2, 2)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_house_graph(self):
        """networkX Graph with 5 nodes and 6 edges - house layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 2), 
                          (2, 3), (3, 4), (4, 0)])
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_domino_graph(self):
        """networkX Graph with 6 nodes and 7 edges - domino layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), 
                          (2, 4), (3, 5), (4, 5)])
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

# 3. Mid-sized Structures
    def test_almost_module_fails(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 4)])
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))  # No true module

    def test_binary_tree_sructure(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2),
                          (1, 3), (1, 4), (2, 5), (2, 6)])
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G)) # Not modularily prime

    def test_irregular_tree_structure(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), 
                          (1, 3), (1, 4), 
                          (4, 5)])
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_graph_with_known_module(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 3),
                          (1, 4), (2, 4)])
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_prime_irregular_structure(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 4),
                          (3, 4), (4, 5)])
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_prime_irregular_structure_after_edge_addition(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 4),
                          (3, 4), (4, 5), (5, 3)]) 
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_k5_with_leaf(self):
        G = nx.complete_graph(5)
        G.add_edge(0, 5)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_connected_p4s(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])
        G.add_edges_from([(1, 2), (2, 3), (3, 4),
                          (5, 6), (6, 7), (7, 8),
                          (7, 2)])
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

# 4. Disconnected Graphs Should Fail
    def test_disconnected_components(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (3, 4)])
        self.assertEqual(is_connected(G), False)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_graph_with_all_isolated_nodes(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3, 4])
        self.assertEqual(is_connected(G), False) # Disconnected
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))  

    def test_multiple_disconnected_components(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3)])  # prime
        G.add_edges_from([(4, 5), (5, 6), (4, 6)]) 
        self.assertEqual(is_connected(G), False)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_two_disjoint_prime_components(self):
        G = nx.disjoint_union(nx.path_graph(3), nx.path_graph(4))
        self.assertEqual(is_connected(G), False)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

# 5. Additional Structures
    def test_true_twins(self):
        G = nx.Graph()
        G.add_edges_from([(0, 2), (1, 2), (0, 3), (1, 3)])
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_chorded_c4(self):
        G = nx.cycle_graph(4)
        G.add_edge(0, 2)
        self.assertEqual(is_connected(G), True)
        self.assertContainsModule(G)
        self.assertFalse(is_prime(G))

    def test_self_loops_ignored(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1)])
        G.add_edge(0, 0)  # self-loop
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

# Input Tests
    def test_string_labels(self):
        G = nx.Graph()
        G.add_edge('A', 'B')
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))
    
    def test_object_labels(self):
        class CustomNode:
            def __init__(self, name):
                self.name = name
            def __repr__(self):
                return f"Node({self.name})"
            def __hash__(self):
                return hash(self.name)
            def __eq__(self, other):
                return isinstance(other, CustomNode) and self.name == other.name

        a, b = CustomNode('a'), CustomNode('b')

        G = nx.Graph()
        G.add_edge(a, b)
        self.assertEqual(is_connected(G), True)
        self.assertTrue(is_prime(G))

    def test_invalid_input_types(self):
        G = nx.Graph()
        self.assertFalse(is_prime(None))           
        self.assertFalse(is_prime("hello")) 
        self.assertFalse(is_prime(123))            
        self.assertFalse(is_prime(Exception))        
        self.assertFalse(is_prime({'a': 1}))           
        self.assertFalse(is_prime([1, 1]))       
        self.assertFalse(is_prime([1, 'A']))
        self.assertFalse(is_prime(float("inf")))

if __name__ == '__main__':
    unittest.main()