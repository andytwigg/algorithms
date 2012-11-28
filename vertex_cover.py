import utils

# vertex cover
# 2-approx: every vertex cover must include at least one endpoint of each edge
# in the below, no 2 edges selected share a vertex
# so |C_opt| >= #selected edges
# in the below, we return a cover of size 2*#selected edges <= 2*|C_opt|

def vertex_cover(G):
    # G is adjacency list
    n=len(G)
    C=[]
    V=range(n)
    while (len(V)>0):
        u=V[0]
        v=G[u][0]
        V.remove(u)
        V.remove(v)
        C.add(u)
        C.add(v)
    return C
	