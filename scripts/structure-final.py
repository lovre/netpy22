import os
from time import *
from random import sample

import matplotlib.pyplot as plt

import networkx as nx

def read_pajek(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  
  G = nx.read_pajek(os.path.join(path, file + '.net'))
  G.name = file
  
  return G

def approx_dists(G, n = 100):
  """
  Compute approximate average distance and diameter of undirected multigraph G.
  """
  
  ds = []
  for i in G.nodes() if len(G) <= n else sample(G.nodes(), n):
    ds.extend([d for d in nx.shortest_path_length(G, source = i).values() if d > 0])
    
  return sum(ds) / len(ds), max(ds)

def graph_info(G):
  """
  Compute and print out standard statistics of undirected multigraph G.
  """
  
  tic = time()
  
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  
  multi = False
  for edge in G.edges():
    if G.number_of_edges(edge[0], edge[1]) > 1:
      multi = True
      break
      
  print("{0:>15s} | '{1:s}'".format('Type', '===' if multi else '---'))
  
  n = G.number_of_nodes()
  m = G.number_of_edges()
  
  print("{0:>15s} | {1:,d} ({2:,d})".format('Nodes', n, nx.number_of_isolates(G)))
  print("{0:>15s} | {1:,d} ({2:,d})".format('Edges', m, nx.number_of_selfloops(G)))
  
  ks = [k for _, k in G.degree()]
  
  print("{0:>15s} | {1:.1f} ({2:,d}, {3:,d})".format('Degree', 2 * m / n, min(ks), max(ks)))
  print("{0:>15s} | {1:.8f}".format('Density', 2 * m / n / (n - 1)))
  
  CCs = sorted(nx.connected_components(G), key = len, reverse = True)

  print("{0:>15s} | {1:.1f}% ({2:,d})".format('Components', 100 * len(CCs[0]) / n, len(CCs)))

  d, D = approx_dists(G.subgraph(CCs[0]))

  print("{0:>15s} | {1:.3f} ({2:,d})".format('Distances', d, D))

  C = nx.average_clustering(G if type(G) == nx.Graph else nx.Graph(G))

  print("{0:>15s} | {1:.6f}".format('Clustering', C))
  
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

def deg_dist(G):
  """
  Plots degree distribution of undirected multigraph G.
  """
  
  nk = {}
  for _, k in G.degree():
    if k not in nk:
      nk[k] = 0
    nk[k] += 1
  ks = list(nk)
  
  plt.loglog(ks, [nk[k] / len(G) for k in ks], '*k')
  plt.ylabel('Fraction of nodes')
  plt.xlabel('Node degree')
  plt.title(G.name)
  plt.show()

tic = time()

# Constructs small toy graph

G = nx.MultiGraph(name = 'toy') # Graph, MultiGraph, DiGraph, MultiDiGraph

G.add_node(1)
G.add_node(2)
G.add_node('foo', cluster = 1)
G.add_node('bar', value = 13.7)
G.add_node('baz')

G.add_edge(1, 2)
G.add_edge(1, 'foo')
G.add_edge(2, 'foo')
G.add_edge('foo', 'bar', weight = 2.0)

# print(G.nodes(data = True))
# print(G.edges(data = True))
# print(G[1]) # G.neighbors(1)
# print(len(G))

# Prints out statistics of toy graph

graph_info(G)

for file in ['karate', 'women', 'dolphins', 'ingredients', 'darknet', 'ppi', 'internet', 'amazon']: # 'aps', 'google', 'texas'

  # Constructs graph representing real network
  
  G = read_pajek(file)
  
  # Prints out statistics of real network
  
  graph_info(G)
  
  n = G.number_of_nodes()
  m = G.number_of_edges()

  # Plots degree distribution of real network

  if n > 5000 or True:
    deg_dist(G)

  # Prints out statistics of Erdös-Rényi random graph

  ER = nx.gnm_random_graph(n, m)
  ER.name = 'Erdös-Rényi'

  graph_info(ER)

  # Prints out statistics of Barabási–Albert scale-free graph

  BA = nx.barabasi_albert_graph(n, round(m / n))
  BA.name = 'Barabási–Albert'

  graph_info(BA)

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
