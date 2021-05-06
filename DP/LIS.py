# Time - O(N^2)
# Space - O(N)

def longestIncreasingSequence(arr):
    length = [1 for i in range(len(arr))] 
    #length of longestIncreasingSequence ending at index i

    seq = [None for i in range(len(arr))]
    #last index of longestIncreasingSequence ending at index i
    
    max_length_idx = 0 # idx of last element of LIS

    for i in range(len(arr)):

        # for each element we will check its  all previous elemnts
        for j in range(0,i):

            #if prev elem is leser than currr element 
            # and (length of LIS ending at that indx(prev elem's idx)) + 1 (including curr elem)
            # is greater than length os LIS ending at curr idx 
            # then, update length of LIS at curr idx
            # and seq[i] = j (last indx of LIS)

            if arr[j] < arr[i] and length[i] <= length[j] + 1:
                length[i] = length[j] + 1
                seq[i] = j
        
        #if curr LIS is greater than last LIS
        # then, update LIS with curr LIS
        if length[i] > length[max_length_idx]:
            max_length_idx = i
    
    return buildLIS(arr, seq, max_length_idx), length[max_length_idx]

def buildLIS(arr, seq, max_length_idx):
    # back track the sequences from idx of LIS
    LIS = []            
    curr = max_length_idx

    while curr is not None:
        LIS.append(arr[curr])
        curr = seq[curr]
    
    return LIS[::-1]


arr = [5,7,-24,12,10,2,3,12,5,18,35]
print(longestIncreasingSequence(arr))
