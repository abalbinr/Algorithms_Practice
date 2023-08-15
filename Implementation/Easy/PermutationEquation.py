# https://www.hackerrank.com/challenges/permutation-equation

#!/bin/python3

import math
import os
import random
import re
import sys

def permutationEquation(p):
    listY = []
    for x in range(1,len(p)+1):
        for y in range(1,len(p)+1):
            if (p[p[y-1]-1] == x):
                listY += [y]
    
    return listY

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()