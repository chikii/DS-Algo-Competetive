import math

arr = [1,2,3,4,5,6,7,8,9,10]
n = 10
sqrt_n = math.sqrt(n)
block_size = math.ceil(n/sqrt_n)
BLOCKS = [0]*block_size

for i in range(n):
    BLOCKS[i//block_size] += arr[i]

def update(idx, new_value):
    BLOCKS[idx//block_size] += new_value - arr[idx]
    arr[idx] = new_value

def range_sum(l, r):

    start_block = l//block_size
    end_block = r//block_size

    res_sum = 0


    while l<r and l<(start_block+1)*block_size: # first l-> last_index of same block
        res_sum += arr[l]
        l += 1
    
    while l//block_size < end_block: # all the blocks excepts last one in which r lies
        res_sum += BLOCKS[l//block_size]
        l += block_size
    
    while l<=r: # starting index of block in which r is till r.
        res_sum += arr[l]
        l += 1
    
    return res_sum

print(arr, BLOCKS)
update(9, 11)
print(arr, BLOCKS)
range_sum(0,4)