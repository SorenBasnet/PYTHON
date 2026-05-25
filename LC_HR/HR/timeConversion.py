#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    # using regex example
    # match = re.search(r"\d+", "I have 2 apples")
    # if match:
    #    print(f"Found: {match.group()}")  # Output: Found: 2

    match = re.search(r"AM|PM", s)

    # Split the hours
    hours = s.split(':')[0]

    total = s.split(':')


    match_result = re.search(r"[0-9]+", total[2])


    if match.group() == "AM":


        if hours == 12:
            return "00"+total[1]+match_result.group()

    if match.group() == "PM":
        return str(int(hours)+12)+":"+total[1]+":"+match_result.group()



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
