# Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit.
# op allowed - # insert, delete, replace

from os import replace


def oneAway(A, B):
    
    n = len(A)
    m = len(B)
    
    # if diff between length is greater than 1. never possible in one edit
    if abs(m-n) > 1: return False

    # we are making the shorter string s1 and and longer s2.
    # So, we have only two option left, 
    #         insert
    #         replace,

    #         if we delete - than the length will become nore shorter, which make no sense

    
    if m < n:
        A, B = B, A
        n = len(A)
        m = len(B)

    i = j = diff = 0
    # one thing to notice, we can insert only,
            # if n < m, else we can only replace the char,

    while i<n and j<m:
        if A[i] != B[j]:
            if diff: return False
            diff = 1

            if m == n: # replace, if replace, then curr char is counted, 
                i += 1
            # if inserted new char, curr char is not counted.
        else:
            i += 1 # if same, curr char counted, we are always increasing j, so it is good.

        j += 1 # always increase j of s2
    return True
        
            



A = 'pale'
B = 'padle'
print(oneAway(A, B))


    



