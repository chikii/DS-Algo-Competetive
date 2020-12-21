# Krushkal algo is used to find minimum spanning tree. 
# Time -> O(ElogE + ElogV)
#             |      |
#          to sort   find and union op. 
#           edges     for each edge

# we can also find maximum spanning tree by multiplying each wieght with -1.

def Krushkal(edges):

    mst = []

    edges.sort() # sort the edges

    j = 0
    edges_include = 0
    while edges_include < V-1 and j < len(edges):
        edge = edges[j]

        u = edge[1][0]
        v = edge[1][1]

        if findP(u) == findP(v): # on including this edge if graph makes a cycle
            j += 1 # skip edge
            continue
        # else

        union(u,v) # combine them

        # edge = (edge[0]*-1,edge[1]) > for maximum spanning tree. converting into positive again.

        mst.append(edge) # add edge in MST

        edges_include += 1
        j += 1
    
    return mst

class node():
    def __init__(self, parent = -1, rank = 0):
        self.parent = parent
        self.rank = rank

def findP(v):
    if dsuf[v].parent == -1 : return v

    dsuf[v].parent = findP(dsuf[v].parent)

    return dsuf[v].parent

def union(u,v):
    p_u = findP(u)
    p_v = findP(v)

    if dsuf[p_u].rank < dsuf[p_v].rank:
        dsuf[p_u].parent = p_v
    elif dsuf[p_v].rank < dsuf[p_u].rank:
        dsuf[p_v].parent = p_u
    else:
        dsuf[p_u].parent = p_v
        dsuf[p_v].rank += 1

def makeSet(n):
    for i in range(n+1):
        dsuf.append(node())

if __name__ == "__main__":
    V = int(input("Total no of vertex : "))        
    E = int(input("Total no of edges : "))        
    
    dsuf = []
    makeSet(V)

    graph = [[] for i in range(V+1)]
    edges = []
    print('Enter {} edges in format - vertex of connected edges..(u v) and w (wieght)\n'.format(e))
    for i in range(E):
        u,v,w = map(int, input().split())
        graph[u].append((w,v))
        graph[v].append((w,u))
        edges.append((w,(u,v)))
        # edges.append((-1*w,(u,v))) -> to find maximum spaning Tree
    
    print(Krushkal(edges))