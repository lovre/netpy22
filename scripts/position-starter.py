import os
from time import *
import operator as op
import networkx as nx

def read(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  G = nx.read_pajek(os.path.join(path, file + '.net'))
  G.name = file
  return G

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
  CCs = sorted(nx.connected_components(G), key = len, reverse = True)
  print("{0:>15s} | {1:.1f}% ({2:,d})".format('Components', 100.0 * len(CCs[0]) / G.number_of_nodes(), len(CCs)))
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))

#def tops(G, centrality, label, n = 15):
#  """
#  Compute and print out node centralities of undirected multigraph G.
#  """
#  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
#  print("{0:>15s} | '{1:s}'".format('Centrality', label))
#  for p, (i, c) in enumerate(sorted(centrality.items(), key = op.itemgetter(1), reverse = True)):
#    if p < n:
#      print("{0:>15.8f} | '{1:s}' ({2:,d})".format(c, i, G.degree(i)))
#  print()

tic = time()

# Constructs a graph of real network

G = read('imdb')
  
# Prints out statistics of real network
  
info(G)

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
