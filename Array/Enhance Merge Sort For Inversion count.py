"""
Inversion Count for an array indicates – 
how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8,4), (4,2),(8,2), (8,1), (4,1), (2,1).


Input: arr[] = {3, 1, 2}
Output: 2

Explanation: Given array has two inversions:
(3, 1), (3, 2) 

"""

def mergesort(arr):
    if len(arr) > 1 :

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        intrusion = mergesort(left)
        intrusion += mergesort(right)
            
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                intrusion += mid - i # all element between mid and i is less than the a[i] if a[i] > a[j]
            k += 1
            #    i       mid,j
            #    |        |
            # [1,5,8,10] [2,3,11,12]
            
            # hence if a[j] is smaller than a[i] . it(a[j]) will be smaller for all element in 1st subarray after i till mid.
            # we can see 5>2:
            #             8>2, 10>2
            #             hence intrusion = mid - i = 3 which is ((5>2), (8>2), (10>2))
            #             i += 1; j+= 1;

            #             and Now continue the same loop for each i j

            
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
        
        return intrusion
    return 0


arr = [7, 9, 3, 5, 1, 6, 4]
print(mergesort(arr), arr)

