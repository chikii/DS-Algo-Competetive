# Q - subarray having maximum sum
"""
The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array (max_ending_here is used for this).
And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). 
Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than max_so_far .
"""
def solve(A, n):
    max_so_far = int_min
    max_ending_here = 0

    # 3 step algo

    for i in range(n):
        # 1) add in curr sum    
        max_ending_here += A[i]

        # 2) if curr sum become greater than ans, update ans
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        
        # 3) if curr sum is less than 0, set curr sum = 0
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

int_min = -float('inf')