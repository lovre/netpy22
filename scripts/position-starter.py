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
  
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

tic = time()

# Constructs a graph of real network

G = read_pajek('imdb')
  
# Prints out statistics of real network
  
graph_info(G)

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))

# 'got-kills', 'lpp', 'ingredients', 'imdb'
