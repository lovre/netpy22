import os
from time import *
import networkx as nx
from random import sample
import matplotlib.pyplot as plt

def read(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  G = nx.read_pajek(os.path.join(path, file + '.net'))
  G.name = file
  return G

def dists(G, n = 100):
  """
  Compute approximate average distance and diameter of undirected multigraph G.
  """
  ds = []
  for i in G.nodes() if len(G) <= n else sample(G.nodes(), n):
    ds.extend([d for d in nx.shortest_path_length(G, source = i).values() if d > 0])
  return sum(ds) / len(ds), max(ds)

def info(G):
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
  print("{0:>15s} | {1:,d} ({2:,d})".format('Nodes', G.number_of_nodes(), nx.number_of_isolates(G)))
  print("{0:>15s} | {1:,d} ({2:,d})".format('Edges', G.number_of_edges(), nx.number_of_selfloops(G)))
  ks = [k for _, k in G.degree()]
  print("{0:>15s} | {1:.1f} ({2:,d}, {3:,d})".format('Degree', 2.0 * G.number_of_edges() / G.number_of_nodes(), min(ks), max(ks)))
  print("{0:>15s} | {1:.8f}".format('Density', 2.0 * G.number_of_edges() / G.number_of_nodes() / (G.number_of_nodes() - 1.0)))
  CCs = sorted(nx.connected_components(G), key = len, reverse = True)
  print("{0:>15s} | {1:.1f}% ({2:,d})".format('Components', 100.0 * len(CCs[0]) / G.number_of_nodes(), len(CCs)))
  d, D = dists(G.subgraph(CCs[0]))
  print("{0:>15s} | {1:.3f} ({2:,d})".format('Distances', d, D))
  print("{0:>15s} | {1:.6f}".format('Clustering', nx.average_clustering(nx.Graph(G))))
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

def dist(G):
  """
  Plots degree distribution of undirected multigraph G.
  """
  nk = {}
  for i in G.nodes():
    k = G.degree(i)
    if k not in nk:
      nk[k] = 0
    nk[k] += 1
  ks = nk.keys()
  plt.loglog(ks, [nk[k] / len(G) for k in ks], '*k')
  plt.ylabel('Fraction of nodes')
  plt.xlabel('Node degree')
  plt.title(G.name)
  plt.show()

tic = time()

# Constructs small toy graph

G = nx.MultiGraph(name = 'toy')
G.add_node(1)
G.add_node(2)
G.add_node('foo')
G.add_node('bar')
G.add_node('baz')
G.add_edge(1, 2)
G.add_edge(1, 'foo')
G.add_edge(2, 'foo')
G.add_edge('foo', 'bar')

# Prints out statistics of toy graph

info(G)

for file in ['karate', 'women', 'dolphins', 'ingredients', 'darknet', 'ppi', 'internet']: # 'amazon', 'aps', 'google', 'texas'

  # Constructs graph representing real network
  
  G = read(file)
  
  # Prints out statistics of real network
  
  info(G)
  
  # Plots degree distribution of real network
  
  if len(G) > 5000:
    dist(G)

  # Prints out statistics of Erdös-Rényi random graph
  
  ER = nx.gnm_random_graph(G.number_of_nodes(), G.number_of_edges())
  ER.name = 'Erdös-Rényi'
  info(ER)
  
  # Prints out statistics of Barabási–Albert scale-free graph

  BA = nx.barabasi_albert_graph(G.number_of_nodes(), round(G.number_of_edges() / G.number_of_nodes()))
  BA.name = 'Barabási–Albert'
  info(BA)

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
