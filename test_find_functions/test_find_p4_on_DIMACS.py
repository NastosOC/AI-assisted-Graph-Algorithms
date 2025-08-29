import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *
from functions.read_DIMACS import read_dimacs_clq

# 37 Tests and 111 Asserts
class TestFindAllP4DIMACS(unittest.TestCase):
    
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


 # DIMACS graphs - 30-vertex subgraph
    def test_brock200_2(self):
        G = read_dimacs_clq("DIMACS_files/brock200_2.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_brock200_4(self):
        G = read_dimacs_clq("DIMACS_files/brock200_4.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_brock400_2(self):
        G = read_dimacs_clq("DIMACS_files/brock400_2.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_brock400_4(self):
        G = read_dimacs_clq("DIMACS_files/brock400_4.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_brock800_2(self):
        G = read_dimacs_clq("DIMACS_files/brock400_2.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_brock800_4(self):
        G = read_dimacs_clq("DIMACS_files/brock400_4.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_C125_9(self):
        G = read_dimacs_clq("DIMACS_files/C125_9.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_C250_9(self):
        G = read_dimacs_clq("DIMACS_files/C250_9.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_C500_9(self):
        G = read_dimacs_clq("DIMACS_files/C500_9.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_C1000_9(self):
        G = read_dimacs_clq("DIMACS_files/C1000_9.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_C2000_5(self):
        G = read_dimacs_clq("DIMACS_files/C2000_5.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_C2000_9(self):
        G = read_dimacs_clq("DIMACS_files/C2000_9.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_C4000_5(self):
        G = read_dimacs_clq("DIMACS_files/C4000_5.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_DSJC500_5(self):
        G = read_dimacs_clq("DIMACS_files/DSJC500_5.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_DSJC1000_5(self):
        G = read_dimacs_clq("DIMACS_files/DSJC1000_5.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_gen200_p09_44(self):
        G = read_dimacs_clq("DIMACS_files/gen200_p09_44.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_gen200_p09_55(self):
        G = read_dimacs_clq("DIMACS_files/gen200_p09_55.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_gen400_p09_55(self):
        G = read_dimacs_clq("DIMACS_files/gen400_p09_55.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_gen400_p09_65(self):
        G = read_dimacs_clq("DIMACS_files/gen400_p09_65.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_gen400_p09_75(self):
        G = read_dimacs_clq("DIMACS_files/gen400_p09_75.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_hamming8_4(self):
        G = read_dimacs_clq("DIMACS_files/hamming8_4.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_hamming10_4(self):
        G = read_dimacs_clq("DIMACS_files/hamming10_4.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_keller4(self):
        G = read_dimacs_clq("DIMACS_files/keller4.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_keller5(self):
        G = read_dimacs_clq("DIMACS_files/keller5.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_keller6(self):
        G = read_dimacs_clq("DIMACS_files/keller6.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_MANN_a27(self):
        G = read_dimacs_clq("DIMACS_files/MANN_a27.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_MANN_a45(self):
        G = read_dimacs_clq("DIMACS_files/MANN_a45.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_MANN_a81(self):
        G = read_dimacs_clq("DIMACS_files/MANN_a81.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat300_1(self):
        G = read_dimacs_clq("DIMACS_files/p_hat300_1.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat300_2(self):
        G = read_dimacs_clq("DIMACS_files/p_hat300_2.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat300_3(self):
        G = read_dimacs_clq("DIMACS_files/p_hat300_3.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat700_1(self):
        G = read_dimacs_clq("DIMACS_files/p_hat700_1.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat700_2(self):
        G = read_dimacs_clq("DIMACS_files/p_hat700_2.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat700_3(self):
        G = read_dimacs_clq("DIMACS_files/p_hat700_3.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat1500_1(self):
        G = read_dimacs_clq("DIMACS_files/p_hat1500_1.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat1500_2(self):
        G = read_dimacs_clq("DIMACS_files/p_hat1500_2.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

    def test_p_hat1500_3(self):
        G = read_dimacs_clq("DIMACS_files/p_hat1500_3.txt")
        H = G.subgraph(31)

        actual = find_all_p4(H)

        self.assertIsP4s(H, actual)
        self.assertAllValidNodes(H, actual)
        self.assertNoDuplicates(actual)

if __name__ == '__main__':
    unittest.main()