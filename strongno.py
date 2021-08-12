def strongprime(start, end):
    array = []
    for i in range(start, end):
        count = 0
        if i == 2:
            array.append(i)
        for j in range(2, i):
            if i % j == 0:
                count = count + 1
        if count == 0:
            array.append(i)
                
    return array
                

prime_numbers = strongprime(start=10, end=51)
print(prime_numbers)
strong_prime = []
first = prime_numbers[0]
last = prime_numbers[-1]
current_index = 1
last_index = len(prime_numbers) - 1

pre_prime = first - 1

while True:
    pre_prime = pre_prime - 1
    print(pre_prime)
    for j in range(2, pre_prime):
        count = 0
        if pre_prime % j == 0:
            count = count + 1
    if count == 0:
        sum_ = (pre_prime + prime_numbers[current_index]) // 2
        print(sum_)
        if first > sum_:
            strong_prime.append(first)
        break
                
            
    
    
    

while current_index < last_index:
    previous_index = current_index - 1
    next_index = current_index + 1
    
    sum_ = (prime_numbers[previous_index] + prime_numbers[next_index]) // 2
    if prime_numbers[current_index] > sum_:
        strong_prime.append(prime_numbers[current_index])
    
    current_index = current_index + 1

print(strong_prime)


    