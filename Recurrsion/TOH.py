# Q) Tower of Hanoi
"""
towers -> A B C

if 1 disk is present only |  A -> B

if 2 disk is present |  A -> B
                        A -> C
                        B -> C

if 3 disk is present ->
    put N-1, from A , To B, using C
    put last disk from A ->  to C
    now, put N-1 , from B, to C, using A
"""

def TOH_path(N, src, dest, mid): # if needed to print path.
    if N == 1:
        print(src, '->', dest)
        return 1
    
    count = 0

    count += TOH_path(N-1, src, mid, dest)
    print(src, '->', dest)
    count += 1
    count += TOH_path(N-1, mid, dest, src)

    return count


def TOH(N): # if just need a minimum steps.
    dp = [0]*(N+1)
    dp[1] = 1
    for disk in range(2, N+1):
        dp[disk] = 2*dp[disk-1] + 1
    return dp[-1]


N = 5
print(TOH_path(N, 'A', 'C', 'B'))
print(TOH(N))
