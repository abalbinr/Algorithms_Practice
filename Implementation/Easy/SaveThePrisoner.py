# https://www.hackerrank.com/challenges/save-the-prisoner/

#!/bin/python3

import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    totalPrisoners = n
    candy = m
    chair = s-1
    
    lastChair = chair + candy
    
    if (lastChair > totalPrisoners):
        prisoner = lastChair - totalPrisoners*int(lastChair/totalPrisoners)
        
        if (prisoner == 0):
            prisoner = totalPrisoners
            
    else:
        prisoner = lastChair
    
    return prisoner

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
