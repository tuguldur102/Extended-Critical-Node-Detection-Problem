import networkx as nx
import math
from utils.helpers_for_PC import bfs, connected_components

def compute_pc(
    G: nx.Graph, terminal_nodes: list[int]
    ) -> int:

  # 1. Get connected components
  # visited = [False] * len(G.nodes)
  # components = []

  # for v in list(G.nodes):
  #   if not visited[v]:
  #     comp = bfs(G, v, visited)
  #     components.append(comp)

  components = connected_components(G)

  # 2. Exclude non-terminal nodes from the components
  excluded_components = []

  for comp in components:
    excluded_comp = []
    for v in comp:
      if v in terminal_nodes:
        excluded_comp.append(v)
      
    excluded_components.append(excluded_comp)

  # 3. Compute pairwise connectivity using comb(n, 2) = n! / (n - 2)! * 2!
  pairwise_connectivity = 0

  for comp in excluded_components:
    n = int(len(comp))
    pairwise_connectivity += math.comb(n, 2)

  return pairwise_connectivity