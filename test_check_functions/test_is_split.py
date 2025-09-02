import networkx as nx
import unittest
from functions.check_functions import *

# 39 Tests and 97 Asserts
class TestIsSplit(unittest.TestCase):
    """
    Testing is_split(nx.Graph, node_list) check function on various edge cases.
    Asserts for each case are either:
        Confirming the provided graph is a split graph.
            If split:
                Confirms the clique is a valid clique.
                Confirms the independent set is a valid independent set.
        Confirming the provided graph is not a split graph.
    """
# Custom Assertions
    def assertIsClique(self, G, clq):
        """
        Assert that clq is a valid clique.
        Parameters:
            G (networkX.Graph): The graph
            clq (list): List of nodes
        """
        self.assertTrue(is_clique(G, clq)) # Makes sure it's a valid clique

    def assertIsIsolatedSet(self, G, set):
        """
        Assert that set is a valid independent set.
        Parameters:
            G (networkX.Graph): The graph
            set (list): List of nodes
        """
        for u in set:
            for v in set:
                if u != v:
                    self.assertFalse(G.has_edge(u, v),
                        msg=f"{u} and {v} are connected — not an independent set.")
                    
# 1. Basic Structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        clq = []
        isolated = []
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_single_node(self):
        """networkX Graph with 1 node and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        clq = [0]
        isolated = []
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_two_connected_nodes(self):
        """networkX Graph with 2 nodes and 1 edge"""
        G = nx.Graph()
        G.add_edge(0, 1)
        clq = [0, 1]
        isolated = []
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_two_disconnected_nodes(self):
        """networkX Graph with 2 nodes and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        G.add_node(1)
        clq = [0]
        isolated = [1]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_k4_graph(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        clq = [0, 1, 2, 3]
        isolated = []
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_k5_graph(self):
        """networkX 5-node complete graph"""
        G = nx.complete_graph(5)
        clq = [0, 1, 2, 3, 4]
        isolated = []
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_p4_graph(self):
        """networkX 4-node path graph"""
        G = nx.path_graph(4)
        clq = [1, 2]
        isolated = [0, 3]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_p5_graph(self):
        """networkX 5-node path graph"""
        G = nx.path_graph(5)
        self.assertFalse(is_split(G))

    def test_c4_graph(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertFalse(is_split(G))

    def test_s4_graph(self):
        """networkX 4-node star graph"""
        G = nx.star_graph(4)
        clq = [0]
        isolated = [1, 2, 3]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_complete_four_node_bipartite_graph(self):
        """networkX 4-node complete bipartite graph"""
        G = nx.Graph()
        G.add_edges_from([(0, 2), (0, 3), (1, 2), (1, 3)])
        self.assertFalse(is_split(G))

    def test_house_graph(self):
        """networkX Graph with 5 nodes and 6 edges - house layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 2), 
                          (2, 3), (3, 4), (4, 0)])
        self.assertFalse(is_split(G))
        
    def test_domino_graph(self):
        """networkX Graph with 6 nodes and 7 edges - domino layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), 
                          (2, 4), (3, 5), (4, 5)])
        self.assertFalse(is_split(G))

# 2. Additional Small Configurations
    def test_two_connected_with_one_isolated_node(self):
        G = nx.Graph()
        G.add_edge(0, 1)
        G.add_node(2)
        clq = [0, 1]
        isolated = [2]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_two_disconnected_two_node_cliques(self):
        G = nx.Graph()
        G.add_edge(0, 1)
        G.add_edge(2, 3)
        self.assertFalse(is_split(G))

    def test_p3_graph(self):
        G = nx.path_graph(3)
        clq = [0, 1]
        isolated = [2]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_triangle_with_single_tail(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])
        clq = [0, 1, 2]
        isolated = [3]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_triangle_with_many_tails(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0), 
                          (2, 3), (1, 4), (0, 5)])
        clq = [0, 1, 2]
        isolated = [3, 4, 5]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        G.add_edges_from([(0, 1), (0, 3), (1, 2), (1, 4), (2, 0), (2, 5)])
        self.assertTrue(is_split(G))

    def test_triangle_with_isolated_nodes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        G.add_nodes_from([3, 4, 5])
        clq = [0, 1, 2]
        isolated = [3, 4, 5]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_triangle_with_tail_and_isolated_nodes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])
        G.add_nodes_from([4, 5])
        clq = [0, 1, 2]
        isolated = [3, 4, 5]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_isolated_nodes_connected_to_other_isolated_nodes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        G.add_nodes_from([3, 4, 5])
        G.add_edge(4, 5)
        self.assertFalse(is_split(G)) # Fails because of edge (4, 5)

    def test_isolated_nodes_connected_to_many_clique_nodes(self):
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0),
                          (3, 2), (3, 1),
                          (4, 0), (4, 2)])
        clq = [0, 1, 2]
        isolated = [3, 4]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_1_clique_node_connected_to_all_isolated_nodes(self):
        G = nx.complete_graph(3)
        G.add_edges_from([(0, 3), (0, 4), (0, 5)])
        clq = [0, 1, 2]
        isolated = [3, 4, 5]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_each_node_connected_to_all_isolated_nodes(self):
        G = nx.complete_graph(3)
        G.add_edges_from([(0, 3), (0, 4), (0, 5),
                          (1, 3), (1, 4), (1, 5),
                          (2, 3), (2, 4), (2, 5)])
        clq = [0, 1, 2]
        isolated = [3, 4, 5]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))
    
