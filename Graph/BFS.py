# bfs works with unwieghted graph. in unwieghted graph we assume distance to adjacent node is 1.

# bfs gives the all pair shortest path from src. (works well only with unwieghted graphs)


from queue import deque
def bfs(src,desti):

    visited = [False]*(n+1)  # we maintain a visited array.

    queue = deque([src])
    d[src] = 0 # distance froms rc to src is 0
    visited[src] = True # mark src visited

    bfsTree = []
    while len(queue) != 0:
        
        node = queue.popleft() # took the oldest elemnt of queue (whihc is the 1st element) and process it.
        #visited[node] = True  ## This should be done down only if done here instead of downwards then time complexity will increase
        bfsTree.append(node)
        for v in graph[node]:
            if not visited[v]: # if node is not visited 
                queue.append(v)   # append in queue. 
                d[v] = d[node]+1  # and increase the distance by 1 with its adjenct node.
                visited[v] = True # and make the node visited .. this is most imp must be done here only.
                p[v] = node
            if v == desti:
                printTree(bfsTree)
                return True
    printTree(bfsTree)
    return False

def backTrack(crawl):

    path = [crawl]

    while p[crawl] != -1:
        crawl = p[crawl]
        path.append(crawl)

    return path[::-1]

def printTree(tree):
    print('These are breath first search and distance of node from src to destination.\n make tree urself you aalsi.')
    print(tree)
    print(d[1:])
    


# ------------------------------main -------------------
n = int(input('No of vertecies - '))
e = int(input('no of edges - '))

graph = [[] for i in range(n+1)]

d = [-1] * (n+1)
# d[i] -shortest distance of i from src.

p = [-1] * (n+1)
# p[i] - parent of i in BFS tree.
for i in range(e):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

src = 1
desti = 7

if bfs(src,desti):
    path = backTrack(desti)
    print(f'Shortest path from {src} to {desti} - ')
    for i in range(len(path)-1):
        print(path[i], end='->')
    print(path[-1])
    print('of Distance :',d[desti])
else:
    print('Given Source and destination are not connencted.')

"""
# sample graph

    1---2     6
    |  /| \ / 
    | / |  5
    |/  | / \ 
    3---4     7


# most important things.
->before starting while len(queue) != 0 loop
    1. append src in queue 
    2. make d[src] = 0
    3. mark visited[src] = True
"""