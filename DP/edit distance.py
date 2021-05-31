def minDistance(self, A, B):
	    src_len = len(A)
	    dest_len = len(B)

	    # think you have only string till i, now what you do to match the curr char of destination string,
	   # i -> denoting dest string
	   # j -> denoting src string
       # -1 -> go one back in curr string

	   # if insert, [dest-1][src] + insert cost
	   # if delete, [dest][src-1] + delete cost
	   # if update, [dest-1][src-1] + update cost
	    
	    cost = [[0]*(src_len+1) for i in range(dest_len+1)]
	    
	    for i in range(dest_len+1):
	        for j in range(src_len+1):
	            if i == 0 or j == 0: 
	                cost[i][j] = j + i
	            elif B[i-1] == A[j-1]:
	                cost[i][j] = cost[i-1][j-1]
	            else:
	                cost[i][j] = min(cost[i-1][j], cost[i][j-1], cost[i-1][j-1])+1
	    return cost[-1][-1]
