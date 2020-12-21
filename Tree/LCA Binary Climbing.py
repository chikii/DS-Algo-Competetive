## Q. To Find Lowest Common Ancestor(LCA) 
## Approch - Binary Climbing


t = int(input())
LOGN = 22

for _ in range(t):
    n,q = map(int,input().split())
    adj = [[] for i in range(n+1)] # adjecency list. (maintain all the edges)


    p = [[0 for i in range(LOGN)] for j in range(n+1)]
    # p[u][i] = 2^i th parent of u node
    # example - p[1][0] - 2^0 th parent of 1st node. 

    h = [0]*(n+1)
    # h[u] = hieght of u from root.

    #xor_from_root = [0]*(n+1) # for specific question

    a = [0]+list(map(int,input().split())) # value of node
    
    for i in range(1,n):
        u,v = map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)

    dfs(1,0,a[1]) # running dfs to find hieghts of all nodes.


    # to find all 2^i th parent of all nodes.
    # this works in this way.
    # 1. we find 2^1 th parent of all node then 2^2 of all node then goes on.
    # remember interchange of these 2 loop wont work
    # and we are starting 1st loop with 1. hence 2^0 is already found in dfs.
    for i in range(1,LOGN):
        for u in range(1,n+1):
            p[u][i] = p[p[u][i-1]][i-1]

    for i in range(q):
        u,v = map(int,input().split())
        #ans = xor_from_root[u] ^ xor_from_root[v] ^ a[lca(u,v)]
        print(lca(u,v))



def lca(u,v):

    if h[u] > h[v] : u,v = v,u

    diff = h[v]-h[u]
    for i in range(LOGN):
        if (diff & 1 << i)  != 0: # breaking diff in terms of power of 2 # binary hack for doing these
            #print(f'2^{i} parent of {v} is {p[v][i]}')
            v = p[v][i] # 2^1 th parent of v = 2
    
    # now height is same
    if u == v : return u

    
    for i in range(LOGN-1,-1,-1):
        if p[u][i] != p[v][i]:
            u = p[u][i]
            v = p[v][i]

    # conjection -> we will just one step away from lca.
    lca_ = p[u][0]
    return lca_

def dfs(u,prv:
    h[u] = h[prv]+1
    p[u][0] = prv
    for v in adj[u]:
        if v==prv: continue
        dfs(v,u)


# any operation canbe performed instead xor using binary climbing
"""
visited = [False]*(V+1)
visited[1] = True
def dfs(u, prev):
    h[u] = h[prev]+1
    p[u][0] = prev
    val[u][0] = A[u]

    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v,u)


dfs(1,0)

for i in range(1,LOGN):
    for j in range(V+1):
        #first_half = p[j][i-1]
        #second_half = p[first_half][i-1]
        #p[j][i] = second_half
        p[j][i] = p[p[j][i-1]][i-1]

        # to get xor of path
        val[j][i] = val[j][i-1] ^ val[p[j][i-1]][i-1]

        # to get sum of path
        # jump1 = val[j][i-1]
        # jump2 = val[p[j][i-1]][i-1]
        # val[j][i] = jump1+jump2

def lca(u,v):
    ans = 0

    if h[u] > h[v]:
        u,v = v,u

    diff = h[v] - h[u]
    for i in range(LOGN):
        if diff & (1<<i):
            ans ^= val[v][i]
            v = p[v][i]

    if u==v: return u, ans+A[u]

    for i in range(LOGN-1, -1, -1):
        if p[u][i] != p[v][i]:
            ans  = ans ^ val[u][i] ^ val[v][i]
            u = p[u][i]
            v = p[v][i]
    
    lca = p[u][0]
    ans = ans ^ val[u][0] ^ val[v][0] ^ val[lca][0]
    return lca, ans

"""