from queue import Queue

class Graph:

    def __init__(self, n) -> None:
        self.vertices = n
        self.graph = [[] for i in range(n)]

        self.src_visited = [False]*n
        self.dest_visited = [False]*n

        self.src_par = [-1]*n
        self.dest_par = [-1]*n

        self.src_dist = [-1]*n
        self.dest_dist = [-1]*n

        self.src_que = Queue()
        self.dest_que = Queue()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, direction):

        if direction == 'forward':
            current = self.src_que.get()

            for adj in self.graph[current]:
                if not self.src_visited[adj]:
                    self.src_visited[adj] = True
                    self.src_par[adj] = current
                    self.src_dist[adj] = self.src_dist[current]+1
                    self.src_que.put(adj)
        else:
            current = self.dest_que.get()

            for adj in self.graph[current]:
                if not self.dest_visited[adj]:
                    self.dest_visited[adj] = True
                    self.dest_par[adj] = current
                    self.dest_dist[adj] = self.dest_dist[current]+1
                    self.dest_que.put(adj)
    
    def bbfs(self, src, dest): # bidirection_bfs
        if src == dest:
            print('path : ', src)
            print('dist : ', 0)
            return

        self.src_que.put(src)
        self.src_visited[src] = True
        self.src_dist[src] = 0

        self.dest_que.put(dest)
        self.dest_visited[dest] = True
        self.dest_dist[dest] = 0

        while not self.src_que.empty() and not self.dest_que.empty():

            self.bfs('forward')
            self.bfs('backward')

            intersect = self.is_intersect()

            if intersect != -1:
                self.print_path(src, intersect, dest)
                return
        
        print('path do not exist.')
        return -1

    def is_intersect(self):

        for i in range(self.vertices):
            if self.src_visited[i] and self.dest_visited[i]:
                return i
        return -1
    
    def print_path(self, src, intersect, dest):

        path = []

        path.append(intersect)

        i = intersect
        while i != src:
            path.append(self.src_par[i])
            i = self.src_par[i]
        
        path = path[::-1]

        i = intersect
        while i!=dest:
            path.append(self.dest_par[i])
            i = self.dest_par[i]
        
        path = list(map(str, path))
        print('path from src to dest : ', end = '')
        print(' '.join(path))
        print('dest - ', end= '')
        d = self.src_dist[intersect] + self.dest_dist[intersect]
        print(d)


# for graph - refer - https://www.geeksforgeeks.org/bidirectional-search/
n = 15
graph = Graph(n)
edges = [(0,4), (1,4), (4,6),(2,5), (3,5), (5,6), (6,7), (7,8), (8,9), (8,10), (9,11), (9,12), (10,13), (10,14)]

for edge in edges:
    u, v = edge
    graph.add_edge(u, v)

graph.bbfs(0, 14)


