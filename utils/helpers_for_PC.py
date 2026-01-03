from collections import deque
import networkx as nx

def bfs(G: nx.Graph, source: int, visited: list[bool]) -> list:
  queue = deque()
  res = []

  visited[source] = True
  queue.append(source)

  while len(queue) > 0:

    v = queue.pop()
    res.append(v)
    # print(f"queue: {v}")

    for u in G.neighbors(v):
      if not visited[u]:
        visited[u] = True
        queue.append(u)
        # print(f"queue append: {u}")

  return res

def connected_components(G: nx.Graph):
  visited = [False] * len(G.nodes)
  components = []

  for v in list(G.nodes):
    if not visited[v]:
      comp = bfs(G, v, visited)
      components.append(comp)

  return components