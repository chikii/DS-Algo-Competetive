# Q - Power set
s = [1,2,3,4,5]

def powerSet(curr_seq, curr_idx, n, A, ans):
    if curr_idx == n:
        ans.append(curr_seq[:])
        return
    
    powerSet(curr_seq, curr_idx+1, n, A, ans)

    curr_seq.append(A[curr_idx])
    powerSet(curr_seq, curr_idx+1, n, A, ans)
    curr_seq.pop()



power_set = []
powerSet([], 0, len(s), s, power_set)
for subset in power_set:
    print(subset)