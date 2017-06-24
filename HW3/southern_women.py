import networkx as nx
import networkx.algorithms.bipartite as bipartite
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy import stats
import numpy as np
import csv
import math

G = nx.davis_southern_women_graph()
women = G.graph['top']
clubs = G.graph['bottom']
print(bipartite.is_bipartite(G))
rc = bipartite.node_redundancy(G)
print(bipartite.node_redundancy(G))
print(sum(rc.values()) / len(G))

c = bipartite.clustering(G)
print(bipartite.clustering(G))
print(bipartite.average_clustering(G))

print("Biadjacency matrix")
print(bipartite.biadjacency_matrix(G,women,clubs))

# project bipartite graph onto women nodes
W = bipartite.projected_graph(G, women)
print('')
print("#Friends, Member")
for w in women:
    print('%d %s' % (W.degree(w),w))

# project bipartite graph onto women nodes keeping number of co-occurence
# the degree computed is weighted and counts the total number of shared contacts
W = bipartite.weighted_projected_graph(G, women)
print('')
print("#Friend meetings, Member")
for w in women:
    print('%d %s' % (W.degree(w,weight='weight'),w))
    
pos = nx.spring_layout(W, k=.5,iterations=50)
nx.draw_networkx_labels(W,pos,font_size=20,font_family='sans-serif', font_color = "red")
 
nx.draw_networkx_edges(W,pos,alpha=0.25,width=6)
nx.draw_networkx_nodes(W,pos,node_size=3000, node_color='yellow')

plt.rcParams["figure.figsize"] = [20,20]
plt.show(block=True)
degree_centrality = nx.degree_centrality(W)
for key, value in sorted(degree.degree_centrality(), key=lambda (k,v): (v,k), reverse = True):
    print "%s: %s" % (key, value)
    

degree = nx.degree(W)
for key, value in sorted(degree.iteritems(), key=lambda (k,v): (v,k), reverse = True):
    print "%s: %s" % (key, value)
    

e = bipartite.projected_graph(G, clubs)

degree = nx.degree(e)
for key, value in sorted(degree.iteritems(), key=lambda (k,v): (v,k), reverse = True):
    print "%s: %s" % (key, value)
    

stats.mode(degree.values())[0][0]
np.mean(degree.values())
np.std(degree.values())


e1 = nx.ego_graph(G, "E1", radius=1, center=True, undirected=False, distance=None)                	