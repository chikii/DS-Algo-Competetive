# idea -> we will maintain the opening and closing brackets count,
# case 1
# if opening brackets < allowed opening brackets (N) : add opening bracket

# case 2
# if closing brackets < opening brackets : add closing brackets



def solve(curr_seq,curr_len, op, clos, n):
    if curr_len == 2*n:
        print(''.join(curr_seq))
        return
    
    if op < n:
        curr_seq.append('(')
        solve(curr_seq, curr_len+1, op+1, clos, n)
        curr_seq.pop()
    
    if clos < op:
        curr_seq.append(')')
        solve(curr_seq, curr_len+1, op, clos+1, n)
        curr_seq.pop()

N = 2
solve([], 0, 0, 0, N)