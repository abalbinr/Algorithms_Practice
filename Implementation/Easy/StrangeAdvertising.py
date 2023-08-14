# https://www.hackerrank.com/challenges/strange-advertising/

#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared = 5
    accumulatedLikes = 0
    for day in range(1,n+1):
        liked = int(shared/2)
        accumulatedLikes += liked
        shared = liked*3
    
    return accumulatedLikes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()