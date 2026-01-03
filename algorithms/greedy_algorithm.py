import networkx as nx
from compute_PC import compute_pc
from collections import defaultdict

def greedy_algorithm(
    G: nx.Graph, terminals: list[int], 
    K: int, case: int) -> list[int]:
  
  # If graph is too big, use sparse representation
  # for better memory usage
  
  S = []

  for _ in range(K):
    max_pc = float('-inf')
    max_v = 0

    V = list(G.nodes)

    for node in V:

      if case == 1:
        # case 1: S in V
        current_pc = compute_pc(G, terminals)

      if case == 2:
        # case 2: S in V \ T
        if node not in terminals:
          current_pc = compute_pc(G, terminals)    

      if max_pc < current_pc:
        max_pc = current_pc
        max_v = node

    S.append(max_v)

  return S



