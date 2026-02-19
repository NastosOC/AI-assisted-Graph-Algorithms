import networkx as nx
import unittest
import random
from datetime import datetime as dt
from functions.clique_algorithms import *
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import *
from functions.generate_qt_graph import *

# 10 Tests and 10 Asserts
class TestQuasiThresholdGenerator10Nodes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.filename = f"generated_graphs_{dt.now().strftime('%Y-%m-%d')}.txt"
        with open(cls.filename, "w") as f:
            pass  # just clear the file

    def test_10_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(10)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))
    
    def test_20_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(20)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_30_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(30)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_40_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(40)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_50_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(50)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_60_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(60)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_70_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(70)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_80_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(80)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_90_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(90)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_100_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(100)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

if __name__ == '__main__':
    unittest.main()