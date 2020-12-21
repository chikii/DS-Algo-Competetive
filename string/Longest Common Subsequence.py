seq = []
def LCS(i,j): # if only length of LCS has to be determined.
    if i < 0 or j < 0:
        return 0

    if s1[i] == s2[j]:
        return LCS(i-1,j-1)+1

    return max(LCS(i-1,j), LCS(i,j-1))



s1 = 'syasgh'
s2 = 'satakshi'
i = len(s1)
j = len(s2)
print(LCS(i-1,j-1), seq)




def LongestCommonSubSequence(s1,s2):
    row = len(s1) + 1 
    colomn = len(s2) + 1

    lcs = [[[None,0, (None, None)] for i in range(colomn)] for j in range(row)]

    for i in range(1, row):
        for j in range(1, colomn):
            if s1[i-1] == s2[j-1]: # go diagonally
                lcs[i][j] = [s1[i-1], lcs[i-1][j-1][1]+1, (i-1,j-1)]
            else:
                if lcs[i-1][j][1] > lcs[i][j-1][1]: # go upward 
                    lcs[i][j] = [None, lcs[i-1][j][1], (i-1,j)]
                else: # # go left
                    lcs[i][j] = [None, lcs[i][j-1][1], (i,j-1)]
    

    return backTrack(lcs), lcs[-1][-1][1]

def backTrack(lcs):
    seq = []
    i = len(lcs)-1
    j = len(lcs[0])-1
    while i != 0 and j != 0:
        curr_entry = lcs[i][j]
        if curr_entry[0] != None: seq.append(curr_entry[0])
        i,j = curr_entry[2]
        
    return ''.join(seq[::-1])


print(LongestCommonSubSequence(s1,s2))

