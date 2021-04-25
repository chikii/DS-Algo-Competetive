# time complexity = pow(2,N)*N

def solve1(): #if this type of data
    arr = ['A','B','C','D']


    for _ in range(int(input('test case : '))):
        n = int(input('N :(1-4) :'))
        total = 1<<n #this means pow(2,N)

        for mask in  range(0,total):
            for i in range(n):
                F = 1<<i 

                if F&mask != 0:
                    print(arr[i],end= ' ')
            
            print()

def solve2(): #if this type of data
    P = 2
    Q = 3
    R = 4
    tot = 1<<3
    for mask in range(tot):
        #if we have limited data we can do manually without looping
        if mask & 1 != 0:   # 1 is F = 1<<0 when i is 0
            print(P,end = ' ')
        if mask & 2 != 0:
            print(Q,end = ' ')
        if mask & 4 != 0:   # 4 is F = 1<<3 when i is 3
            print(R,end = ' ')
        
        print()

        
print('solve 1 -->')
solve1()
print('solve 2 -- >')
solve2()