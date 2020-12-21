def printValues():
    print('2-d grid : ->')
    for i in range(r):
        for j in range(c):
            print(a[i][j], end = '  ')
        print('\n')
    
    print('shortest path from all initial floods point to every cell \n(-1 flod is not reachable there. or there is a wall): ->')
    for i in range(r):
        for j in range(c):
            print(d[i][j], end = '  ')
        print('\n')


def valid(x,y): # this function will check all the edge cases.
    # like row is exceded or not so for column or 
    # there is wall on this x,y  or not
    # return True if this will be the valid cell to explore else false.
    return x >= 0 and x < r and y >=0 and y < c and a[x][y] != '#' 

"""
sample input
4 4
. . . #
. F . #
F . # P
. . . .
"""


#---------------------------------------------code starts here ------------------------------------->
r, c = map(int, input().split())
d = [[-1 for i in range(c)] for j in range(r)] # setting initial destance to -1
a = [0] * r

queue = []

for i in range(r):
    a[i] = input().split()
    for j in range(c):
        if a[i][j] == 'F':
            queue.append((i,j)) # making dummy node.  # most imp things
            # work similar like dummy node.
            # suppose we created dummy node and add with all floods cell with 0 distance
            # so on exploring dummy node it will push all floods cell in queue.. this is what we do here as well ...
            # also a hacky thing.
            d[i][j] = 0 # most imp things
        elif a[i][j] == 'P':
            desti = (i,j)
        else: 
            #/.
            continue

dx = [1,-1,0,0] #
dy = [0,0,1,-1] # hacky thing


print("Initial queu is :")
for i in range(len(queue)):
    print(queue[i], end= '->')
print('\n')
print('on each second we will put all four adjacent cells of flood in queue (if not visited and valid.)')
while len(queue) != 0:

    u = queue[0]
    queue.remove(u)
    x,y = u
    for i in range(4): # in all four direction x+1, X-1, y+1, y-1,, if d[][] not -1 means already visisted. (here distance is used as visited array)
        if valid( x+dx[i] , y+dy[i]) and d[x + dx[i]][y+dy[i]] == -1: 
            d[x + dx[i]][y+dy[i]] = d[x][y] + 1
            queue.append((x+dx[i] , y+dy[i]))

    #on each second we will put four cell in queue (if not visited and valid.)
    print(queue)

ans = d[desti[0]][desti[1]] # our ans will be the shortest distance (which is the (second in time)) of our destination
print("ANS --------->")
if ans == -1:
    print('Flood Can not hit person. He is surrounded by wall.')
else:
    print(f'Flood will hit person in {ans} seconds.')
print("------------->")
print('\n')
printValues()


"""
# most important things.
->before starting while len(queue) != 0 loop
    1. append src in queue 
    2. make d[src] = 0
    3. mark visited[src] = True

-> update dx dy according to need.
-> explore only those nodes which are neccasary.
-> remember you don't need to make a graph in 2-d BFS.
there is most of the time the way to solve using grid itself. (ex flood hit person, taking 1's path to reach end of grid.)
"""