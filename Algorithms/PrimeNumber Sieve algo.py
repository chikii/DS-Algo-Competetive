
def enhanced_sieve(MAX): ## time complxity = O(2N)
    isprime = [True] * MAX
    prime = []  
    SPF = [-1] * (MAX)  # smallest prime factor
    outer_count = 0
    inner_count = 0

    for i in range(2, MAX):  
        outer_count += 1
        if isprime[i] == True:  
            prime.append(i)  
            SPF[i] = i  
        
        j = 0
        while (j < len(prime) and (i * prime[j]) < MAX and prime[j] <= SPF[i]): 
            inner_count += 1
            isprime[i * prime[j]] = False
            
            SPF[i * prime[j]] = prime[j] 
            j += 1

    print('Outer Loop Runs : ', outer_count, "times")
    print('inner Loop Runs : ', inner_count, "times")
    return prime    

def sieve(MAX):## time complxity = O(N * log(log(N)))

    isPrime = [True] * MAX
    outer_count = 0
    inner_count = 0
    prime = []
    for i in range(2, MAX):
        outer_count += 1
        if isPrime[i]:
            prime.append(i)
            for j in range(i*i, MAX, i):
                inner_count += 1
                isPrime[j] = False

    print('Outer Loop Runs : ', outer_count, "times")
    print('inner Loop Runs : ', inner_count, "times")
    return prime    



    
print('Sieve Algo : ')
print(sieve(100))

print('Enhanced Sieve Algo : ')
print(enhanced_sieve(100))