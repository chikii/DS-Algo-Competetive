def knapsack(W_C, profit, wieght, n):
    ##base case
    if n == -1 or W_C == 0:
        return 0

    ## if wieght[nth item] is greater than capacity of knapsack then we can not include it.
    if wieght[n] > W_C:
        return knapsack(W_C, profit, wieght, n-1)
    ## we choose max of
    # 1. either we include it -> 1. add profit[nth item] 
    #                            2. decrease W_C(wieght capacity) by wieght[nth item]
    #                            3. n = n-1
    # 2. or we not include it.-> 1. n = n-1
    else:
        return max( profit[n] + knapsack(W_C-wieght[n], profit, wieght, n-1), knapsack(W_C, profit, wieght, n-1) )

profits = [60,100,120]
wieghts = [10,20,30]
capacity = 40
n = len(wieghts)
ans = knapsack(capacity, profits, wieghts, n-1)
print('Maximun Profit : ', ans) 
