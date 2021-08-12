""" Time complexity:O(logn)"""

def BinarySearch(array, low, high, element):
    while low <= high:
        # Divide the problem
        mid = low + (high - low) // 2
        # If mid is greater than element
        if array[mid] > element:
            high = mid - 1

        # if mid is less than element
        elif array[mid] < element:
            low = mid + 1
        else:
            return mid

# Driver code
array = [2, 5, 7, 12, 34, 56, 79, 80, 90]
element = 80
n = len(array)
pos = BinarySearch(array, 0, n-1, element) # Call the main function
print(pos)