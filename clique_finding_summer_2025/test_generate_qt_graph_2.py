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

    def test_110_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(110)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))
    
    def test_120_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(120)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_130_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(130)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_140_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(140)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_150_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(150)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_160_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(160)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_170_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(170)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_180_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(180)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_190_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(190)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

    def test_200_node(self):
        with open(self.__class__.filename, "a") as f:
            for n in range(1000):
                G = generate_trivially_perfect_graph(200)
                g6 = nx.to_graph6_bytes(G, header=False).decode().strip()
                f.write(f"{g6}\n")
                self.assertTrue(is_quasi_threshold(G))

if __name__ == '__main__':
    unittest.main()