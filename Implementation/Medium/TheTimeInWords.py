# https://www.hackerrank.com/challenges/the-time-in-words

#!/bin/python3

import math
import os
import random
import re
import sys

def timeInWords(h, m):
    timeString = ""
    numberConvert = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
    }
    
    minutesConvert = {
        0: "o' clock",
        15: "quarter past",
        30: "half past",
        45: "quarter to"
    }
    
    if (m == 0):
        timeString = numberConvert[h] + " " + minutesConvert[0]
    elif (m in [15,30]):
        timeString = minutesConvert[m] + " " + numberConvert[h]
    elif (m == 45):
        timeString = minutesConvert[m] + " " + numberConvert[h+1]
    else:
        if (m > 30):
            m = 60 - m
            h = h + 1
            position = "to"
        else:
            position = "past"
        
        if (m == 1):
            timeString = numberConvert[1] + " minute " + position + " " + numberConvert[h]
        elif (m <= 20):
            timeString = numberConvert[m] + " minutes " + position + " " + numberConvert[h]
        elif (m < 30):
            timeString = numberConvert[20] + " " + numberConvert[m - 20] + " minutes "+ position + " " + numberConvert[h]

    
    return timeString

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
