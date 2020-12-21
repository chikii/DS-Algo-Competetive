def printValues():
    print('2-d grid : ->')
    for i in range(r):
        for j in range(c):
            print(a[i][j], end = '  ')
        print('\n')
    
    print('shortest path from src to every cell \n(-1 means cell is not reachable there using 1\'s path): ->')
    for i in range(r):
        for j in range(c):
            print(d[i][j], end = '  ')
        print('\n')
    

def valid(x,y): # this function will check all the edge cases.
    # like row is exceded or not so for column or 
    # there is 1 on this x,y  or not
    # return True if this will be the valid cell to explore else false.
    return x >= 0 and x < r and y >=0 and y < c and a[x][y] != 0 

def backTrack(crwal):

    path = [crwal]
    x,y = crwal
    while p[x][y] != -1:
        crwal = p[x][y]
        x,y = crwal
        path.append(crwal)
    
    return path[::-1]

"""
sample test case 

1 1 1 0
1 1 0 1
0 1 1 0
0 1 1 1

"""

# ---------------- main function 
r, c = map(int, input().split())
d = [[-1 for i in range(c)] for j in range(r)]
p = [[-1 for i in range(c)] for j in range(r)]
a = [0] * r

queue = []

for i in range(r):
    a[i] = list(map(int,input().split()))

# hacky thing
dx = [0,1] # go right
dy = [1,0] # go down

queue = [(0,0)]
d[0][0] = 0

print("Initial queu is :")
for i in range(len(queue)):
    print(queue[i], end= '->')

print('\n')
print('on each second we will go right and down adjacent cells of curr cell in queue (if not visited and valid.)')
while len(queue) != 0:

    u = queue[0]
    queue.remove(u)
    x,y = u
    for i in range(2):
        if valid( x+dx[i] , y+dy[i]) and d[x + dx[i]][y+dy[i]] == -1: 
            d[x + dx[i]][y+dy[i]] = d[x][y] + 1
            queue.append((x+dx[i] , y+dy[i]))
            p[x + dx[i]][y+dy[i]] = (x,y)
    
ans = d[r-1][c-1]
print("ANS --------->")
if ans == -1:
    print(f'Not reachable to using 1\'s path {r,c}')
else:
    print(f'Shortest distance to reach {r,c} from {1,1} using 1\'s path only is {ans}.')
    
    path = backTrack((r-1,c-1))
    for i in range(len(path)-1):
        print(path[i],end = '->')
    print(path[-1])
    
print("------------->")
print('\n')
printValues()