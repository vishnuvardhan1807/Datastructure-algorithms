from random import randint
def randomList(m, n, arr):
    arr1 = [0] * m - 1
    n = n - 1
	for i in range(n) :
		arr1[randint(0, n) % m] += 1
	return len(arr + arr1)


m = 5 
n = 10
arr = [1]
randomList(m, n, arr)

