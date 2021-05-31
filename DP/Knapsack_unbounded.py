  #  recursion : N^W - Time
    
def solve(self, W, values, weights):
    n = len(values)
    
    profit = [0]*(W+1)
    
    for i in range(1, n+1):
        for w in range(1, W+1):
            if w >= weights[i-1]:
                profit[w] = max(profit[w], profit[w-weights[i-1]]+values[i-1])
                
    return profit[W]