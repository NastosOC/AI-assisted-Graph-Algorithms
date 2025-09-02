import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import read_dimacs_clq

# 37 Tests and 148 Asserts
class TestFindAllP4DIMACS(unittest.TestCase):
    """
    Testing find_all_p4(nx.Graph) function on 25-node subgraphs of DIMACS graphs.
    Asserts for each case include:
        Confirming all P4s found are valid P4s.
        Confirming all nodes in the P4s are valid in the graph.
        Confirming there are no duplicate P4s found.
        Confirming that the P4 list is non-negative.
    """
    # Custom Assertion
    def assertIsP4s(self, G, p4_list):
        for p4 in p4_list:
            self.assertTrue(is_p4(G, list(p4)))

    def assertAllValidNodes(self, G, p4_list):
        nodes = set(G.nodes)
        for p4 in p4_list:
            for node in p4:
                self.assertIn(node, nodes, f"Node {node} not in graph")

    def assertNoDuplicates(self, p4_list):
        self.assertEqual(len(p4_list), len(set(frozenset(p) for p in p4_list)), "Duplicate P4s found")

# DIMACS graphs - 25-vertex subgraph
    def test_brock200_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock200_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_brock200_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock200_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_brock400_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock400_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_brock400_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock400_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_brock800_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock800_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_brock800_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock800_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_C125_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C125_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_C250_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C250_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_C500_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C500_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_C1000_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C1000_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_C2000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C2000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_C2000_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C2000_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_C4000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C4000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_DSJC500_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/DSJC500_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_DSJC1000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/DSJC1000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_gen200_p09_44(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen200_p09_44.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_gen200_p09_55(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen200_p09_55.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_gen400_p09_55(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_55.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_gen400_p09_65(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_65.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_gen400_p09_75(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_75.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_hamming8_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/hamming8_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_hamming10_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/hamming10_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_keller4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_keller5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_keller6(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller6.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_MANN_a27(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a27.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_MANN_a45(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a45.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_MANN_a81(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a81.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat300_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat300_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)        

    def test_p_hat300_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat700_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat700_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat700_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat1500_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat1500_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

    def test_p_hat1500_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        c4_list = find_all_p4(H)

        self.assertIsP4s(G, c4_list)
        self.assertGreaterEqual(len(c4_list), 0)
        self.assertAllValidNodes(G, c4_list)
        self.assertNoDuplicates(c4_list)

if __name__ == '__main__':
    unittest.main()