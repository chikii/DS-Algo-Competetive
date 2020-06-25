"""
QUESTION - Celebrity Problem
We have N persons in a room.
If a persons is known by everyone and he does not know anyone,
then he is celebrity.
Your task is to find celebrity in a room if any else print -1.
you can ask only - does A knows B ?

"""

def knows(A,B):
    if p[A][B] == 1:
        return True
    else:
        return False

n = 4
p = [[1,0,1,1],
     [1,1,1,1],
     [0,0,0,1],
     [0,0,0,1],
]

stack = []

for i in range(n):
    stack.append(i)

while len(stack) > 1:

    A = stack.pop()
    B = stack.pop()
    
    if knows(A,B):
        stack.append(B)
        # a is nt celeb
    else:
        stack.append(A)
        # b is not celeb
 

celeb = stack.pop()


#check whether everyone knows c or not
for i in range(n):
    if (knows(i,celeb) == False or knows(celeb,i) == True) and i != celeb :
        celeb = False
        break

if celeb:
    print('celebrity is ',celeb+1)
else:
    print(-1)


#time complexity - O(n)