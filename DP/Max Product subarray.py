def maxProduct(self, A):
    n = len(A)
    max_prod = A[0]
    min_prod = A[0]
    
    ans = A[0]
    
    for i in range(1, n):
        
        choice1 = max_prod*A[i]
        choice2 = min_prod*A[i]
        
        max_prod = max(choice1, choice2, A[i])
        min_prod = min(choice1, choice2, A[i])
        
        ans = max(ans, max_prod)
    
    return ans