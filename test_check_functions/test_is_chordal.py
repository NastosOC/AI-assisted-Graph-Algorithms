import networkx as nx
import unittest
from networkx import *

# 10 Tests and 10 Asserts
class TestIsChordal(unittest.TestCase):
    """
    Verifying the networkX function is_chordal(nx.Graph) on the list of chordal graphs from:
    https://users.cecs.anu.edu.au/~bdm/data/graphs.html
    """

    def test_4_vertex(self):
        try:
            graphs = read_graph6("Graph6_files/chordal_4v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_4_vertex_total(self):
        # Result should be 5
        chordal_count = 0
        try:
            graphs = read_graph6("Graph6_files/chordal_4v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(5, chordal_count)

    def test_5_vertex(self):
        try:
            graphs = read_graph6("Graph6_files/chordal_5v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_5_vertex_total(self):
        # Result should be 15
        chordal_count = 0
        try:
            graphs = read_graph6("Graph6_files/chordal_5v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(15, chordal_count)

    def test_6_vertex(self):
        try:
            graphs = read_graph6("Graph6_files/chordal_6v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_6_vertex_total(self):
        # Result should be 58
        chordal_count = 0
        try:
            graphs = read_graph6("Graph6_files/chordal_6v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(58, chordal_count)

    def test_7_vertex(self):
        try:
            graphs = read_graph6("Graph6_files/chordal_7v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_7_vertex_total(self):
        # Result should be 272
        chordal_count = 0
        try:
            graphs = read_graph6("Graph6_files/chordal_7v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(272, chordal_count)

    def test_8_vertex(self):
        try:
            graphs = read_graph6("Graph6_files/chordal_8v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_8_vertex_total(self):
        # Result should be 1614
        chordal_count = 0
        try:
            graphs = read_graph6("Graph6_files/chordal_8v.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(1614, chordal_count)

if __name__ == '__main__':
    unittest.main()