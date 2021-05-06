def permute(curr_seq, curr_len, n, freq):
    if curr_len == n:
        print(curr_seq)
        return

    for i in freq.keys(): # point to remember, iterate over unique items only.
        if freq[i] > 0:
            freq[i] -= 1
            curr_seq.append(i)
            permute(curr_seq, curr_len+1, n, freq)
            curr_seq.pop()
            freq[i] += 1

A = 'yaas'
n = len(A)
freq = {}
for i in A:
    if i in freq: freq[i] += 1
    else: freq[i] = 1
permute([], 0, n, freq)