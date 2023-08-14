# https://www.hackerrank.com/challenges/utopian-tree/

#!/bin/python3

import math
import os
import random
import re
import sys

def utopianTree(n):
    
    finalHeight = 1
    for cycle in range(1,n+1):
        if (cycle % 2 == 1):
            finalHeight *= 2
        else:
            finalHeight += 1
    
    return finalHeight

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
