# https://www.hackerrank.com/challenges/angry-professor/

#!/bin/python3

import math
import os
import random
import re
import sys

def angryProfessor(k, a):
    onTime = 0
    for arrivalTime in a:
        if (arrivalTime <= 0):
            onTime += 1
    
    if (onTime < k):
        return "YES"
    else: 
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()