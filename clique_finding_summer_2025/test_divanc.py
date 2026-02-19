import networkx as nx
import unittest
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *

# 15 Tests and 27 Asserts
class TestDivanc(unittest.TestCase):

    def test_empty_graph(self):
        G = nx.Graph()

        result = divanc(G)

        self.assertEqual(len(result), 0)

    def test_single_node(self):
        G = nx.Graph()
        G.add_node(1)

        result = divanc(G)

        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), 1)
        self.assertTrue(result[0].has_node(1))

    def test_no_removal_needed(self):
        G = nx.star_graph(3) 

        result = divanc(G)

        self.assertEqual(len(result), 1)
        # The original graph should be unchanged
        self.assertEqual(len(result[0].edges()), len(G.edges()))
        self.assertLessEqual(nx.diameter(result[0]), 2)

    def test_large_hub_and_spoke(self):
        G = nx.star_graph(10)  # Center node 0 connected to 1..10

        result = divanc(G)
        
        self.assertEqual(len(result), 1)
        self.assertLessEqual(nx.diameter(result[0]), 2)

    def test_removal_occurs(self):
        # Path graph of length 4 has diameter 3
        G = nx.path_graph(4) 
        
        result = divanc(G)

        # Result should have split into subgraphs with diameter ≤ 2
        for subgraph in result:
            self.assertLessEqual(nx.diameter(subgraph), 2)
        # The number of components should be more than 1
        self.assertGreater(len(result), 1)

    def test_multiple_components(self):
        # Two disconnected paths of length 4
        G = nx.path_graph(4)
        H = nx.path_graph(4)
        H = nx.relabel_nodes(H, lambda x: x + 10)
        G = nx.compose(G, H)

        result = divanc(G)

        # There should be at least two components after divanc
        self.assertGreaterEqual(len(result), 2)
        for subgraph in result:
            self.assertLessEqual(nx.diameter(subgraph), 2)

    def test_complete_graph(self):
        G = nx.complete_graph(5)

        result = divanc(G)
        
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0].nodes()), 5)
        self.assertLessEqual(nx.diameter(result[0]), 2)

    def test_isolated_nodes(self):
        G = nx.Graph()
        G.add_nodes_from(range(5))  # 5 isolated nodes

        result = divanc(G)
        
        self.assertEqual(len(result), 5)
        for subgraph in result:
            self.assertEqual(len(subgraph.nodes()), 1)
            self.assertEqual(len(subgraph.edges()), 0)

    def test_cycle_graph(self):
        G = nx.cycle_graph(6)  # Diameter = 3

        result = divanc(G)

        self.assertGreater(len(result), 1)
        for subgraph in result:
            self.assertLessEqual(nx.diameter(subgraph), 2)

    def test_graph_with_bridges(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), 
                          (5, 6), (3, 7), (7, 8)])
        
        result = divanc(G)
        
        for subgraph in result:
            self.assertLessEqual(nx.diameter(subgraph), 2)

    def test_non_graph_input(self):
        with self.assertRaises(AttributeError):  # Because G.copy() will fail
            divanc("not a graph")

    def test_none_input(self):
        with self.assertRaises(AttributeError):
            divanc(None)

    def test_directed_graph_input(self):
        G = nx.DiGraph()
        G.add_edges_from([(1, 2), (2, 3)])
        with self.assertRaises(nx.NetworkXNotImplemented):
            divanc(G)

    def test_all_nodes_preserved(self):
        G = nx.path_graph(6)
        result = divanc(G)

        original_nodes = set(G.nodes())
        result_nodes = set()
        for subgraph in result:
            result_nodes.update(subgraph.nodes())

        self.assertEqual(original_nodes, result_nodes)

    def test_disjoint_output(self):
        G = nx.path_graph(6)
        result = divanc(G)

        seen = set()
        for sg in result:
            for node in sg.nodes():
                self.assertNotIn(node, seen)
                seen.add(node)
  
if __name__ == '__main__':
    unittest.main()