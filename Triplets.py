def triplets(array, targetsum):
    array.sort()
    for i in range(len(array)-2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] <= targetsum:
                    print((array[i], array[j], array[k]))

    # Finding triplets equal to a given sum
    '''for value in range(len(array) - 2):
        left = value + 1
        right = len(array) - 1

        while left < right:
            currentsum = array[left] + array[right] + array[value]
            if currentsum == targetsum:
                print((array[left], array[right], array[value]))
                left = left + 1
                right = right - 1

            elif currentsum < targetsum:
                print((array[left], array[right], array[value]))
                left = left + 1
            
            elif currentsum > targetsum:
                right = right - 1'''



array = [2, 7, 4, 9, 5, 1, 3]
targetsum = 10
triplets(array, targetsum)