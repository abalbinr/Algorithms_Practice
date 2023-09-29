# https://www.hackerrank.com/challenges/reduced-string/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    reduced = True
    while (reduced):
        newString = ""
        reduced = False
        index = 0
        while (index < len(s)):
            letter = s[index]
            if (index == len(s)-1):
                newString += letter
                index += 1
            elif (letter != s[index+1]):
                newString += letter
                index += 1
            else:
                index += 2
                reduced = True
        
        s = newString
        
    if(len(s) == 0):
        return "Empty String"
    else:
        return newString
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()