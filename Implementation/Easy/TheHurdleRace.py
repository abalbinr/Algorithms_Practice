# https://www.hackerrank.com/challenges/the-hurdle-race/

#!/bin/python3

import math
import os
import random
import re
import sys

def hurdleRace(k, height):
    maxHeight = max(height)
    diff = maxHeight - k
    if (diff <= 0):
        return 0
    else:
        return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
