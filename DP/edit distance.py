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

def oneEditDistance(A, B):
    # insert, delete, replace
    n = len(A)
    m = len(B)
    
    if abs(m-n) > 1: return False

    if m < n:
        A, B = B, A
		# now we have only option on deletion and updation
    i = j = diff = 0

    while i<n and j<m:
        if A[i] != B[j]:
			
			# if already edited, 
            if diff: return False

			# mark edited = True
            diff = 1

			# if m==n then we can not delete, so just update and move.
            if m == n:
                i += 1
			#else:
				# just delete the element from A, i.e -> j

        else:
			# if equal, good to go.
            i += 1

        j += 1
    return True
        

A = 'pale'
B = 'padle'

