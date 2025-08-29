import networkx as nx
import unittest
from networkx import *

# 10 Tests and 10 Asserts
class TestIsChordal(unittest.TestCase):
    # Using lists of chordal graphs from: https://users.cecs.anu.edu.au/~bdm/data/graphs.html
    def test_4_vertex(self):
        graphs = read_graph6("Graph6_files/chordal_4v.txt")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_4_vertex_total(self):
        # Result should be 5
        chordal_count = 0
        graphs = read_graph6("Graph6_files/chordal_4v.txt")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(5, chordal_count)

    def test_5_vertex(self):
        graphs = read_graph6("Graph6_files/chordal_5v.txt")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_5_vertex_total(self):
        # Result should be 15
        chordal_count = 0
        graphs = read_graph6("Graph6_files/chordal_5v.txt")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(15, chordal_count)

    def test_6_vertex(self):
        graphs = read_graph6("Graph6_files/chordal_6v.txt")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_6_vertex_total(self):
        # Result should be 58
        chordal_count = 0
        graphs = read_graph6("Graph6_files/chordal_6v.txt")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(58, chordal_count)

    def test_7_vertex(self):
        graphs = read_graph6("Graph6_files/chordal_7v.txt")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_7_vertex_total(self):
        # Result should be 272
        chordal_count = 0
        graphs = read_graph6("Graph6_files/chordal_7v.txt")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(272, chordal_count)

    def test_8_vertex(self):
        graphs = read_graph6("Graph6_files/chordal_8v.txt")
        for index, G in enumerate(graphs):
            self.assertTrue(is_chordal(G))

    def test_8_vertex_total(self):
        # Result should be 1614
        chordal_count = 0
        graphs = read_graph6("Graph6_files/chordal_8v.txt")
        for index, G in enumerate(graphs):
            if is_chordal(G):
                chordal_count += 1
        
        self.assertEqual(1614, chordal_count)

if __name__ == '__main__':
    unittest.main()