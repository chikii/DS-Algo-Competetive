

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

def isCycle(edges):
    for u,v in edges:
        if findP(u) == findP(v):
            print('There is a cycle.')
            return True
        
        union(u,v)
    
    print('There is NO cycle.')
    return False

if __name__ == "__main__":
    n = int(input("Total no of vertex : "))        
    e = int(input("Total no of edges : "))        
    
    dsuf = []
    makeSet(n)

    graph = [[] for i in range(n+1)]
    edges = []
    print('Enter {} edges in format - vertex of connected edges..(u v)\n'.format(e))
    for i in range(e):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u,v))
    
    print(isCycle(edges))