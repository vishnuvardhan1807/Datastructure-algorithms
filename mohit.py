import math

l = int(input())
r = int(input())
k = int(input())

n = l
p = []
for i in range(n, r+1):
    for i in range(1, math.sqrt(n)):

        if n % i == 0:
            flag = 0
            break

    if flag == 1:
        p.append(i)
        
print(p)
