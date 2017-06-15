import networkx as nx
import urllib  
import matplotlib.pyplot as plt                                        
url = "http://networkdata.ics.uci.edu/data/football/football.gml"
f = urllib.urlopen(url)
myfile = f.read()
#print myfile
G=nx.path_graph(115)
#G = nx.read_gml(myfile)
G.node
G.edge
nx.draw_random(G)
plt.show()
