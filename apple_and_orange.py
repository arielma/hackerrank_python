#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_distance_list = [distance + a for distance in apples]
    oranges_distance_list = [distance + b for distance in oranges]

    apple_in_house = sum(distance in range(s, t + 1) for distance in apples_distance_list)
    orange_in_house = sum(distance in range(s, t + 1) for distance in oranges_distance_list)
    print(str(apple_in_house) + '\n' + str(orange_in_house))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
