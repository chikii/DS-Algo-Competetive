# nCr under mod
def C(n,r,mod = 10**9+7):
  if r>n: return 0
  if r>n-r: r = n-r
  num = den = 1
  for i in range(r):
      num = (num*(n-i))%mod
      den = (den*(i+1))%mod
  return (num*pow(den,mod-2,mod))%mod

# nCr
def C(n,r):
  if r>n:
      return 0
  if r>n-r:
      r = n-r
  ans = 1
  for i in range(r):
      ans = (ans*(n-i))//(i+1)
  return ans