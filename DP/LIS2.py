# Time - O(NlogN)
# Space - O(N)

def longestIncreasingSubSequence(arr):
    n = len(arr)
    if n == 0 : return 0

    # indices - last element indx of LIS of length i
    # means - indexes are length of LIS
    # and there values are last element's indx of LIS of length i
    # i.e = indices[3] = 2 means LIS of length 3 will end at index 2.
    indices = [None for i in range(n+1)]
    sequences = [None for i in range(n)] # same as earlier

    max_length = 0

    for i in range(n):
        # performimng binary searches on length. 
        # as if a element increasing a length of LIS at half then it makess more sense to increase rather decrease.
        # so we go in increasing direction
        # we can apply binary search for this.

        # max_length is itself the end because aftterthat we will have all NOne values.
        new_length = binarySearch(arr, 1, max_length, i, indices)

        # it will end on length of LIS we can have with arr[i] as last element of LIS

        indices[new_length] = i # we update the last element of LIS of length new_length

        sequences[i] = indices[new_length-1] 
        # as it obvious length increase by one (adding curr element) in last LIS.

        max_length = max(max_length, new_length)

    print(sequences)
    return buildSeq(arr, sequences, indices[max_length]), max_length

def binarySearch(arr, start, end, curr, indices):
    if start > end: return start 
    ## we have to give one index ahead of it. as we are adding curr element also.
    
    mid = (start + end) // 2
    
    # i = indices[mid] -> (idx of last element) of (LIS of length 'mid')
    # arr[i] = that element itself
    if arr[indices[mid]] < arr[curr]:
        start = mid + 1
    else:
        end = mid - 1
    
    return binarySearch(arr, start, end, curr, indices)


def buildSeq(arr, sequences, curr):
    seq = []
    while curr != None:
        seq.append(arr[curr])
        curr = sequences[curr]
    return seq[::-1]

arr = [5,7,-24,12,10,2,3,12,5,6,35]
print(longestIncreasingSubSequence(arr))