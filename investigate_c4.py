import networkx as nx
import unittest
from functions.check_functions import *
from functions.find_functions import *

G = nx.erdos_renyi_graph(8, 0.5)
print(f"Random 8-node Graph:")
for e in G.edges():
    print(f"Edge: {e}")

H = nx.complete_graph(6)
print(f"Complete 6-node Graph:")
for e in H.edges():
    print(f"Edge: {e}")