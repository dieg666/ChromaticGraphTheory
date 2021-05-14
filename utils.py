from itertools import combinations
import networkx as nx
import grinpy as gp

def get_independent_set(G):
    n = G.number_of_nodes()
    a = G.nodes()
    comb = []
    l = []
    for i in range(1,G.number_of_nodes()+1):
        comb += list(combinations(a, i))
    for c in comb:
        if(gp.is_independent_set(G, list(c))):
            l.append(list(c))
    return l

def get_max_independent_set(G):
    S = get_independent_set(G)
    MIS = []
    for i in range(len(S)):
        if len(S[i]) == len(S[-1]):
            MIS.append(S[i])
    return MIS
