# we check whether the node is in visited stack or not by using graph coloring
# white- > not visited
# gray -> in visiting stack
# black -> visited

## NOTE : a -> b , represent a is dependent to b.

white = 1
gray = 2
black = 3

def dfs(curr):

    global isCycle

    if isCycle: return

    color[curr] = gray # change color to visiting

    for adj in graph[curr]:
        if color[adj] == white: # if unvisited 
            dfs(adj) # visit
        elif color[adj] == gray: # if it is already in visiting stack. it means there is a cycle
            isCycle = True
            return
    
    color[curr] = black # visiting complete color to black.
    topological_sort_order.append(curr) # add to sorted order.

num_of_nodes = 5
isCycle = False
graph = {}
topological_sort_order = []
color = {node: white for node in range(num_of_nodes)} # initally every node is of white color

for node in range(num_of_nodes):
    if color[node] == white:
        dfs(node)

if isCycle:
    print('there is a cycle in dependencies.')
else:
    print('topological sort order is ', topological_sort_order)

