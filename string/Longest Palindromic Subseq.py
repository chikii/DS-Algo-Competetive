def solve(self, A):
    n = len(A)
    LPS = [[0]*n for i in range(n+1)]
    
    for Len in range(1, n+1): # length
        for start in range(n-Len+1):
            end = start+Len-1
        
            if start == end:
                LPS[start][end] = 1
            elif start+1 == end:
                if A[start] == A[end]:
                    LPS[start][end] = 2
                else:
                    LPS[start][end] = 1
            elif A[start] == A[end]:
                LPS[start][end] = LPS[start+1][end-1] + 2
            else:
                LPS[start][end] = max(LPS[start+1][end], LPS[start][end-1])

    return LPS[0][-1]
                