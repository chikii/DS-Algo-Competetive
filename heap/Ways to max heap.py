import math

memo = [-1]*101
def MAX_heap(self, N):
    if N<= 2: return 1
    if self.memo[N] != -1:
        return self.memo[N]
    
    H = int(math.log2(N))
    p = (1<<H)-1
    L = (p-1)//2 + min(N-p, (p+1)//2)
    R = N-1 - L
    
    self.memo[N] = nCr(N-1, L) * self.solve(L) * self.solve(R)
    
    self.memo[N] %= mod
    
    return self.memo[N]
	    
def nCr(n,r):
  if r>n:
      return 0
  if r>n-r:
      r = n-r
  ans = 1
  for i in range(r):
      ans = (ans*(n-i))//(i+1)
  return ans
    
mod = int(1e9)+7