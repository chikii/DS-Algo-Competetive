def heapify(arr, n, i):
    l = (2*i)+1
    r = (2*i)+2

    largest = i
    if l < n and arr[l] > arr[largest] :
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heapSort(arr):

    # first convert array into max heap
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr,n,i)
    print('after heapify',arr)

    # now top element is max, so put it at last and then ignore that element and heapify.
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f'after {i} pass',arr)
        heapify(arr, i, 0)
        print('heapify',arr)

    print('after sort',arr)

    
arr = [2,1,25,0,48,6,23,1]
heapSort(arr), arr