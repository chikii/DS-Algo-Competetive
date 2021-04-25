# Q> You are given an array, find is there a subset whose sum is equal to target.

# Subset -> Elemen can be in any order
# Subsequence -> contigeous element.

def SubsetSumR(lastIDX, target): # Recurr
    if target == 0:
        return True
    if lastIDX < 0:
        return False
    
    if SubsetSumR(lastIDX-1, target):
        return True
    
    if arr[lastIDX] > target:
        return False
    
    return SubsetSumR(lastIDX-1, target-arr[lastIDX])


def SubsetSumDP(arr, target):

    row = (len(arr)+1)
    col = (target+1)

    dp = [[False]*col for i in range(row)]

    # We can always have sum = 0
    for i in range(row):
        dp[i][0] = True

    # we can not have any sum (except 0) when we have 0 elements.
    # dp[0][1->col] = False

    for curr_elem in range(1, row):
        for curr_sum in range(1, col):
            dp[curr_elem][curr_sum] = dp[curr_elem-1][curr_sum]

            if arr[curr_elem-1] <= curr_sum:
                dp[curr_elem][curr_sum] |= dp[curr_elem-1][curr_sum-arr[curr_elem-1]]
    
    return backTrack(dp, target), dp[-1][-1]

def backTrack(dp, target):
    if dp[-1][-1] == False: return []

    result_subset = []

    curr_elem = len(dp)-1
    target = target

    while target and curr_elem:
        if dp[curr_elem-1][target]:
            curr_elem = curr_elem-1
        else:
            result_subset.append(arr[curr_elem-1])
            target -= arr[curr_elem-1]
            curr_elem = curr_elem-1
    
    return result_subset

arr = [4,2,5,3,6,8]
target = 15
lastIDX = len(arr)-1
print(SubsetSumDP(arr, target))
















