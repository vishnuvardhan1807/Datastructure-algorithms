def numTriplets(array, target):
   i = 0
   j = 1
   triplets = []
   while True:
      for k in range(j+1,len(array)):
         if array[i] + array[j] + array[k] <= targetsum:
           triplets.append((array[i], array[j], array[k]))
      j += 1
      if j == len(array) - 1:
         i += 1
         j = i + 1
      if i == len(array) - 2:
         return triplets

a = [2, 7, 4, 9, 5, 1, 3]
targetsum = 10
values = numTriplets(a,targetsum)
for i in values:
    print(i)