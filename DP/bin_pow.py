
fun_call = 0

def power(a,n): # reccur
    global fun_call

    fun_call += 1
    
    if n == 0:
        return 1
    if n == 1:
        return a

    if n%2 == 0:
        dp[n//2] = power(a,n//2)
        dp[n] = dp[n//2]*dp[n//2]
    else:
        dp[n] = power(a,n-1)*a
    
    return dp[n]


def powerIter(a,b): # iterative
    res = 1
    while b>0:
        if b&1:
            res = res*a

        b = b>>1
        a = a*a
    
    return res


n = 12
a = 2
# find a^n
dp = [0]*(n+1)
ans = power(a,n)
print(fun_call)
print(ans)

# n = 12
#2^12 -> 2 * 2 * 2 * 2 * .... 12 times --> O(N)

13 12*1
2^13 -> 2^12 * 2^1 -> 2^(12+1) -> 2^13


"""
# Approch 2

2^12 = 2^6 * 2^6  
2^6  = 2^3 * 2^3  
2^3  = 2^1 * 2^1 * 2 
2^1  = 2

O(log(N))
"""