#!/bin/python3

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    if len(a) == len(b) == 3:
        score_a = 0
        score_b = 0
        for i in range(3):
            if a[i] > b[i]:
                score_a += 1
            if a[i] < b[i]:
                score_b +=1
        return [score_a, score_b]

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))
 