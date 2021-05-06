# Q. In How many ways N stair can be climb if allowesd steps are 1, 2 or 3.
# triple Sort

def noOfSteps(n, k):
    if n<0: return 0
    if n == 0: return 1

    t_steps = 0
    for i in range(1, k+1):
        t_steps += noOfSteps(n-i, k)
    
    return t_steps

def noOfStepsDP(n,k):

    dp = [0]*max((n+1),3)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    
    return dp[n]

n = 10
noOfSteps(n,3), noOfStepsDP(n,3)