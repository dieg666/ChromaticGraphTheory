import networkx as nx
import itertools as I
import utils
import time
import math
import sys
import grinpy as gp
def eppstein(G):
    X = {}
    for S in utils.subsets_of_graph(G):
        S2 = utils.createGraph(S, G)
        chromatic_number = gp.chromatic_number(S2)
        X[str(list(S2.nodes()))] = 999
        if chromatic_number <= 3:
            X[str(list(S2.nodes()))] = chromatic_number
    for S in utils.subsets_of_graph(G):
        if  3<= X[str(S)]:
            substraction = utils.diff(list(G.nodes()), S)
            S2 = utils.createGraph(substraction,G)
            limit = len(S) / X[str(S)]
            for I in utils.get_max_independent_set(S2):
                if len(I) <= limit:
                    addition = utils.add(S,I)
                    addition.sort()
                    X[str(addition)] = min(X[str(S)]+1,X[str(addition)])
    return X[str(list(G.nodes()))]

correct = 0
wrong = 0
output = ""

for i in range(1,150):
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
