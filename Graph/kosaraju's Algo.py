# idea ->
# 1) dfs, once node completly visit append in stack.
# 2) compute transpose of graph
# 3) run dfs over stack.


def fill_stack(curr):

    for adj in graph[curr]:
        if not visited[adj]:
            visited[adj] = True
            fill_stack(adj,stack)
    
    stack.append(curr)


def dfs(curr):
    print(curr, end='->')
    for adj in graph_transpose[curr]:
        if not visited[adj]:
            visited[adj] = True
            dfs(adj)

from collections import defaultdict as dd
def transpose(graph):
    graph_transpose = dd(list)

    for u in graph:
        for v in graph[u]:
            graph_transpose[v].append(u)
    
    return graph_transpose

def kosaraju(graph, n):

    visited = [False]*n
    stack = []
    for i in range(n):
        if not visited[i]:
            fill_stack(i, stack)
    
    graph_transpose = transpose(graph)

    visited = [False]*n
    
    while stack:
        head = stack.pop()
        if visited[head]: continue

        print('Strongly Connected Component -> ')
        dfs(head)
        print()
    
    