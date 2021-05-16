import networkx as nx
import itertools as I
import utils
def convert(G,L):
    k = 0
    L2 = L.copy()
    for i in list(G.nodes()):
        if k == i:
            pass
        for l in L2:
            l = list(l)
            if l[0] == i:
                left = k
            if l[1] == i:
                l[1] = k
            l = tuple(l)
        k += 1
    return L2
def eppstein(G):
    X = {}
    for S in utils.subsets_of_graph(G):
        substraction = [item for item in G.nodes() if item not in S]
        S2 = utils.createGraph(substraction,G)
        X[str(S)] = len(S)
        for I in utils.get_max_independent_set(S2):
            addition = utils.add(S,I)
            if not str(addition) in X:
                X[str(addition)] = len(addition)
            X[str(addition)] = min(X[str(S)],X[str(addition)] + 1)
    return X[str(list(G.nodes()))]
correct = 0
wrong = 0
for i in range(5,6):
    G = nx.read_gpickle("data/graph"+'{0:03}'.format(i)+".gpickle")
    x = eppstein(G)
    if x != G.graph["Chromatic number"]:
        print(str(x)+" vs "+str(G.graph["Chromatic number"]))
        print("WRONG:: test/graph"+'{0:03}'.format(i)+".gpickle")
        wrong += 1
    else:
        print("RIGHT:: test/graph"+'{0:03}'.format(i)+".gpickle")
        correct += 1

import itertools as I

#G = nx.read_gpickle("test/graph022.gpickle")
#A = nx.to_numpy_matrix(G)
#print(A)
#print(c(G.number_of_nodes(), list(G.edges())))
#pos = nx.spring_layout(G)
#nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
#                        node_size = 500)
#nx.draw_networkx_labels(G, pos)
#nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True)
#nx.draw_networkx_edges(G, pos, arrows=False)
#plt.show()
#plt.draw()
