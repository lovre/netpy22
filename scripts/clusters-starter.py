import os
from time import *

import networkx as nx

from cdlib import algorithms
from cdlib.classes import *
from cdlib import viz

def read_pajek(file, path = '../nets'):
  """
  Construct undirected multigraph G from specified file in Pajek format.
  """
  
  G = nx.MultiGraph(name = file)
  
  with open(os.path.join(path, file + '.net'), 'r') as file:
    nodes = {}
    for line in file:
      if line.startswith('*vertices'):
        continue
      elif line.startswith('*'):
        break
      else:
        node = line.strip().split('"')
        nodes[node[0].strip()] = node[1]
        G.add_node(node[1], cluster = int(node[2]) if len(node[2]) > 0 else 0)
        
    for line in file:
      edge = line.strip().split(' ')
      G.add_edge(nodes[edge[0]], nodes[edge[1]])
      
  return G
  
def known_clusters(G):
  """
  Construct clustering of undirected multigraph G from node attribute 'cluster'.
  """

  clusters = {}
  for i, data in G.nodes(data = True):
    c = data['cluster'] if 'cluster' in data else 0
    
    if c in clusters:
      clusters[c].append(i)
    else:
      clusters[c] = [i]
    
  return NodeClustering(list(clusters.values()), G, 'known')

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
  
def clusters_info(G, alg, label, k = 100):
  """
  Find and print out standard statistics of clusters of undirected multigraph G.
  """
  
  print("{0:>15s} | '{1:s}'".format('Graph', G.name.replace('_', '-')))
  print("{0:>15s} | '{1:s}' ({2:d}x)".format('Algorithm', label, k))
  
  known = known_clusters(G)
  
  t, c, C, Q, NMI = 0, 0, 0, 0, 0
  for _ in range(k):
    tic = time()
    
    comms = alg(G)
    
    t += (time() - tic) / k
    
    c += len(comms.communities) / k
    C += max(len(comm) for comm in comms.communities) / k
    Q += comms.newman_girvan_modularity().score / k
    
    NMI += known.normalized_mutual_information(comms).score / k
    
  print("{0:>15s} | {1:,.1f} x {2:,.0f} ({3:.1f}%)".format('Clusters', c, len(G) / c, 100 * C / len(G)))
  
  print("{0:>15s} | {1:.3f}".format('Q', Q))
  
  print("{0:>15s} | {1:.3f}".format('NMI', NMI))
  
  print("{0:>15s} | {1:.1f} sec\n".format('Time', t))
  
  return comms

tic = time()

# Constructs a graph of real network

G = read_pajek('karate')

# Prints out statistics of real network

graph_info(G)

# Finds community structure of real network

clusters_info(G, lambda G: algorithms.girvan_newman(G, level = 1), 'betweenness')

print("{0:>15s} | {1:.1f} sec\n".format('Total', time() - tic))