# 3. Mid-Sized Configurations
    def test_triangles_bridged_by_an_edge(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 3),   # Triangle 1
                          (4, 5), (4, 6), (5, 6),   # Triangle 2
                          (3, 4)])                  # Bridge edge
        self.assertFalse(is_split(G))

    def test_disconnected_triangles(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (1, 3), (2, 3),       # Triangle 1
                          (4, 5), (4, 6), (5, 6)])      # Triangle 2
        self.assertFalse(is_split(G))

    def test_multiple_isolated_nodes_only(self):
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3, 4, 5])
        clq = [0]
        isolated = [1, 2, 3, 4, 5]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_tree_sructure(self):
        G = nx.balanced_tree(r=2, h=2) # 7 Total Nodes
        self.assertFalse(is_split(G))

# 4. Larger Configurations
    def test_k10_graph(self):
        G = nx.complete_graph(10)
        clq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        isolated = []
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_k10_with_isolated_nodes(self):
        G = nx.complete_graph(10)
        G.add_nodes_from([10, 11, 12, 13, 14])
        clq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        isolated = [10, 11, 12, 13, 14]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_k10_with_tails(self):
        G = nx.complete_graph(10)
        G.add_edges_from([(2, 10), (4, 11), (6, 12), (8, 13)])
        clq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        isolated = [10, 11, 12, 13]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

    def test_k10_with_tails_and_two_connected_tail_nodes(self):
        G = nx.complete_graph(10)
        G.add_edges_from([(2, 10), (4, 11), (6, 12), (8, 13), (12, 13)])
        self.assertFalse(is_split(G))

    def test_s10_graph(self):
        G = nx.star_graph(10)
        clq = [0]
        isolated = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G))

# 5. Isolated Nodes with Non-Clique
    def test_non_k4_with_many_tails(self):
        G = nx.complete_graph(4)
        G.remove_edge(1, 2)
        G.add_edges_from([(0, 4)])
        clq = [0, 1, 3]
        isolated = [2, 4]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G)) # EX. [0, 1, 3] is a K3, [2, 4] is the independent set

    def test_non_k4_with_many_tails(self):
        G = nx.complete_graph(4)
        G.remove_edge(1, 2)
        G.add_edges_from([(0, 4), (1, 5), (2, 6), (3, 7)])
        self.assertFalse(is_split(G))

    def test_non_k4_with_isolated_nodes(self):
        G = nx.complete_graph(4)
        G.remove_edge(1, 2)
        G.add_nodes_from([4, 5, 6, 7])
        clq = [0, 1, 3]
        isolated = [2, 4, 5, 6, 7]
        self.assertIsClique(G, clq)
        self.assertIsIsolatedSet(G, isolated)
        self.assertTrue(is_split(G)) # EX. [0, 1, 3] is a K3, [2, 4, 5, 6, 7] is the independent set
        
    def test_non_k4_with_isolated_nodes_connected_to_many_non_clique_nodes(self):
        G = nx.complete_graph(4)
        G.remove_edge(1, 2)
        G.add_edges_from([(0, 4), (1, 5), (2, 4), (3, 5)])
        self.assertFalse(is_split(G))

# 6. Different Inputs
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
        G.add_edges_from([(a, b), (b, c), (c, a), (d, a)])
        self.assertTrue(is_split(G))

    def test_string_node_labels(self):
        """networkX Graph with strings as node labels"""
        G = nx.Graph()
        G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'A')])
        self.assertTrue(is_split(G))

    def test_invalid_input_types(self):
        G = nx.Graph()
        self.assertFalse(is_split(None))           
        self.assertFalse(is_split("hello")) 
        self.assertFalse(is_split(123))            
        self.assertFalse(is_split(Exception))        
        self.assertFalse(is_split({'a': 1}))           
        self.assertFalse(is_split([1, 1]))       
        self.assertFalse(is_split([1, 'A']))
        self.assertFalse(is_split(float("inf")))

if __name__ == '__main__':
    unittest.main()
