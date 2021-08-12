""" Time complexity:O(logn)"""

def BinarySearch(array, low, high, element):
    # Consider this as a small problem
    if low == high:
        if array[low] == element:
            return low
        else:
            return -1
    
    # Big Problem -> Use divide and Conquer
    else:
        mid = (low + high) // 2
        ''' 
        If numbers are big
        mid = low + (high - low) // 2
        '''
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            return BinarySearch(array, mid + 1, high, element) # -> Conquer(Recursive call=T(N/2))
        else:
            return BinarySearch(array, low, mid-1, element)  # -> Conquer(Recursive call=T(N/2))



# Driver code
array = [2, 5, 7, 12, 34, 56, 79, 80, 90]
element = 80
n = len(array)
pos = BinarySearch(array, 0, n-1, element) # Call the main function
print(pos)