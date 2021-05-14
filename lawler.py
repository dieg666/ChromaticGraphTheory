import networkx as nx
import grinpy as gp
import utils
import matplotlib.pyplot as plt
G = nx.read_gpickle("data/graph001.gpickle")
n = G.number_of_nodes()
X = [0]*(2**n-1)
S = utils.get_independent_set(G)
MIS = utils.get_max_independent_set(G)
#G[0] = {set of nodes}

print(n)
print(len(S))
print(len(X))

print(G.graph["Chromatic number"])
for s in S:
    for mis in MIS:
        pass


pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
                        node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, arrows=False)
plt.show()
plt.draw()
