def dfs(u, graph, visited, par, depth, level):

    for adj in graph[u]:
        if not visited[adj]:
            visited[adj] = True
            par[adj] = u
            depth[adj] = depth[u]+1
            level[adj] = level[u]+1
            dfs(adj, graph, visited, par, depth, level)


from queue import Queue
import queue
def bfs(src, graph):
    # pre processing

    n = V # no of vertex
    visited = [False]*n
    dist = [int_max]*n
    par = [-1])*n
    que = Queue(maxsize=n)


    que.put(src)            # **** remember
    dist[src] = 0           # **** remember
    visited[src] = True     # **** remember

    while que.empty():
        curr_node = que.get()

        for adj in graph[curr_node]:
            if not visited[adj]:
                que.put(adj)  # *** remember to put in que
                visited[adj] = True # *** remmenber to mark visited
                dist[adj] = dist[curr_node]+1
                par[adj] = curr_node
            





