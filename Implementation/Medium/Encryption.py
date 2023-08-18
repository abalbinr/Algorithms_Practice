# https://www.hackerrank.com/challenges/encryption/

#!/bin/python3

import math
import os
import random
import re
import sys

def encryption(s):
    s = s.replace(" ","")
    lenght = len(s)
    floorS = math.floor(math.sqrt(lenght))
    ceilS = math.ceil(math.sqrt(lenght))
    
    if (floorS*floorS >= lenght):
        row = floorS
        column = floorS
    elif (floorS*ceilS >= lenght):
        row = floorS
        column = ceilS
    elif (ceilS*ceilS >= lenght):
        row = ceilS
        column = ceilS
    
    firstEncoding = []
    index = 0
    while (index < lenght):
        if (index+column < lenght):
            word = s[index:index+column]
            firstEncoding += [word]
            index += column
        else:
            word = s[index:]
            firstEncoding += [word]
            index += column
    
    secondEncoding = []
    for i in range(column):
        secondEncoding += [""]
        
    for word in firstEncoding:
        for index in range(column):
            if (index < len(word)):
                secondEncoding[index] = secondEncoding[index] + word[index]

        
    return " ".join(secondEncoding)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
