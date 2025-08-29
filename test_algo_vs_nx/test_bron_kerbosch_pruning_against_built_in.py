import networkx as nx
import unittest
from networkx import find_cliques
from functions.check_functions import is_clique
from functions.clique_algorithms import max_clique
from functions.read_DIMACS import read_dimacs_clq

# 37 Tests and 222 Asserts
class TestBronKerboschPruningAgainstBuiltIn(unittest.TestCase):
    """
    Compares outputs of max_clique(nx.Graph) to networkX built-in function find_cliques(nx.Graph)
    ---THIS IS A PRUNING VARIANT OF THE BRON KERBOSCH ALGORITHM---
    Each test compares output using a 30-node subgraph of all DIMACS graphs.
    Asserts for each case run through:
        Confirming the clique the algorithm finds is a valid clique
        Confirming all nodes exist within the subgraph
        Confirming no duplicate nodes were returned
        A sanity test confirming the clique size is not 0
        A sanity test confirming the clique size does not exceed 30
        A final check for correct max clique length compared to find_cliques(nx.Graph)
    """

    def assertIsClique(self, G, clq):
        """
        Assert that clq is a valid clique.
        Parameters:
            G (networkX.Graph): The graph
            clq (list): List of nodes
        """
        self.assertTrue(is_clique(G, clq)) # Makes sure it's a valid clique

    # DIMACS graphs - 30-vertex subgraph
    def test_brock200_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock200_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_brock200_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock200_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_brock400_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock400_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_brock400_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock400_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_brock800_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock800_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_brock800_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/brock800_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_C125_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C125_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_C250_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C250_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_C500_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C500_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_C1000_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C1000_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_C2000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C2000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_C2000_9(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C2000_9.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_C4000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/C4000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_DSJC500_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/DSJC500_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_DSJC1000_5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/DSJC1000_5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_gen200_p09_44(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen200_p09_44.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_gen200_p09_55(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen200_p09_55.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_gen400_p09_55(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_55.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_gen400_p09_65(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_65.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_gen400_p09_75(self):
        try:
            G = read_dimacs_clq("DIMACS_files/gen400_p09_75.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_hamming8_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/hamming8_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_hamming10_4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/hamming10_4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_keller4(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller4.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_keller5(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller5.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_keller6(self):
        try:
            G = read_dimacs_clq("DIMACS_files/keller6.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_MANN_a27(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a27.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_MANN_a45(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a45.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_MANN_a81(self):
        try:
            G = read_dimacs_clq("DIMACS_files/MANN_a81.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat300_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat300_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat300_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat300_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat700_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat700_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat700_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat700_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat1500_1(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_1.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat1500_2(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_2.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

    def test_p_hat1500_3(self):
        try:
            G = read_dimacs_clq("DIMACS_files/p_hat1500_3.txt")
        except IndexError as e:
            self.skipTest(f"Skipping test due to IndexError: {e}")
        H = G.subgraph(range(25))

        max_i = max(find_cliques(H), key=len)
        max_c = max_clique(H)

        self.assertIsClique(H, max_c)
        self.assertTrue(set(max_c).issubset(H.nodes))
        self.assertEqual(len(max_c), len(set(max_c)))
        self.assertGreater(len(max_c), 0) # Clique size > 0
        self.assertLessEqual(len(max_c), 30) # Clique size <= 30 (size of H)
        self.assertEqual(len(max_i), len(max_c))

if __name__ == '__main__':
    unittest.main()