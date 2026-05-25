#!/bin/python3

"""
Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:
- If the difference between the  and the next multiple of  is less than ,
round  up to the next multiple of .

- If the value of  is less than , no rounding occurs as the result will still be a failing grade.
"""

# quotient = 23 // 5

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here

    result = []

    for grade in grades:
        # find the quotient
        quotient = grade // 5

        if grade < 38:
            result.append(grade)

        elif (((quotient+1)*5) - grade) < 3:
            result.append((quotient+1)*5)

        else:
            result.append(grade)

    return result





if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)

#    fptr.write('\n'.join(map(str, result)))
#    fptr.write('\n')

 #   fptr.close()

