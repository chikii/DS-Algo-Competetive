"""
given a array 
find the maximum of contineous sub seq of size k
ex. for A = [10,5,3,2,7,1,5,2,8,1] and  k = 3
ans = [10,5,7,7,7,5,8,8]
""" 
#InVariance = d[i] > d[i+1]

from collections import deque

def isEmpty(d):
    if len(d) == 0:
        return True
    else:
        return False

def push(i):
    while not isEmpty(d):
        if d[-1][0] < A[i]:
            d.pop()
        else:
            break
    d.append([A[i],i])

def query(l,r):
    while not isEmpty(d):
        if d[0][1] < l:
            d.popleft()
        else:
            break
    return d[0][0]

d = deque()

A = [10,5,3,2,7,1,5,2,8,1]
k = 3

for i in range(k):
    push(i)

l = 0 
r = k-1
print(query(l,r),end= ' ')
for r in range(k,len(A)):
    l += 1
    push(r)
    print(query(l,r),end = ' ')
