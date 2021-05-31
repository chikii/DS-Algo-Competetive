def oneAway(A, B):
    # insert, delete, replace
    n = len(A)
    m = len(B)
    
    if abs(m-n) > 1: return False
    if m < n:
        A, B = B, A

    i = j = diff = 0

    while i<n and j<m:
        if A[i] != B[j]:
            if diff: return False
            diff = 1
            if m == n:
                i += 1
        else:
            i += 1
        j += 1
    return True
        
            



A = 'pale'
B = 'padle'
print(oneAway(A, B))


    



