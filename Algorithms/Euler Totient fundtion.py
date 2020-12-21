"""
# Euler totient funtion -> return the count of number from 1..n which are coprimes with n. i.e. gcd(i,n) = 1
ex. -> n = 4
phi(4) = ?
ans->
gcd(1,4) = 1 -> count+1
gcd(2,4) = 2
gcd(3,4) = 1 -> count+1
gcd(4,4) = 4

ans = 2

refernece-> https://www.youtube.com/watch?v=d5FlCz4nRiU&ab_channel=CodeBuddyOfficial
"""



# basic idea
def phii(n): # O(Nlog(log(n)))

    # assume intitally all are co-primes with n
    co_prime = [True]*(n+1)
    co_prime[0] = False
    co_prime[1] = True

    for i in range(2,n+1):

        # if a no diveds n then, all its multiple(upto n) will also divide n.
        if n%i == 0: 
            j = 1
            while i*j <= n:
                co_prime[i*j] = False
                j += 1
    
    
    return sum(co_prime)


def build_phi(n): # O(Nlog(log(n)))
    phi = [i for i in range(n+1)]

    phi[1] = 1 # base

    # using sieve approch.

    for i in range(2,n+1):

        if i != phi[i] : 
            continue
            # already check

        # we will check only for prime no.
        j = 1
        while i*j<=n:
            phi[i*j] = phi[i*j] - (phi[i*j]//i)
            j += 1
    print(phi)
    return phi

if __name__ == "__main__":
    n = 10
    query = 5
    
    # phie[i] -> no of count from 1..n which are coprimes with n. i.e. gcd(i,n) = 1
    phi = build_phi(n)

    for i in range(query):
        q = int(input(f"enter a no. upto {n} : "))
        print(phi[q])  # O(1) -> Total will O(query * 1)
        print(phii(q)) # O(Nlog(log(n))) -> Total will O( query * q*log(log(q)) )





