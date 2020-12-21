n = int(input()) # no of node
e = int(input()) # no of edge

import math
d = [math.inf] * n
# d[i] -> distance of i node from src.

graph = [[] for i in range(n)]

for i in range(e):
    u,v,w = map(int, input().split()) # edge and its wieght
    graph[u-1].append((v-1, w))
    graph[v-1].append((u-1, w))

print(graph)
print('\n')


# djikstra
import heapq

def djikstra(src):

    visited = [False] * n

    h = []
    heapq.heappush(h,(0,src))

    d[src] = 0 # mark the dist from src to src is 0
    
    
    while not all(visited):  # wile all node is not visited.
        dist_till_node, node = heapq.heappop(h)      # pop the minimimum distance node.
        if visited[node] : continue # if it is visited continue
        visited[node] = True        # else mark it visited
        for v,edge_wieght_from_node_to_v in graph[node]:     # for all adj node of minimum distance node
            if not visited[v]:
                if d[v] > dist_till_node + edge_wieght_from_node_to_v:
                    d[v] = dist_till_node + edge_wieght_from_node_to_v
                    heapq.heappush(h,(d[v],v))

#-------------------------------------------------------------->


src = int(input("For wich node you want to find shortest path to all nodes. : "))

djikstra(src-1)

for i in range(n):
    print(f'Shortest Distance from {src} to {i+1} : {d[i]}')
