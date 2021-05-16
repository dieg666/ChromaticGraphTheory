from itertools import combinations
import networkx as nx
import grinpy as gp
def diff(S,I):
    ## S - I
    l = []
    for s in S:
        if s not in I:
            l.append(s)
        return l
def add(S,I):
    l = []
    for s in S:
        l.append(s)
    for i in I:
        if not i in l:
            l.append(i)
    return l

def createGraph(S,G):
    G2 = G.copy()
    for i in range(G.number_of_nodes()):
        if not i in S:
            G2.remove_node(i)
    return G2
def index_graph(G,L):
    if (L == []):
        return 0
    L.sort()
    s = subsets_of_graph(G)
    index = s.index(L)
    return index
def subsets_of_graph(G):
    a = G.nodes()
    comb = [[]]
    l = []
    for i in range(1,G.number_of_nodes()+1):
        comb += list(combinations(a, i))
    for c in comb:
        l.append(list(c))
    return l
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
