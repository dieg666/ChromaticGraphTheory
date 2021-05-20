import networkx as nx
import itertools as I
import utils
import math
import sys
import grinpy as gp
def eppstein(G):
    X = {}
    for S in utils.subsets_of_graph(G):
        S2 = utils.createGraph(S, G)
        X[str(S)] = 999
        chromatic_number = gp.chromatic_number(S2)
        if chromatic_number == 3:
            X[str(S2.nodes())] == 3
        elif chromatic_number == 2:
            X[str(S2.nodes())] == 2
        elif chromatic_number == 1:
            X[str(S2.nodes())] == 1
    for S in utils.subsets_of_graph(G):
        if 3 <= X[str(S)] < 999:
            substraction = utils.diff(list(G.nodes()), S)
            S2 = utils.createGraph(substraction,G)
            for I in utils.get_max_independent_set(S2):
                if len(I) >= (len(S)/ X[str(S)]):
                    addition = utils.add(S,I)
                    addition.sort()
                    X[str(addition)] = min(X[str(S)]+1,X[str(addition)])
    return X[str(list(G.nodes()))]
correct = 0
wrong = 0
output = ""
for i in range(5,10):
    G = nx.read_gpickle("data/graph"+'{0:03}'.format(i)+".gpickle")
    x = eppstein(G)
    if x != G.graph["Chromatic number"]:
        output += str(x)+" vs "+str(G.graph["Chromatic number"])+"\n"
        output += "WRONG:: test/graph"+'{0:03}'.format(i)+".gpickle\n"
        wrong += 1
    else:
        output += "RIGHT:: test/graph"+'{0:03}'.format(i)+".gpickle"+"\n"
        correct += 1

    with open('eppsteinOutput.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(output)
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
