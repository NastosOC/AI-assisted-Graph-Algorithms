import networkx as nx
import unittest
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *

# 14 Tests and 36 Asserts
class TestEdgeNicheCentrality(unittest.TestCase):

    def assertNonNegativeValues(self, values, msg=None):
        for v in values:
            self.assertGreaterEqual(v, 0, msg or f"Found negative value: {v}")

    def test_empty_graph(self):
        G = nx.Graph()

        enc = edge_niche_centrality(G)

        self.assertEqual(len(enc), 0)
        self.assertNonNegativeValues(enc.values())
        self.assertIsInstance(enc, dict)


    def test_single_node(self):
        G = nx.Graph()
        G.add_node(1)

        enc = edge_niche_centrality(G)

        self.assertEqual(len(enc), 0)
        self.assertNonNegativeValues(enc.values())
        self.assertIsInstance(enc, dict)

    def test_triangle_graph(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (1, 3)])  # Triangle

        enc = edge_niche_centrality(G)
        expected_value = (0 + 1)/(1 + 1)

        self.assertEqual(len(enc), 3)
        self.assertNonNegativeValues(enc.values())
        self.assertIsInstance(enc, dict)
        for edge in [(1, 2), (2, 3), (1, 3)]:
            self.assertAlmostEqual(enc[edge], expected_value, places = 5)
    
    def test_path_graph(self):
        G = nx.path_graph(4)  # 0-1-2-3

        enc = edge_niche_centrality(G)

        self.assertEqual(len(enc), 3)
        self.assertNonNegativeValues(enc.values())
        for edge in G.edges():
            p4 = 1 if edge == (1, 2) else 0
            deg_term = min(len(G[edge[0]]) - 1, len(G[edge[1]]) - 1)
            expected_value = (p4 + deg_term) / 1
            self.assertAlmostEqual(enc[edge], expected_value, places=5)

    def test_disconnected_edges(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (3, 4)])

        enc = edge_niche_centrality(G)

        self.assertEqual(set(enc.keys()), {(1, 2), (3, 4)})
        self.assertNonNegativeValues(enc.values())
        for score in enc.values():
            self.assertEqual(score, 0)

    def test_common_neighbors_triangle_count(self):
        # Square with diagonal: nodes 1-2-3-1 form triangle, 3-4 is extra
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (1, 3), (3, 4)])
        enc = edge_niche_centrality(G)

        self.assertNonNegativeValues(enc.values())
        for edge in [(1, 2), (2, 3), (1, 3)]:
            self.assertIn(edge, enc)
            self.assertGreater(enc[edge], 0)

    def test_star_graph(self):
        G = nx.star_graph(4) # Node 0 is the central node

        enc = edge_niche_centrality(G)

        self.assertEqual(len(enc), 4)
        self.assertNonNegativeValues(enc.values())
        for value in enc.values():
            self.assertEqual(value, 0)

    def test_cycle_graph(self):
        G = nx.cycle_graph(5)

        enc = edge_niche_centrality(G)
        expected_value = (1 + 1)/(0 + 1)

        self.assertEqual(len(enc), 5)
        self.assertNonNegativeValues(enc.values())
        for edge in G.edges():
            self.assertAlmostEqual(enc[edge], expected_value, places = 5)

    def test_complete_graph(self):
        G = nx.complete_graph(4) 
        
        enc = edge_niche_centrality(G)

        self.assertEqual(len(enc), 6) # 4 choose 2
        self.assertNonNegativeValues(enc.values())
        for score in enc.values():
            self.assertLess(score, 1)  # Very embedded edges

    def test_non_integer_labels(self):
        G = nx.Graph()
        G.add_edges_from([('A', 'B'), ('B', 'C'), ('B', 'D'), 
                          ('A', 'D'), ('D', 'E')])
        
        enc = edge_niche_centrality(G)
        
        self.assertEqual(len(enc), 5)
        self.assertNonNegativeValues(enc.values())
        self.assertIn(('B', 'D'), enc)
        for u, v in G.edges():
            neighbors_u = set(G[u]) - {v}
            neighbors_v = set(G[v]) - {u}
            
            p4_count = sum(1 for x in neighbors_u for y in neighbors_v if x != y and not G.has_edge(x, y))
            deg_term = min(len(G[u]) - 1, len(G[v]) - 1)
            triangles = len(set(G[u]) & set(G[v]))
            
            expected_value = (p4_count + deg_term) / (triangles + 1)
            enc_val = enc.get((u, v) if u < v else (v, u))
        
            self.assertAlmostEqual(enc_val, expected_value, places=5)

    def test_non_graph_input(self):
        with self.assertRaises(TypeError):
            edge_niche_centrality("not a graph")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            edge_niche_centrality(None)
    
    def test_directed_graph_input(self):
        G = nx.DiGraph()
        G.add_edges_from([(1, 2), (2, 3)])

        enc = edge_niche_centrality(G)

        self.assertIsInstance(enc, dict)

    def test_edge_order_consistency(self):
        G = nx.Graph()
        G.add_edges_from([(1, 2), (2, 3), (3, 1)])

        enc = edge_niche_centrality(G)

        for u, v in G.edges():
            self.assertIn((min(u, v), max(u, v)), enc)
        
if __name__ == '__main__':
    unittest.main()