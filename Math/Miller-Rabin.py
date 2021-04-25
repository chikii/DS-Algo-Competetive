
def binpow(a, d, n):
    """
    binary exponantion of a^d
    """
    res = 1
    while d:
        if d&1:
            res = (res*a)%n
        a = (a*a)%n
        d >>= 1
    return res

def check_composite(a, d, r, n):
    """
    True : if n is composite
    False: if n is prime
    """
    x = binpow(a%n, d, n)
    
    if x == 1 or x == n-1:
        return False
    
    for s in range(1, r):
        x = (x*x)%n
        if x == n-1:
            return False
    return True


def MillerRabin(n):
    """
    True : if n is Prime
    False: if n is composite
    """
    if n<2: return True
    
    for p in [2,3,5,7,11,13,17,19,23,29,61]:
        if n%p == 0: return n==p
    
    r = 0
    d = n-1
    while d&1 == 0:
        r += 1
        d >>= 1
    
    for a in [2,3,61]:
        if a == n: return True
        if check_composite(a, d, r, n):
            return False
    return True

def getNextPrime(n):
    while not MillerRabin(n):
        n += 1
    return n

n = 27
print(MillerRabin(n))