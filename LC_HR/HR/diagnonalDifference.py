#!/bin/python3

import math
import os
import random
import re
import sys


"""
STDIN      Function
-----      --------
3           arr[][] sizes n = 3, m = 3
11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
4 5 6
10 8 -12
"""


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    diag_sum = 0
    reverse_diag_sum = 0
    n = len(arr)

    for i in range(0, n):
        diag_sum += arr[i][i]
        reverse_diag_sum += arr[i][n-1-i]

return math.fabs(diag_sum - reverse_diag_sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)


    fptr.write(str(result) + '\n')

    fptr.close()


