def knapsack(W_C, profit, wieght, n):
    ##base case
    if n == -1 or W_C <= 0:
        return 0

    if memo[n][W_C] != -1:
        print('memo used')
        return memo[n][W_C]

    ## if wieght[nth item] is greater than capacity of knapsack then we can not include it.
    if wieght[n] > W_C:
        memo[n][W_C] = knapsack(W_C, profit, wieght, n-1)
        return memo[n][W_C]
    ## we choose max of
    # 1. either we include it -> 1. add profit[nth item] 
    #                            2. decrease W_C(wieght capacity) by wieght[nth item]
    #                            3. n = n-1
    # 2. or we not include it.-> 1. n = n-1
    else:
        memo[n][W_C] =  max( profit[n] + knapsack(W_C-wieght[n], profit, wieght, n-1), knapsack(W_C, profit, wieght, n-1) )
        return memo[n][W_C]

profits = [60,100,120]
wieghts = [10,20,30]
capacity = 40
n = len(wieghts)
memo = [[-1]*(capacity+1) for i in range(n+1)]
ans = knapsack(capacity, profits, wieghts, n-1)
print('Maximun Profit : ', ans) 



def solve(self, value, weight, W):
    n = len(value)
    
    # profit[i][j] -> maximum profit i can make upto j using i items.
    
    prv = [0]*(W+1)
    
    for i in range(1, n+1):
        curr = [0]*(W+1)
        for j in range(1, W+1):
            if j >= weight[i-1]:
                curr[j] = max(prv[j]  , value[i-1] + prv[j-weight[i-1]])
            else:
                curr[j] = prv[j]
        
        prv = curr[:]
        
    return curr[W]