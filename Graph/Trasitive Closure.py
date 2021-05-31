
# Time - > V^2
# space - V^2
# dfs is running over v.
# and curr is fixed

"""
Given a directed graph,
find out if a vertex j is reachable from another vertex i for all vertex pairs (i, j) in the given graph.
Here reachable mean that there is a path from vertex i to j. The reach-ability matrix is called the transitive closure of a graph.
"""

# dfs i done over second parameter.
# for each node, which is 1st parameter.
def dfs(curr, u):
    tc[curr][u] = 1

    for v in graph[u]:
        if tc[curr][v] == 0:
            dfs(curr, v)
        

def transitiveClosure():
    for i in range(n):
        dfs(i, i)


graph = {
    0:[1],
    1:[2],
    2:[3],
    3:[]
}
n = len(graph)
tc = [[0]*n for i in range(n)]
transitiveClosure()
for i in tc:
    print(i)