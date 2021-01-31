# in this algorithm, we will take care of incomming edges
"""
if incomming edges is = 0
it means we have no dependencies left. and we can add this in our queue to visit this.
this implement by using BFS
"""
## NOTE : a -> b , represent b is dependent to a.

in_degree = {}
for dependecy, src in pre_requisites:
    graph[src].append(dependecy)
    in_degree[dependecy] = in_degree.get(dependecy, 0) + 1

pre_requisites = [
    [a,b],
    [c,a],
    [d,b], [d,c], [d,e]
]
    """
    a <- b
   ,|,  ,|,
    c -> d <- e
    
    graph[a] = [c]    | indegree[a] = 1
    graph[b] = [a,d]  | indegree[b] = 0
    graph[c] = [d]    | indegree[c] = 1
    graph[d] = []     | indegree[d] = 3
    graph[e] = [d]    | indegree[r] = 0

    """

def bfs():

    queue = []
    topological_sort = []

    for node,  inDegree in in_degree.items():
        if inDegree == 0:
            queue.append(node)
    
    while len(queue) != 0:
        node = queue.pop(0)

        topological_sort.append(node)

        for adj in graph[node]:
            inDegree[adj] -= 1
            if inDegree == 0:
                queue.append(adj)
        
    if len(topological_sort) == no_of_nodes:
        return topological_sort, 'order'
    
    return 'there is a cycle'

