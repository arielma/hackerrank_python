#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_sub = []
    for ele in arr:
        sum_sub.append(sum(arr) - ele)
    print(str(min(sum_sub)) + ' ' + str(max(sum_sub)))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)