#!/bin/python3

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
    new_grades = []
    for i in range(0,4):
        if grades[i] < 38:
            new_grades.append(grades[i])
        else:
            x=grades[i]+1
            y=grades[i]+2
            if grades[i] % 5 == 0:
                new_grades.append(grades[i])
            elif x%5 == 0:
                new_grades.append(x)
            elif y%5 == 0:
                new_grades.append(y)
            else:
                new_grades.append(grades[i])
    return new_grades
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
