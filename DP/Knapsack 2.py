 #knapsack over (n, profit) state,
#  if constraint of W and cost is very high.
 
 def solve(self, profit, weight, W):
        n = len(profit)
        
        prev = [0]*(50*n+1)
        
        for i in range(n+1):
            curr = [0]*(50*n+1)
            for j in range(50*n+1):
                if j == 0:  curr[j] = 0
                elif i == 0:  curr[j] = float('inf')
                elif j >= profit[i-1]:
                    curr[j] = min(prev[j],  weight[i-1]+prev[j-profit[i-1]])
                else:
                    curr[j] = prev[j]
            
            prev = curr[:]
        
        for i in range(50*n, -1, -1):
            if curr[i] <= W: return i