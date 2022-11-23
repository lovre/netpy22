import os
from time import *

import networkx as nx

def read_pajek(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  
  G = nx.read_pajek(os.path.join(path, file + '.net'))
  G.name = file
  
  return G
  
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
  
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

def top_nodes(G, centrality, label, n = 15):
  """
  Compute and print out node centralities of undirected multigraph G.
  """
  
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  print("{0:>15s} | '{1:s}'".format('Centrality', label))
  
  for p, (i, c) in enumerate(sorted(centrality.items(), key = lambda item: (-item[1], -G.degree(item[0]), item[0]))):
    if p >= n:
      break
    print("{0:>15.8f} | '{1:s}' ({2:,d})".format(c, i, G.degree(i)))
  print()

tic = time()

for file in ['got-kills', 'lpp', 'ingredients', 'imdb']:

  # Constructs a graph of real network
  
  G = read_pajek(file)
  G = nx.Graph(G)
  
  # Prints out statistics of real network
  
  graph_info(G)
  
  # Prints top degree centrality nodes of real network

  top_nodes(G, nx.degree_centrality(G), 'degree')
  
  # Prints top clustering coefficient nodes of real network

  top_nodes(G, nx.clustering(G), 'clustering')
  top_nodes(G, {i: c * (G.degree(i) - 1) for i, c in nx.clustering(G).items()}, 'μ-clustering')

  # Prints top spectral centrality nodes of real network
  
  top_nodes(G, nx.eigenvector_centrality(G, tol = 1e-04), 'eigenvector')
  top_nodes(G, nx.pagerank(G), 'pagerank')

  # Prints top distance centrality nodes of real network

  top_nodes(G, nx.closeness_centrality(G), 'closeness')
  top_nodes(G, nx.betweenness_centrality(G), 'betweenness')

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
