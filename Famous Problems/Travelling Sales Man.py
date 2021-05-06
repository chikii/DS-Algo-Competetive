

# mask -> 1 - city we had visited
#         0 - city is unvisited
# pos  ->  define the curr city we are standing on.
def tsp(mask, pos):

    if mask == all_visited: # if all city is visited.
        return A[pos][0] # return the distance from last city to our src city
    
    if dp[mask][pos] != -1:
        return dp[mask][pos]
        
    ans = int_max
    for city in range(0, n):
        if mask&(1<<city) == 0: # if city is not visited
            # mark the city visited and find cost for that.
            new_ans = A[pos][city] + tsp(mask|(1<<city), city)
            ans = min(ans, new_ans)

    dp[mask][pos] = ans
    return ans


int_max = float('inf')
A = [
    [0,20,42,25],
    [20,0,30,34],
    [42,30,0,10],
    [25,34,10,0]
]
n = len(A)


all_visited = (1<<n)-1
# 1 - visited
# 0 - unvisted
# all_visited = 1111  # our base condition

ans = int_max
for i in range(n):
    dp = [[-1]*n for i in range(1<<n)]
    ans = min(ans, tsp(1<<i, i))

print(ans)