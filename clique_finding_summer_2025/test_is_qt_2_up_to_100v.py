import networkx as nx
import unittest
from datetime import datetime as dt
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import *
from functions.generate_qt_graph import *

# 57 Tests and 171 Asserts
class TestIsQuasiThreshold2(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.filename = f"generated_graphs_{dt.now().strftime('%Y-%m-%d')}.txt"
        with open(cls.filename, "w") as f:
            pass  # just clear the file

    def generate_and_log_graph(self, size):
        G = generate_trivially_perfect_graph(size)
        g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
        with open(self.__class__.filename, "a") as f:
            f.write(f"{g6}\n")
        return G
    
    def toggle_edge(self, G, u, v):
        if not G.has_edge(u, v):
            G.add_edge(u, v)
        else:
            G.remove_edge(u, v)

    def induce_p4(self, G, v):
        G.add_edges_from([(v[0], v[1]), (v[1], v[2]), (v[2], v[3])])
        G.remove_edges_from([(v[0], v[2]), (v[0], v[3]), (v[1], v[3])])

    def induce_c4(self, G, v):
        G.add_edges_from([(v[0], v[1]), (v[1], v[2]), (v[2], v[3]), (v[3], v[0])])
        G.remove_edges_from([(v[0], v[2]), (v[1], v[3])])

    def test_10_node_edge_modification(self):
        G = self.generate_and_log_graph(10)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 1, 4)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_10_node_induce_p4(self):
        G = self.generate_and_log_graph(10)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [2, 3, 4, 5])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_10_node_induce_c4(self):
        G = self.generate_and_log_graph(10)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [2, 4, 6, 9])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_15_node_edge_modification(self):
        G = self.generate_and_log_graph(15)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 5, 9)
        self.toggle_edge(G, 8, 13)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_15_node_induce_p4(self):
        G = self.generate_and_log_graph(15)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [4, 9, 13, 14])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_15_node_induce_c4(self):
        G = self.generate_and_log_graph(15)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [2, 9, 11, 14])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_20_node_edge_modification(self):
        G = self.generate_and_log_graph(20)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 2, 9)
        self.toggle_edge(G, 8, 10)
        self.toggle_edge(G, 14, 19)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_20_node_induce_p4(self):
        G = self.generate_and_log_graph(20)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [3, 9, 14, 18])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_20_node_induce_c4(self):
        G = self.generate_and_log_graph(20)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [7, 9, 11, 18])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_25_node_edge_modification(self):
        G = self.generate_and_log_graph(25)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 21, 9)
        self.toggle_edge(G, 17, 22)
        self.toggle_edge(G, 4, 14)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_25_node_induce_p4(self):
        G = self.generate_and_log_graph(25)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [8, 12, 16, 20])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_25_node_induce_c4(self):
        G = self.generate_and_log_graph(25)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [3, 11, 18, 23])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_30_node_edge_modification(self):
        G = self.generate_and_log_graph(30)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 3, 4)
        self.toggle_edge(G, 7, 9)
        self.toggle_edge(G, 5, 1)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_30_node_induce_p4(self):
        G = self.generate_and_log_graph(30)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [3, 8, 23, 24])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_30_node_induce_c4(self):
        G = self.generate_and_log_graph(30)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [24, 25, 26, 28])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_35_node_edge_modification(self):
        G = self.generate_and_log_graph(35)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 5, 24)
        self.toggle_edge(G, 11, 13)
        self.toggle_edge(G, 22, 27)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_35_node_induce_p4(self):
        G = self.generate_and_log_graph(35)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [1, 13, 24, 30])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_35_node_induce_c4(self):
        G = self.generate_and_log_graph(35)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [14, 15, 22, 31])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_40_node_edge_modification(self):
        G = self.generate_and_log_graph(40)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 2, 34)
        self.toggle_edge(G, 14, 38)
        self.toggle_edge(G, 3, 23)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_40_node_induce_p4(self):
        G = self.generate_and_log_graph(40)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [4, 14, 34, 39])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_40_node_induce_c4(self):
        G = self.generate_and_log_graph(40)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [6, 12, 24, 36])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_45_node_edge_modification(self):
        G = self.generate_and_log_graph(45)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 11, 44)
        self.toggle_edge(G, 9, 22)
        self.toggle_edge(G, 27, 34)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_45_node_induce_p4(self):
        G = self.generate_and_log_graph(45)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [4, 9, 35, 44])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_45_node_induce_c4(self):
        G = self.generate_and_log_graph(45)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [14, 33, 34, 44])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_50_node_edge_modification(self):
        G = self.generate_and_log_graph(50)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 2, 13)
        self.toggle_edge(G, 14, 27)
        self.toggle_edge(G, 30, 39)
        self.toggle_edge(G, 44, 46)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_50_node_induce_p4(self):
        G = self.generate_and_log_graph(50)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [3, 7, 36, 39])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_50_node_induce_c4(self):
        G = self.generate_and_log_graph(50)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [11, 22, 33, 44])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_55_node_edge_modification(self):
        G = self.generate_and_log_graph(55)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 13, 51)
        self.toggle_edge(G, 19, 33)
        self.toggle_edge(G, 9, 35)
        self.toggle_edge(G, 44, 45)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_55_node_induce_p4(self):
        G = self.generate_and_log_graph(55)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [24, 35, 46, 50])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_55_node_induce_c4(self):
        G = self.generate_and_log_graph(55)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [13, 24, 35, 46])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_60_node_edge_modification(self):
        G = self.generate_and_log_graph(60)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 45, 59)
        self.toggle_edge(G, 38, 49)
        self.toggle_edge(G, 11, 1)
        self.toggle_edge(G, 7, 54)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_60_node_induce_p4(self):
        G = self.generate_and_log_graph(60)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [6, 34, 7, 57])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_60_node_induce_c4(self):
        G = self.generate_and_log_graph(60)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [32, 42, 48, 57])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_65_node_edge_modification(self):
        G = self.generate_and_log_graph(65)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 53, 24)
        self.toggle_edge(G, 1, 34)
        self.toggle_edge(G, 2, 60)
        self.toggle_edge(G, 44, 64)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_65_node_induce_p4(self):
        G = self.generate_and_log_graph(65)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [4, 35, 49, 61])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_65_node_induce_c4(self):
        G = self.generate_and_log_graph(65)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [22, 35, 59, 64])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_70_node_edge_modification(self):
        G = self.generate_and_log_graph(70)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 4, 54)
        self.toggle_edge(G, 19, 68)
        self.toggle_edge(G, 34, 44)
        self.toggle_edge(G, 8, 67)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_70_node_induce_p4(self):
        G = self.generate_and_log_graph(70)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [5, 36, 48, 69])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_70_node_induce_c4(self):
        G = self.generate_and_log_graph(70)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [61, 62, 66, 67])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_75_node_edge_modification(self):
        G = self.generate_and_log_graph(75)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 55, 4)
        self.toggle_edge(G, 12, 29)
        self.toggle_edge(G, 57, 39)
        self.toggle_edge(G, 6, 8)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_75_node_induce_p4(self):
        G = self.generate_and_log_graph(75)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [3, 46, 68, 71])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_75_node_induce_c4(self):
        G = self.generate_and_log_graph(75)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [71, 72, 73, 74])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_80_node_edge_modification(self):
        G = self.generate_and_log_graph(80)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 54, 51)
        self.toggle_edge(G, 79, 73)
        self.toggle_edge(G, 34, 35)
        self.toggle_edge(G, 44, 65)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_80_node_induce_p4(self):
        G = self.generate_and_log_graph(80)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [47, 67, 37, 78])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_80_node_induce_c4(self):
        G = self.generate_and_log_graph(80)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [66, 77, 22, 48])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_85_node_edge_modification(self):
        G = self.generate_and_log_graph(85)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 5, 76)
        self.toggle_edge(G, 34, 50)
        self.toggle_edge(G, 8, 45)
        self.toggle_edge(G, 17, 18)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_85_node_induce_p4(self):
        G = self.generate_and_log_graph(85)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [45, 56, 67, 83])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_85_node_induce_c4(self):
        G = self.generate_and_log_graph(85)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [78, 79, 80, 81])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_90_node_edge_modification(self):
        G = self.generate_and_log_graph(90)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 5, 84)
        self.toggle_edge(G, 18, 80)
        self.toggle_edge(G, 38, 69)
        self.toggle_edge(G, 57, 82)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_90_node_induce_p4(self):
        G = self.generate_and_log_graph(90)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [4, 78, 88, 89])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_90_node_induce_c4(self):
        G = self.generate_and_log_graph(90)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [30, 40, 70, 80])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_95_node_edge_modification(self):
        G = self.generate_and_log_graph(95)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 91, 92)
        self.toggle_edge(G, 1, 79)
        self.toggle_edge(G, 31, 59)
        self.toggle_edge(G, 81, 89)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_95_node_induce_p4(self):
        G = self.generate_and_log_graph(95)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [89, 90, 91, 92])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_95_node_induce_c4(self):
        G = self.generate_and_log_graph(95)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [40, 44, 90, 94])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_100_node_edge_modification(self):
        G = self.generate_and_log_graph(100)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Modify edge and re-assert
        self.toggle_edge(G, 91, 99)
        self.toggle_edge(G, 1, 95)
        self.toggle_edge(G, 3, 5)
        self.toggle_edge(G, 65, 87)
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        
    def test_100_node_induce_p4(self):
        G = self.generate_and_log_graph(100)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a P4 and re-assert
        self.induce_p4(G, [67, 87, 97, 99])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

    def test_100_node_induce_c4(self):
        G = self.generate_and_log_graph(100)
        # Confirm the graph is Quasi Threshold
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)
        self.assertTrue(actual)
        # Induce a C4 and re-assert
        self.induce_c4(G, [24, 49, 74, 99])
        expected = is_quasi_threshold(G)
        actual = is_quasi_threshold_2(G)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()