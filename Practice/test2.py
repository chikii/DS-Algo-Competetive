



# def solve(curr, seq, sq_len, switch, rem):
#     global ans_sq 
#     global ans
#     if sq_len == 10 and len(seq) == 10:
#         if switch < ans:
#             ans = switch
#             ans_sq = seq[:]
#             # print('curr seq', seq, ans_sq)
#         return 

#     # print(f' rem elem for {curr} {[i for i in range(10) if rem[i] == True]} ')
#     for i in range(10):
#         if not rem[i]: continue
#         curr_s = no[curr]
#         next_s = no[i]
#         temp_switch = 0
#         for j in range(7):
#             if curr_s[j] != next_s[j]:
#                 temp_switch += 1 
#         seq.append(i)
#         rem[i] = False
#         solve(i, seq, sq_len+1, switch+temp_switch, rem)
#         rem[i] = True
#         seq.pop()
    

# ans_sq = ''
# ans = float('inf')
no = [
    '1111110',
    '0110000',
    '1101101',
    '1111001',
    '0110011',
    '1011011',
    '0011111',
    '1110000',
    '1111111',
    '1110011'
]

# # switch = 0
# # for j in no[0]:
# #     if j=='1':
# #         switch += 1
# # rem = {i:True for i in range(1, 10)}
# # rem[0] = False
# # print(solve(0,[0],1,switch, rem))

# for i in range(10):
#     switch = 0
#     for j in no[i]:
#         if j=='1':
#             switch += 1
#     rem = {i:True for i in range(0, 10)}
#     rem[i] = False
#     solve(i, [i], 1, switch, rem) 
#     # print('if start with', i, 'best seq')
#     print(ans, ans_sq)


# print(ans, ans_sq)

# switch = [0]*10
# best_seq = [7,0,1,2,3,4,5,6,8,9]

# for i in no[7]:
#     if i=='1':
#         switch[0] += 1
# for i in range(1, 10):
#     for j in range(7):
#         if no[best_seq[i]][j] != no[best_seq[i-1]][j]:
#             switch[i] += 1

# print(switch)


t = int(input())
for _ in range(t):
    len_ = int(input())
    string = input()

    frq = {}
    for i in range(10):
        frq[i] = False

    for i in string:
        frq[int(i)] = True

    best_seq = [1, 7, 3, 2, 0, 8, 6, 5, 9, 4]

    ans = 0
    last = -1
    for i in best_seq:
        if frq[i]:
            if last == -1:
                last = i
                for j in range(7):
                    if no[i][j] == '1':
                        ans += 1
            else:
                for j in range(7):
                    if no[i][j] != no[last][j]:
                        ans += 1
                last = i
    
    print(ans)
            
