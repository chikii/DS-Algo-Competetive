# we have a 2d grid i which a bombb is  placed x,y i.e a[x][y] = 1 else all a[][] = 0
# you have to find bomb in q query
# you can ask query is a[i][j] contain bomb or not?
# ans would be - found, left, right, upper,down,upper-left,upper-right,down-left, down-right respective to the bomb position in grid,

def bomb_squad(starti, endi, startj, endj):
    global query
    global a
    
    midi = (starti+endi)//2
    midj = (startj+endj)//2

    if starti == endi and startj == endj:
        query += 1
        pos = input()
        if a[midi][midj] == 1:
            return 'Bomb Defused', query    
        else:
            return 'Bomb not Found', query

    print(midi,midj)
    query += 1
    pos = input()
    if pos == 'found': 'bomb found'
    if a[midi][midj] == 1:
        return 'Bomb Defused', query

    if pos == 'left':
        endj = midj
        endi = midi
        starti = endi
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)
    if pos == 'right':
        starti = midi
        startj = midj
        endi = midi
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)
    if pos == 'upper':
        endi = midi
        endj = midj
        startj = midj
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)
    if pos == 'down':
        starti = midi
        startj = midj
        endj = midj
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)
    if pos == 'upper-left':
        endi = midi
        endj = midj
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)
    if pos == 'down-right':
        starti = midi
        startj = midj
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)
    if pos == 'upper-right':
        startj = midj
        endi = midi
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)
    if pos == 'down-left':
        starti = midi
        endj = midj
        print(starti,endi, startj,endj)
        return bomb_squad(starti,endi,startj,endj)



a = [[0 for i in range(10)] for i in range(10)]
a[1][7] = 1 # bomb placed
print(a)

query = 0
starti = 0
startj = 0
endi = len(a)
endj = len(a[0])
result, query_need = bomb_squad(starti,endi,startj,endj)
print(result, query)