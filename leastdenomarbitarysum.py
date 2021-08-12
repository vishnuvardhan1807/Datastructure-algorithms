"""
logic:
   
    4 -> 1, 2, 3 = log(4) + 1 = 3
    8 -> 1, 2, 3, 4 = log(8) + 1 = 4
    
    so the minum number of denom's for
    a given arbitary sum 'n' is log(n) to base 2 + 1
    
"""

import math
class denom_arbitary:
    def min_num_denoms(self, n):
        return math.log2(n) + 1
    
if __name__ == '__main__':
    n = int(input("Enter a Number:"))
    ob = denom_arbitary()
    print(math.floor((ob.min_num_denoms(n))))
        