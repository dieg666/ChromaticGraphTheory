import networkx as nx
import sys
import utils
def lawler(G):
    X = {}
    for S in utils.subsets_of_graph(G):
        #print("Actual S iteration: "+ str(S))
        # TODO check better naming of remove
        S2 = utils.createGraph(S,G)
        X[str(S2.nodes())] = len(S)
        for I in utils.get_max_independent_set(S2):
            substract = utils.diff(S,I)
            X[str(S)] = min(X[str(S)],X[str(substract)] + 1)
    return X[str(list(G.nodes()))]

correct = 0
wrong = 0
output = ""
for i in range(1,150):
    G = nx.read_gpickle("data/graph"+'{0:03}'.format(i)+".gpickle")
    x = lawler(G)
    if x != G.graph["Chromatic number"]:
        output += str(x)+" vs "+str(G.graph["Chromatic number"])+"\n"
        output += "WRONG:: test/graph"+'{0:03}'.format(i)+".gpickle\n"
        wrong += 1
    else:
        output += "RIGHT:: test/graph"+'{0:03}'.format(i)+".gpickle"+"\n"
        correct += 1

    with open('lawlerOutput.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        print(output)
