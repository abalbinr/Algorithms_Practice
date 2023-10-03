# https://www.hackerrank.com/challenges/two-characters/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    maxLength = 0
    
    uniqueChar = list(set(s))
    for i in range(0,len(uniqueChar)):
        for j in range(i+1,len(uniqueChar)):
            
            #Transform the string in all the possible combination
            stringTransform = s
            char1 = uniqueChar[i]
            char2 = uniqueChar[j]
            
            for char in uniqueChar:
                if(char != char1 and char != char2):
                    stringTransform = re.sub(char,"",stringTransform)
            
            #To see if the new String is has alternating characters
            if (stringTransform[0] == char1):
                firstChar = char1
                secondChar = char2
            else:
                firstChar = char2
                secondChar = char1

            index=0
            alternating = True
            for char in stringTransform:
                if (index%2 == 0):
                    if(char != firstChar):
                        alternating = False
                        break
                else:
                    if(char != secondChar):
                        alternating = False
                        break
                index += 1
            
            if (alternating):
                if(len(stringTransform) > maxLength):
                    maxLength = len(stringTransform)
    
    return(maxLength)
                    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
