

def dfs(curr, par, graph):
    global time, disc, low

    child = 0

    disc[curr] = low[par] = time
    time += 1

    for adj in graph[curr]:
        child += 1

        #case 1
        # self edge
        if adj == curr: continue


        # case 2
        # if not visited:
        if disc[adj] == -1:
            dfs(adj, curr, graph)
            low[curr] = min(low[curr], low[adj])

            "for bridge"
            if low[adj] > disc[curr]:            
                 bridge.append([curr, adj])

            ' for Articulation point'
            if low[adj] >= disc[curr] and par == -1:
                ap[curr] = True
            
            if par == -1 and child > 1:
                ap[curr] = True
        
        # case 3 - back edge
        # adj node is not a parent node. why this. because we are consedering low as curr and we do not want child->parent relationship.
        elif adj != par:
            # focus here, we are considering low of curr.
            low[curr] = min(low[curr], disc[adj])
            # if we take par in consideration, then it will be a child->parent relationship.







graph = {}
n = len(graph)
disc = [-1]*n  # discovevry time of curr node
low = [-1]*n   # lowest discovery time node reachable from curr node
time = 1
bridge = []
ap = [False]*n # articulation point


for i in range(n):
    if disc[i] == -1:
        dfs(i, -1)
