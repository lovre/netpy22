import os
import warnings
from time import *
import networkx as nx
from cdlib import viz
from cdlib.classes import *
from cdlib import algorithms
from matplotlib import pyplot as plt

def read(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  G = nx.MultiGraph(name = file)
  nodes = {}
  with open(os.path.join(path, file + '.net'), 'r') as file:
    for line in file:
      if line.startswith('*vertices'):
        continue
      elif line.startswith('*edges') or line.startswith('*arcs'):
        break
      else:
        node = line.strip().split('"')
        nodes[node[0].strip()] = node[1]
        G.add_node(node[1], cluster = int(node[2]) if len(node[2]) > 0 else 0)
    for line in file:
      edge = line.strip().split(' ')
      G.add_edge(nodes[edge[0]], nodes[edge[1]])
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

def clusters(G, alg):
  """
  Find and print out standard statistics of clusters of undirected multigraph G.
  """
  tic = time()
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  comms = alg(G)
  print("{0:>15s} | '{1:s}'".format('Algorithm', comms.method_name.lower()))
  print("{0:>15s} | {1:,d}".format('Clusters', len(comms.communities)))
#  truth = {}
#  for node in G.nodes(data = True):
#    cluster = node[1]['cluster'] if 'cluster' in node[1] else 0
#    if cluster not in truth:
#      truth[cluster] = []
#    truth[cluster].append(node[0])
#  truth = NodeClustering(list(truth.values()), G, 'truth')
  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))
  return comms

tic = time()

# Constructs a graph of real network

G = read('karate')

# Prints out statistics of real network

info(G)

# Finds community structure of real network

comms = clusters(G, lambda G: algorithms.girvan_newman(G, level = 1))

#def kcores(G, k):
#  """
#  Find and construct k-cores of undirected multigraph G for specified k.
#  """
#  K = nx.MultiGraph(G)
#  K.name = str(k) + '-core'
#  change = True
#  while change:
#    change = False
#    for i in list(K.nodes()):
#      if K.degree(i) < k:
#        K.remove_node(i)
#        change = True
#  return K

#def kstars(G):
#  """
#  Find and print out largest k-cores of undirected multigraph G.
#  """
#  tic = time()
#  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
#  k = 1
#  K = nx.MultiGraph(G)
#  while True:
#    K1 = kcores(K, k)
#    if K1.number_of_nodes() == 0:
#      break
#    K = K1
#    k += 1
#  CCs = sorted(nx.connected_components(K), key = len, reverse = True)
#  print("{0:>15s} | {1:,d} ({2:,d})".format(K.name, len(CCs[0]), len(CCs)))
#  print("{0:>15s} | {1:.1f} sec\n".format('Time', time() - tic))
#  return K

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
