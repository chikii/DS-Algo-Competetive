# MO's Algorithm - arranging asked query in such way that it cost only root(N) to access all query.


# question- range (L,R) will be given in each q queries output total distinct element in that range.

# brute force - Traverse each range of q queries - TIME COmplexity - O(N*Q)

# Optimized Approch -> MO's Algo

a = [0]+[4,5,2,2,1,5,9,8,2,3] # 1 based indexing
n = 10 

import math

n_sqrt = math.sqrt(n)


q= int(input())

# freuqcy counter
freq = {}
# ans count for each query
count = 0

def add(pos): #adding elemnet in freq
    freq[a[pos]] += 1
    global count
    if freq[a[pos]] == 1: # adding 1 in ans only when count increses from 0 to 1 . hence it will be in range (L,R)
        count += 1

def remove(pos):
    global count
    if freq[a[pos]] == 0 :
        return
    freq[a[pos]] -= 1 
    if freq[a[pos]] == 0 : # removing 1 in ans when freq become 0 for element
        count -= 1

currentl = 0
currentr = 0

for i in a: # setting intial freq to 0
    freq[i] = 0



#-----------------------------MO's Algo---------------------->
queries = []
for _ in range(q):
    l,r = map(int, input().split())
    queries.append((l//n_sqrt, r, l)) # SQRT DECOMPOSITION OF array (l/sqrt(n) , r)

print(queries)
#[(0.0, 3), (0.0, 10), (2.0, 10), (1.0, 8), (0.0, 10)]
queries.sort(key= lambda x: (x[0],x[1])) # sorting with l/sqrt(n) if ties then with r
#[(0.0, 3), (0.0, 10), (0.0, 10), (1.0, 8), (2.0, 10)]
print(queries)
for q in range(len(queries)):
    s,r,l = queries[q]
    queries[q] = (l,r) # converting it into actual formate

print(queries)
#--------------------------------------------------->
# now queries are arrange optimally ---------------->



#processing each query
for q in queries:
    l,r = q

    while currentl < l:
        remove(currentl)
        currentl += 1
        if l == currentl:
            add(currentl)
    while currentl > l:
        currentl -= 1
        add(currentl)
    while currentr < r:
        currentr += 1
        if currentr > currentl:
            add(currentr)
    while currentr > r:
        remove(currentr)
        currentr -= 1
   
    print(f'distinct element for range {l} AND {r}', count)