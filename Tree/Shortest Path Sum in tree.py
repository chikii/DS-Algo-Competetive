# shortest path (u,v) in TREE is path going through LCA

def dfs(src, par):
    for v in graph[src]:
        if v != par:
            p[v] = src
            depth[v] = depth[src] + 1 
            sum_from_root[v] = sum_from_root[src] + weight[v]
            dfs(v,src)

def lca(u,v):

    if u == v:
        return u
    
    if depth[u] == depth[v]:
        u = p[u]
        v = p[v]
        return lca(u,v)
    
    if depth[u] > depth[v]:
        return lca(p[u],v)
    
    return lca(u,p[v])

if __name__ == "__main__":
    V,Q = map(int, input().split())
    weight = list(map(int, input().split())) # weight assign to each node

    graph = [[] for i in range(V+1)]

    for i in range(V-1):
        u,v = map(int, input().split())
        u,v = u-1,v-1
        graph[u].append(v)
        graph[v].append(u)
    
    # intializing
    p = [0]*V
    sum_from_root = [0]*V
    depth = [0]*V

    # base condition
    p[0] = -1 
    sum_from_root[0] = weight[0]
    depth[0] = 0

    dfs(0,-1)

    for q in range(Q):
        u,v = map(int, input().split())
        u,v = u-1,v-1

        lca_ = lca(u,v)

        ans = sum_from_root[u] + sum_from_root[v] - 2*sum_from_root[lca_] + weight[lca_]
        print(ans)