import networkx as nx
import unittest
from functions.check_functions import is_clique

# 30 Tests and 66 Asserts
class TestIsClique(unittest.TestCase):
    """
    Testing is_clique(nx.Graph, node_list) check function on various edge cases.
    Asserts for each case are either:
        Confirming provided nodes make a valid Clique
        Confirming provided nodes do not make a valid Clique
    """
# 1. Basic Structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        self.assertTrue(is_clique(G, []))

    def test_single_node(self):
        """networkX Graph with 1 node and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        self.assertTrue(is_clique(G, [0]))

    def test_two_connected_nodes(self):
        """networkX Graph with 2 nodes and 1 edge"""
        G = nx.Graph()
        G.add_edge(0, 1)
        self.assertTrue(is_clique(G, [0, 1]))

    def test_two_disconnected_nodes(self):
        """networkX Graph with 2 nodes and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        G.add_node(1)
        self.assertFalse(is_clique(G, [0, 1]))

    def test_triangle_graph(self):
        """networkX Graph with 3 nodes and 3 edges"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        self.assertTrue(is_clique(G, [0, 1, 2]))

    def test_k4_graph(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        self.assertTrue(is_clique(G, [0, 1, 2, 3]))  

    def test_k5_graph(self):
        """networkX 5-node complete graph"""
        G = nx.complete_graph(5)
        self.assertTrue(is_clique(G, [0, 1, 2, 3, 4]))  

    def test_p4_graph(self):
        """networkX 4-node path graph"""
        G = nx.path_graph(4)
        self.assertFalse(is_clique(G, [0, 1, 2, 3])) 
        self.assertTrue(is_clique(G, [1, 2])) # Largest clique possible in a path graph is 2

    def test_c4_graph(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertFalse(is_clique(G, [0, 1, 2, 3])) 
        self.assertTrue(is_clique(G, [1, 2])) # Largest clique possible in a cycle graph is 2

    def test_s4_graph(self):
        """networkX 4-node star graph"""
        G = nx.star_graph(4)
        self.assertFalse(is_clique(G, [0, 1, 2, 3]))
        self.assertTrue(is_clique(G, [0, 1])) # Largest clique possible in a star graph is 2

    def test_house_graph(self):
        """networkX Graph with 5 nodes and 6 edges - house layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 2), 
                          (2, 3), (3, 4), (4, 0)])
        self.assertTrue(is_clique(G, [0, 1, 2])) # Triangle a the top is a clique
        self.assertFalse(is_clique(G, [0, 2, 3, 4])) # Bottom of the house is a C4

    def test_4_node_bipartite_graph(self):
        """networkX 4-node bipartite graph"""
        G = nx.complete_bipartite_graph(2, 2)
        self.assertTrue(is_clique(G, [0, 2]))   

    def test_domino_graph(self):
        """networkX Graph with 6 nodes and 7 edges - domino layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), 
                          (2, 4), (3, 5), (4, 5)])
        self.assertTrue(is_clique(G, [0, 1])) # Largest clique possible in a domino graph is 2
        self.assertFalse(is_clique(G, [0, 1, 2, 3])) # Fails -> C4
        self.assertFalse(is_clique(G, [0, 1, 3, 5])) # Fails -> P4

# 2. Non-Clique/Broken Clique Structures
    def test_k4_missing_edge(self):
        """networkX 4-node complete graph missing edge (1, 2)"""
        G = nx.complete_graph(4) 
        G.remove_edge(1, 2) # Missing (1, 2)
        self.assertFalse(is_clique(G, [0, 1, 2, 3])) # Should fail

    def test_k5_missing_edge(self):
        """networkX 5-node complete graph missing edge (1, 2)"""
        G = nx.complete_graph(5) 
        G.remove_edge(1, 2) # Missing (1, 2)
        self.assertFalse(is_clique(G, [0, 1, 2, 3, 4])) # Should fail

    def test_k6_missing_edge(self):
        """networkX 6-node complete graph missing edge (1, 2)"""
        G = nx.complete_graph(6) 
        G.remove_edge(1, 2) # Missing (1, 2)
        self.assertFalse(is_clique(G, [0, 1, 2, 3, 4, 5])) # Should fail

# 3. Test All Sub-Cliques Return Valid
    def test_all_single_node_cliques(self):
        """networkX 4-node complete graph missing edge (1, 2)"""
        G = nx.complete_graph(4) 
        self.assertTrue(is_clique(G, [0]))
        self.assertTrue(is_clique(G, [1]))
        self.assertTrue(is_clique(G, [2]))
        self.assertTrue(is_clique(G, [3]))

    def test_all_2_node_cliques(self):
        """networkX 4-node complete graph missing edge (1, 2)"""
        G = nx.complete_graph(4) 
        self.assertTrue(is_clique(G, [0, 1]))
        self.assertTrue(is_clique(G, [0, 2]))
        self.assertTrue(is_clique(G, [0, 3]))
        self.assertTrue(is_clique(G, [1, 2]))
        self.assertTrue(is_clique(G, [1, 3]))
        self.assertTrue(is_clique(G, [2, 3]))

    def test_all_3_node_cliques(self):
        """networkX 4-node complete graph missing edge (1, 2)"""
        G = nx.complete_graph(4) 
        self.assertTrue(is_clique(G, [0, 1, 2]))
        self.assertTrue(is_clique(G, [0, 1, 3]))
        self.assertTrue(is_clique(G, [0, 2, 3]))
        self.assertTrue(is_clique(G, [1, 2, 3]))

# 4. Graphs With Added Noise
    def test_partial_cliques(self):
        """networkX Graph with 7 nodes and 7 edges"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 6),
                          (1, 4), (1, 5), (2, 5),
                          (5, 6)])
        self.assertTrue(is_clique(G, [1, 2, 5]))
        self.assertTrue(is_clique(G, [5, 6]))

    def test_k4_added_tails(self):
        """networkX 4-node complete graph with each node connected to a non-clique node"""
        G = nx.complete_graph(4)
        G.add_edges_from([(0, 4), (1, 5), (2, 6), (3, 7)])
        self.assertTrue(is_clique(G, [0, 1, 2, 3]))
        self.assertFalse(is_clique(G, [0, 1, 2, 3, 4, 5, 6, 7]))

    def test_k4_added_noise(self):
        """networkX 4-node complete graph with extra edges added"""
        G = nx.complete_graph(4)
        G.add_edges_from([(3, 4), (4, 5), (2, 5),
                          (1, 6), (1, 7), (3, 7)])
        self.assertTrue(is_clique(G, [0, 1, 2, 3]))
        self.assertFalse(is_clique(G, [0, 1, 2, 3, 4, 5, 6, 7]))

    def test_k5_added_noise(self):
        """networkX 5-node complete graph with extra edges added"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 3), (0, 6), (0, 7),
                          (1, 2), (1, 3), (1, 6), (1, 7),
                          (2, 4), (2, 6), (2, 7),
                          (3, 4), (3, 6), (3, 7),
                          (4, 5),
                          (5, 6),
                          (6, 7)])
        self.assertTrue(is_clique(G, [0, 1, 3, 6, 7]))
        self.assertFalse(is_clique(G, [0, 1, 2, 3, 4, 5, 6, 7]))

# 5. Large Graph Configurations
    def test_large_complete_graph(self):
        G = nx.complete_graph(100)
        clq_1 = list(range(10)) # Nodes 0-9
        clq_2 = list(range(25)) # Nodes 0-24
        clq_3 = list(range(50)) # Nodes 0-49
        clq_4 = list(range(100)) # Nodes 0-99
        clq_5 = list(range(60, 80)) # Nodes 60-79
        clq_6 = list(range(30, 45)) # Nodes 30-44
        self.assertTrue(is_clique(G, clq_1))
        self.assertTrue(is_clique(G, clq_2))
        self.assertTrue(is_clique(G, clq_3))
        self.assertTrue(is_clique(G, clq_4))
        self.assertTrue(is_clique(G, clq_5))
        self.assertTrue(is_clique(G, clq_6))

    def test_large_graph_missing_edges(self):
        G = nx.complete_graph(100)
        G.remove_edges_from([(1, 2), (2, 50), (29, 44), (50, 51), 
                             (50, 56), (70, 75), (70, 90), (80, 99)])
        clq_1 = list(range(10)) # Nodes 0-9
        clq_2 = list(range(25, 35)) # Nodes 25-34
        clq_3 = list(range(25, 50)) # Nodes 25-49
        clq_4 = list(range(90, 100)) # Nodes 90-99
        clq_5 = list(range(60, 80)) # Nodes 60-79
        clq_6 = list(range(30, 45)) # Nodes 30-44
        self.assertFalse(is_clique(G, clq_1)) # Removed edge (1, 2)
        self.assertTrue(is_clique(G, clq_2)) # All edges still intact
        self.assertFalse(is_clique(G, clq_3)) # Removed edge (29, 44)
        self.assertTrue(is_clique(G, clq_4)) # All edges still intact
        self.assertFalse(is_clique(G, clq_5)) # Removed edge (70, 75)
        self.assertTrue(is_clique(G, clq_6)) # All edges still intact

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
        a, b, c = CustomNode('a'), CustomNode('b'), CustomNode('c')

        G = nx.Graph()
        G.add_edges_from([(a, b), (b, c), (c, a)])
        self.assertTrue(is_clique(G, [a, b, c]))

    def test_string_node_labels(self):
        """networkX Graph with strings as node labels"""
        G = nx.Graph()
        G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])
        self.assertTrue(is_clique(G, ['A', 'B', 'C']))

    def test_nodes_not_in_G(self):
        G = nx.complete_graph(4)
        self.assertFalse(is_clique(G, [5, 6, 7, 8]))

    def test_duplicate_nodes(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 1)])
        self.assertFalse(is_clique(G, [1, 2, 3, 1]))

    def test_invalid_input_types(self):
        G = nx.Graph()
        G.add_nodes_from([1, 2, 3])
        G.add_edges_from([(1, 2), (2, 3), (1, 3)])
        self.assertFalse(is_clique(G, None))           
        self.assertFalse(is_clique(G, 5))             
        self.assertFalse(is_clique(G, {1: 2}))        
        self.assertFalse(is_clique(G, [1, 1]))           
        self.assertFalse(is_clique(G, [[1], [2]]))       
        self.assertFalse(is_clique(G, [1, None]))  

if __name__ == '__main__':
    unittest.main()