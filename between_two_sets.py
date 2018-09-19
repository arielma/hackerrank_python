#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    a_max = max(a)
    b_min = min(b)
    count = 0
    if b_min >= a_max:
        for i in range(a_max, b_min + 1):
            if sum([i % a_elem for a_elem in a]) == 0 and sum([b_elem % i for b_elem in b]) == 0:
                count += 1
    return count  

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
