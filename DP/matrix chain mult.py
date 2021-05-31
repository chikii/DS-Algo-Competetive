# Q) Minimum cost of reducing Array by merging any adjacent elements repetitively
# Q) Matrix chain multiplication...

# Input: arr[] = { 6, 4, 4, 6 } 
# Output: 40 


def solve(A):
    n = len(A)

    dp = [[0]*(n+1) for i in range(n+3)]

    for i in range(1, n+1):
        dp[i][i] = A[i-1]
    
    prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1]+A[i])

    
    for p in range(1, n+1):
        for k in range(1, n+1-p):
            i = k
            j = k+p

            if i == j-1:
                dp[i][j] = dp[i][i]+dp[j][j]
                continue
            
            dp[i][j] = float('inf')
            sum_ = prefix[j] - prefix[i-1]

            # breaking  at each point
            # i...c | c+1.....j
            # and then the cost adding those part will adding those as one, and thier entire sum(i...j)
            for c in range(i, j):
                left = dp[i][c]
                right = dp[c+1][j]
                dp[i][j] = min(dp[i][j], left+right+sum_ )
        
    for i in dp:
        print(i)
    return dp[1][n]

A = [3, 2, 4, 1]
A = [6,4,4,6]
solve(A)

            