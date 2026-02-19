import networkx as nx
import unittest
from functions.check_functions import *

# 32 Tests and 90 Asserts
class TestIsC4(unittest.TestCase):
    """
    Testing is_c4(nx.Graph, node_list) check function on various edge cases.
    Asserts for each case are either:
        Confirming provided nodes make a valid C4
        Confirming provided nodes do not make a valid C4
    """
# 1. Basic Structures
    def test_empty_graph(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        self.assertFalse(is_c4(G, []))

    def test_single_node(self):
        """networkX Graph with 1 node and 0 edges"""
        G = nx.Graph()
        G.add_node(0)
        self.assertFalse(is_c4(G, [0]))

    def test_two_connected_nodes(self):
        """networkX Graph with 2 nodes and 1 edge"""
        G = nx.Graph()
        G.add_edge(0, 1)
        self.assertFalse(is_c4(G, [0, 1]))

    def test_k4_graph(self):
        """networkX 4-node complete graph"""
        G = nx.complete_graph(4)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_p4_graph(self):
        """networkX 4-node path graph"""
        G = nx.path_graph(4)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_c4_graph(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertTrue(is_c4(G, [0, 1, 2, 3]))

    def test_c5_graph(self):
        """networkX 5-node cycle graph"""
        G = nx.cycle_graph(5)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))
        self.assertFalse(is_c4(G, [0, 1, 2, 4]))
        self.assertFalse(is_c4(G, [0, 1, 3, 4]))
        self.assertFalse(is_c4(G, [0, 2, 3, 4]))
        self.assertFalse(is_c4(G, [1, 2, 3, 4]))

    def test_s4_graph(self):
        """networkX 4-node star graph"""
        G = nx.star_graph(4)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_house_graph(self):
        """networkX Graph with 5 nodes and 6 edges - house layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 2), 
                          (2, 3), (3, 4), (4, 0)])
        self.assertTrue(is_c4(G, [0, 2, 3, 4]))
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_4_node_bipartite_graph(self):
        """networkX 4-node bipartite graph"""
        G = nx.complete_bipartite_graph(2, 2)
        self.assertTrue(is_c4(G, [0, 1, 2, 3]))

    def test_domino_graph(self):
        """networkX Graph with 6 nodes and 7 edges - domino layout"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), 
                          (2, 4), (3, 5), (4, 5)])
        self.assertTrue(is_c4(G, [0, 1, 2, 3]))
        self.assertTrue(is_c4(G, [2, 3, 4, 5]))
        self.assertFalse(is_c4(G, [0, 1, 3, 5]))
        self.assertFalse(is_c4(G, [0, 2, 3, 5]))
        self.assertFalse(is_c4(G, [0, 2, 4, 5]))
        self.assertFalse(is_c4(G, [1, 0, 2, 4]))
        self.assertFalse(is_c4(G, [1, 3, 2, 4]))
        self.assertFalse(is_c4(G, [1, 3, 5, 4]))

# 2. Kn Graphs with Edge (1, 2) Missing
    def test_k4_missing_edge(self):
        """networkX 4-node complete graph with edge (1, 2) removed"""
        G = nx.complete_graph(4)
        G.remove_edge(1, 2)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_k5_missing_edge(self):
        """networkX 5-node complete graph with edge (1, 2) removed"""
        G = nx.complete_graph(5)
        G.remove_edge(1, 2)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))
        self.assertFalse(is_c4(G, [0, 1, 2, 4]))
        self.assertFalse(is_c4(G, [0, 1, 3, 4]))
        self.assertFalse(is_c4(G, [0, 2, 3, 4]))
        self.assertFalse(is_c4(G, [1, 2, 3, 4]))

    def test_k6_missing_edge(self):
        """networkX 6-node complete graph with edge (1, 2) removed"""
        G = nx.complete_graph(6)
        G.remove_edge(1, 2)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))
        self.assertFalse(is_c4(G, [0, 1, 2, 4]))
        self.assertFalse(is_c4(G, [0, 1, 2, 5]))
        self.assertFalse(is_c4(G, [0, 1, 3, 4]))
        self.assertFalse(is_c4(G, [0, 1, 3, 5]))
        self.assertFalse(is_c4(G, [0, 1, 4, 5]))
        self.assertFalse(is_c4(G, [0, 2, 3, 4]))
        self.assertFalse(is_c4(G, [0, 2, 3, 5]))
        self.assertFalse(is_c4(G, [0, 2, 4, 5]))
        self.assertFalse(is_c4(G, [0, 3, 4, 5]))
        self.assertFalse(is_c4(G, [1, 2, 3, 4]))
        self.assertFalse(is_c4(G, [1, 2, 3, 5]))
        self.assertFalse(is_c4(G, [1, 2, 4, 5]))
        self.assertFalse(is_c4(G, [2, 3, 4, 5]))

