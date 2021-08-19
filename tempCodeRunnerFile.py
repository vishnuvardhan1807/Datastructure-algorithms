
def randomList(m, n):

    arr = [0] * m

    for i in range(n) :


        arr[randint(0, n) % m] += 1

    printArr(arr, m)