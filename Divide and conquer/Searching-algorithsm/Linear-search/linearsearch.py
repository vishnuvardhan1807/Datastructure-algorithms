"""
Best-case:O(1), Worst-case:O(n), average-case:O(n)

"""


def Linearsearch(array, element, n):
    for i in range(n):
        if array[i] == element:
            return i
    return -1 # -1 indicates that element is not present in array 


# Driver code
arr = [53, 21, 90, 32, 47, 89]
element = int(input("Enter the element to search:"))
n = len(arr)
print(Linearsearch(arr, element, n))