# https://www.hackerrank.com/challenges/strong-password/

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    number = 0
    if (n < 6):
        number += 6-n
    
    missingDigit = True
    missingLowerCase = True
    missingUpperCase = True
    missingSpecialChar = True
    special_characters = "!@#$%^&*()-+"
    
    for letter in password:
        if (letter.isdigit()):
            missingDigit = False
        if (letter.isupper()):
            missingUpperCase = False
        if (letter.islower()):
            missingLowerCase = False
        if (letter in special_characters):
            missingSpecialChar = False
    
    otherNumber = missingDigit + missingLowerCase + missingUpperCase + missingSpecialChar
    
    return max(number,otherNumber)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
