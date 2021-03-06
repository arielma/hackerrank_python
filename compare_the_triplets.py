#!/bin/python3

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    if len(a) == len(b) == 3:
        score_a = 0
        score_b = 0
        for i in range(3):
           [score_a, score_b] = scoring(a[i], b[i], score_a, score_b)
        return [score_a, score_b]
def scoring(num1, num2, score1, score2):
    if num1 > num2:
        score1 += 1
    if num1 < num2:
        score2 += 1
    return [score1, score2]


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))
