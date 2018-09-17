#!/bin/python3

# Complete the plusMinus function below.
def plusMinus(arr):
    if len(arr) > 0:
        count_pos = 0
        count_neg = 0
        count_zero = 0
        for num in arr:
            if num > 0:
                count_pos += 1
            if num == 0:
                count_zero += 1
            if num < 0:
                count_neg += 1
        print(format(count_pos / len(arr), '.6f') + '\n' + format(count_neg / len(arr), '.6f') + '\n' + format(count_zero / len(arr), '.6f') )

n = int(input())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
