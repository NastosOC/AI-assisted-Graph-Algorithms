import networkx as nx
import unittest
import random
from datetime import datetime as dt
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import *
from functions.generate_qt_graph import *

# 15 Tests and 30 Asserts
class TestIsQuasiThreshold2(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.filename = f"generated_graphs_{dt.now().strftime('%Y-%m-%d')}.txt"
        with open(cls.filename, "w") as f:
            pass  # just clear the file

    def log_graph(self, G):
        g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
        with open(self.__class__.filename, "a") as f:
            f.write(f"{g6}\n")
    
    def toggle_edge(self, G, u, v):
        if not G.has_edge(u, v):
            G.add_edge(u, v)
        else:
            G.remove_edge(u, v)

    # Tests 100 graphs removing edge (4, 9)
    def test_100_remove_edge_4_9(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 4, 9)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (4, 9): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (21, 22)
    def test_100_remove_edge_21_22(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 21, 22)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (21, 22): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (30, 38)
    def test_100_remove_edge_30_38(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 30, 38)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (30, 38): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (24, 41)
    def test_100_remove_edge_24_41(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 24, 41)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (24, 41): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (44, 45)
    def test_100_remove_edge_44_45(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 44, 45)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (44, 45): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (49, 51)
    def test_100_remove_edge_49_51(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 49, 51)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (49, 51): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (11, 61)
    def test_100_remove_edge_11_61(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 11, 61)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (11, 61): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (66, 69)
    def test_100_remove_edge_66_69(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 66, 69)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (66, 69): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (35, 72)
    def test_100_remove_edge_35_72(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 35, 72)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (35, 72): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (74, 77)
    def test_100_remove_edge_74_77(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 74, 77)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (74, 77): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (80, 90)
    def test_100_remove_edge_80_90(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 80, 90)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (80, 90): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (84, 86)
    def test_100_remove_edge_84_86(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 84, 86)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (84, 86): TRUE: {true_count}, FALSE: {false_count}")

# Tests 100 graphs removing edge (14, 87)
    def test_100_remove_edge_14_87(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 14, 87)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (14, 87): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (24, 99)
    def test_100_remove_edge_24_99(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 24, 99)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (24, 99): TRUE: {true_count}, FALSE: {false_count}")

    # Tests 100 graphs removing edge (43, 71)
    def test_100_remove_edge_43_71(self):
        true_count = 0
        false_count = 0
        for i in range(100):
            G = generate_trivially_perfect_graph(100)
            self.log_graph(G)
            # Confirm the graph is Quasi Threshold
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            # Modify edge and re-assert
            self.toggle_edge(G, 43, 71)
            expected = is_quasi_threshold(G)
            actual = is_quasi_threshold_2(G)
            self.assertEqual(expected, actual)
            if actual:
                true_count += 1
            else:
                false_count += 1
        print(f"Test edge (43, 71): TRUE: {true_count}, FALSE: {false_count}")

if __name__ == '__main__':
    unittest.main()