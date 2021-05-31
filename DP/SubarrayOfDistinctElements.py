"""
find count of all subsequesce of less than euqal to k having destinct elements.
note -> subsquence of len 0 is valid
ex = arr = [2,2,3,3,5], k = 3
ans = 18

explanation -> 
1 seq with 0 distinct elem
5 seq with 1 distinct elem
8 seq with 2 distinct elem
4 seq with 3 distinct elem

total = 18
"""

n,k = map(int,input().split())
a = list(map(int,input().split()))

# frequency array
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1


n = len(freq) # now n is total distinct element

freq = list(freq.values()) # taking actual freq values  for element


dp = [[0]*(k+1) for _ in range(n)] 

for i in range(n):
    dp[i][0] = 1

dp[0][1] = freq[0]

"""
      k -> 0  1  2  3  # len of elements of distinct element
n
^
1 element  1  2  0  0   d[i][j] -> how many total subarray using i elemnets can have of length j
2 element  1  0  0  0   subarray_can_be_made_using_i_element = total subarrays withouth using ith element(dp[i-1][j-1]) * freq[i]
3 element  1  0  0  0   total_subarray_of j len with i elements = total_subarray_without_i_of j len(dp[i-1][j]) + subarray_can_be_made_using_i_element
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*freq[i]
"""

for i in range(1,n):
    for j in range(1,k+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*freq[i]

# now total subarrays of distinct element of less than euqal to k len is
# subarrays of distinct element using n elements of len 0 + 1 + 2 + 3 + .. K 
"""
      
n     k -> 0  1  2  3  # len of elements of distinct element
^
1 element  1  2  0  0   
2 element  1  4  4  0
3 element  1  5  8  4   

def ->
d[i][j] -> how many total subarray using i elemnets can have of length j                        
"""

ans = 0
for i in range(k+1):
    ans += dp[n-1][i]


print(ans)
print(dp)

# this problem can be treat as subarray of distinct element of len k
# in this case do print dp[n-1][K]