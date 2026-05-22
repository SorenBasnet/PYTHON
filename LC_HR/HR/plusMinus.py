#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    # Calculate the number of
    # Positve, Negative, Zero

    pos = 0
    neg = 0
    zero = 0

    for i in range(0, len(arr)):
        if arr[i] == 0:
            zero += 1
        elif arr[i] < 0:
            neg += 1
        else:
            pos += 1

    # print(f"{number:.2f}")

    print(f"{pos/len(arr):.6f}")
    print(f"{neg/len(arr):.6f}")
    print(f"{zero/len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
