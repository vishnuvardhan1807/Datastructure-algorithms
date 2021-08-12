'''
logic:
    i = 0 ;       1
    i = 1 ;    1    1  
    i = 2 ;   1    -   1 ->(2)  
    i = 3 ; 1   -   -   1 -> (3, 3)
    i = 4 ; 1  -   -   -   1 -> (4, 6, 4) 
    
'''

def pascal_triangle(numrows):
    pascal_triangle = [[1] * i for i in range(1, numrows + 1)]
    
    i = 1
    while i < numrows:
        for j in range(1, len(pascal_triangle[i - 1])):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j - 1]
        i = i + 1 
    return pascal_triangle

print(pascal_triangle(5))