# 3. Four Node Configurations
    def test_isolated_nodes(self):
        """networkX Graph with 4 nodes and 0 edges"""
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3])
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_4_nodes_2_edges(self):
        """networkX Graph with 4 nodes and 2 edges - 2 disjoint 2-cliques"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (2, 3)])
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_triangle_with_tail(self):
        """networkX Graph with 4 nodes and 4 edges - triangle with a tail"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_triangle_with_isolated_node(self):
        """networkX Graph with 4 nodes and 3 edges - triangle with a disconnected node"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 0)])
        G.add_node(3)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_c4_with_chord(self):
        """networkX 4-node cycle graph with an added chord from (0, 2)"""
        G = nx.cycle_graph(4)
        G.add_edge(0, 2)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))

    def test_c4_all_node_permutations(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertTrue(is_c4(G, [0, 1, 2, 3]))
        self.assertTrue(is_c4(G, [1, 2, 3, 0]))
        self.assertTrue(is_c4(G, [2, 3, 0, 1]))
        self.assertTrue(is_c4(G, [3, 0, 1, 2]))

        self.assertTrue(is_c4(G, [0, 3, 2, 1]))
        self.assertTrue(is_c4(G, [3, 2, 1, 0]))
        self.assertTrue(is_c4(G, [2, 1, 0, 3]))
        self.assertTrue(is_c4(G, [1, 0, 3, 2]))

    def test_c4_with_chord_all_node_permutations(self):
        """networkX 4-node cycle graph with an added chord from (0, 2)"""
        G = nx.cycle_graph(4)
        G.add_edge(0, 2)
        self.assertFalse(is_c4(G, [0, 1, 2, 3]))
        self.assertFalse(is_c4(G, [1, 2, 3, 0]))
        self.assertFalse(is_c4(G, [2, 3, 0, 1]))
        self.assertFalse(is_c4(G, [3, 0, 1, 2]))

        self.assertFalse(is_c4(G, [0, 3, 2, 1]))
        self.assertFalse(is_c4(G, [3, 2, 1, 0]))
        self.assertFalse(is_c4(G, [2, 1, 0, 3]))
        self.assertFalse(is_c4(G, [1, 0, 3, 2]))

# 4. Complex Configurations
    def test_graph_with_multiple_cycles(self):
        """networkX Graph with a Triangle connected to a C4"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), 
                          (4, 5), (5, 6), (6, 7), (7, 5)]) 
        self.assertTrue(is_c4(G, [1, 2, 3, 4]))  
        self.assertFalse(is_c4(G, [4, 5, 6, 7])) # Fails because [5, 6, 7] is a triangle

    def test_extra_node_does_not_invalidate(self):
        """networkX 4-node cycle Graph with an extra node connected to all nodes in the C4"""
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
        G.add_node(5)
        G.add_edges_from([(5, 1), (5, 2), (5, 3), (5, 4)])
        self.assertTrue(is_c4(G, [1, 2, 3, 4]))

    def test_layered_c4_only_one_valid(self):
        """
        networkX Graph with 1 valid C4, and 1 invalid C4 due to chord.
        Chord edge (0, 3) is shared in both candidate C4s
        """
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 3), (0, 4), (0, 5), 
                          (1, 2), (2, 3), (3, 4), (3, 5)])
        self.assertTrue(is_c4(G, [0, 1, 2, 3]))
        self.assertFalse(is_c4(G, [0, 4, 3, 5])) # Fails because of edge (0, 3)

    def test_large_graph_with_1_c4(self):
        """networkX Graph with 10 nodes and only 1 valid C4"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (0, 4), (0, 8), (0, 9),
                          (2, 3), (3, 4), (4, 5), (5, 2),
                          (1, 6), (1, 9), (6, 9), (7, 8)])
        self.assertTrue(is_c4(G, [2, 3, 4, 5]))
        self.assertFalse(is_c4(G, [0, 1, 2, 3])) # Fails because no edge (1, 2)
        self.assertFalse(is_c4(G, [0, 1, 6, 9])) # Fails because of edge (1, 9)

    def test_two_c4_node_pairs(self):
        """networkX Graph with 2 C4s, each node in subgraph_1 maps to one node in subgraph_2"""
        G = nx.Graph()
        G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0),
                          (4, 5), (5, 6), (6, 7), (7, 4),
                          (0, 4), (1, 5), (2, 6), (3, 7)])
        self.assertTrue(is_c4(G, [0, 1, 2, 3]))
        self.assertTrue(is_c4(G, [4, 5, 6, 7]))
        self.assertTrue(is_c4(G, [0, 1, 4, 5]))

# 5. Different Inputs
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
        self.assertTrue(is_c4(G, [a, b, c, d]))

    def test_string_node_labels(self):
        """networkX Graph with strings as node labels"""
        G = nx.Graph()
        G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])
        self.assertTrue(is_c4(G, ['A', 'B', 'C', 'D']))

    def test_nodes_not_in_G(self):
        """networkX Graph with 5 nodes and 0 edges"""
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3, 4])
        self.assertFalse(is_c4(G, [5, 6, 7, 8]))

    def test_too_few_nodes(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertFalse(is_c4(G, [0]))
        self.assertFalse(is_c4(G, [0, 1]))
        self.assertFalse(is_c4(G, [0, 1, 2]))

    def test_invalid_input_types(self):
        """Empty networkX Graph"""
        G = nx.Graph()
        self.assertFalse(is_c4(G, None))           
        self.assertFalse(is_c4(G, "hello")) 
        self.assertFalse(is_c4(G, 123))            
        self.assertFalse(is_c4(G, Exception))        
        self.assertFalse(is_c4(G, {'a': 1}))           
        self.assertFalse(is_c4(G, [1, 1]))       
        self.assertFalse(is_c4(G, [1, 'A']))
        self.assertFalse(is_c4(G, float("inf")))

    def test_duplicate_node_input(self):
        """networkX 4-node cycle graph"""
        G = nx.cycle_graph(4)
        self.assertFalse(is_c4(G, [0, 1, 1, 2]))

if __name__ == '__main__':
    unittest.main()