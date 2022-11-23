import os
from time import *
from random import sample

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
  
  print("{0:>15s} | {1:,d}".format('Nodes', n))
  print("{0:>15s} | {1:,d}".format('Edges', m))
  
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

tic = time()

# Constructs small toy graph

G = nx.MultiGraph(name = 'toy')

G.add_node(1)
G.add_node(2)

G.add_edge(1, 2)

# Prints out statistics of toy graph

graph_info(G)

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))

# 'karate', 'women', 'dolphins', 'ingredients', 'darknet', 'ppi', 'internet', 'amazon', 'aps', 'google', 'texas'
