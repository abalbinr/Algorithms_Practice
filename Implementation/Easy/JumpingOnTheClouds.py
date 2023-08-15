# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited

#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    index = (0 + k) % len(c)
    energy = 99 
    if (c[index] == 1):
        energy -= 2
    
    while (index != 0):
        index = (index + k) % len(c)
        
        energy -= 1
        if (c[index] == 1):
            energy -= 2
            
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
