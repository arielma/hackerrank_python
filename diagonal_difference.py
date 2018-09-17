#!/bin/python3

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    ltr_diag_sum = 0
    rtl_diag_sum = 0
    for i in range(0, len(arr[0])):
        ltr_diag_sum += arr[i][i]
        rtl_diag_sum += arr[i][-i-1]
    return abs(ltr_diag_sum - rtl_diag_sum)


n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(str(result) + '\n')

