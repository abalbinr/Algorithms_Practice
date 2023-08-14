# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/

#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    
    beautifulDay = 0
    for day in range(i,j+1):
        reverseDay = int(str(day)[::-1])
        diff = abs(day - reverseDay)
        
        if (diff % k == 0):
            beautifulDay += 1
    
    return beautifulDay

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()