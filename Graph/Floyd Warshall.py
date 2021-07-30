# all pair shorted path Algorithm
# time  -> V^3
# space -> V^2

# IDEA -> we just check is there any shorter path to reach from u to v via K. for all u, v and for all K
#  -> we take each node as an intermediate node. and try to relax each edge.
        # relax edge => d[y] = min(d[y], d[x]+ w(x, y))


# graph is a matrix , 1 means there's a edge
                    # 0 no edge
def floydWarshell(graph):
    n = len(graph)
    int_max = float('inf')
    res = [[int_max]*n for i in range(n)]
    for i in range(n):
        res[i][i] = 0

    for K in range(n):
        shortestPathVia_K(K, graph, res)
    
    return res

def shortestPathVia_K(K, graph, res):
    n = len(graph)

    for i in range(n):
        for j in range(n):
            res[i][j] = min(res[i][j], res[i][K]+res[K][j])
    
    