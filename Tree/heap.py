# defination of heap ->
# min heap -> In a Min-Heap the root node must be minimum among the keys present at all of it’s children.
# The same property must be recursively true for all sub-trees in that Binary Tree.

# Max-Heap: In a Max-Heap the root node must be greatest among the keys present at all of it’s children. 
# The same property must be recursively true for all sub-trees in that Binary Tree.

# point to remember ->
# parent -> (i-1)//2
# left -> (2*i)+1
# right -> (2*i)+2

def heapush(new_elem, arr): # min heap
    arr.append(new_elem)
    curr = len(arr)-1
    parent = (curr-1)//2
    print(curr, parent)
    while parent >= 0 and arr[parent] > arr[curr]: # min heap
    # while parent >= 0 and arr[parent] < arr[curr]: # max heap
        temp = arr[parent]
        arr[parent] = arr[curr]
        arr[curr] = temp

        curr = parent
        parent = (parent-1)//2

    return 

def heappop(arr):
    # min or max
    if len(arr) == 0: return 'empty!!!'
    arr[0], arr[-1] = arr[-1], arr[0]
    elem = arr.pop() 
    min_heapify(0, arr)
    return elem

def min_heapify(index, arr, n):
    l = (2*index)+1
    r = (2*index)+2

    smallest = index
    if l < n and arr[l] < arr[smallest]:
        smallest = l
    
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
         
        min_heapify(smallest, arr, n)

a = [5,4,3,2,1]
n = len(a)
def createHeap(a):
    for i in range(len(a)//2 - 1, -1, -1):
        min_heapify(i, a, n)

createHeap(a), a

arr = []    
heapush(1, arr)
heapush(3, arr)
heapush(2, arr)
heapush(4, arr)
heapush(0, arr)
heapush(5, arr)

heappop(arr), arr
heappop(arr), arr
heappop(arr), arr
heappop(arr), arr
heappop(arr), arr
heappop(arr), arr
heappop(arr), arr