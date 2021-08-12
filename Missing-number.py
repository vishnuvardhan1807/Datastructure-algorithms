''' Find the missing number in the array
    
   input: [1, 2, 4, 5, 6]
   output: 3
'''

# My approach (Time-complexity-o(nlogn))
def find_missing_number(input_array):
    input_array.sort()
    min_value = input_array[0]
    max_value = input_array[len(input_array) - 1]
    
    for i in range(min_value, max_value):
        if i not in input_array:
            print(f"{i} is the missing number")
            break
            
    
    
array = [1, 2, 4, 5, 6]
find_missing_number(array)


''' Approach 2

   1. Find the sum of all number in array
   2. Find the sum of n numbers using formula n(n + 1) // 2
   3. subract 2 with 1
   
   Time-complexity - O(n), space-complexity - O(1)
   
'''

def find_missing_number(input_array) ->int:
    length = len(input_array)
    total_sum = 0
    for num in input_array:
        total_sum = total_sum + num
    
    sum_of_n_numbers = length * (length + 1) // 2
    
    print(f"The missing number is {(abs(sum_of_n_numbers - total_sum))}")




array = [1, 2, 4, 5, 6]
find_missing_number(array)
    