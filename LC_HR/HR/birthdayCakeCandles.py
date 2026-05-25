#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here

    candles.sort()
    maximum = 0
    count = 0

    for i in range(len(candles)):
        if candles[i] > maximum:
            maximum = candles[i]
            count = 1
        elif candles[i] == maximum:
            count += 1
        else:
            pass

    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
