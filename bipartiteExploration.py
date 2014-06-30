
import networkx as nx
from networkx.algorithms import bipartite
import pylab

bp = nx.Graph()

bp = nx.bipartite_random_graph(10, 100,.3)

left = set(x for x, y in bp.nodes(data = True) if y['bipartite']== 0)

right = set(bp) - left

edges = bp.edges(left)

pylab.scatter([x[0] for x in edges], [y[1] for y in edges])

#centrality = bipartite.centrality.closeness_centrality(bp, set(bp))
#
#pylab.plot([centrality[x] for x in centrality])

pylab.show()

