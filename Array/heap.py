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

    return arr 

def heappop(arr):
    # min or max
    if len(arr) == 0: return 'empty!!!'
    arr[0], arr[-1] = arr[-1], arr[0]
    elem = arr.pop() 
    min_heapify(0, arr)
    return elem

def min_heapify(index, arr):
    l = (2*index)+1
    r = (2*index)+2

    largest = index
    if l < len(arr) and arr[l] < arr[largest]:
        largest = l
    
    if r < len(arr) and arr[r] < arr[largest]:
        largest = r

    if largest != index:
        temp = arr[largest]
        arr[largest] = arr[index]
        arr[index] = temp

        min_heapify(largest, arr)

a = [5,4,3,2,1]
def createHeap(a):
    for i in range(len(a)//2 - 1, -1, -1):
        min_heapify(i, a)

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