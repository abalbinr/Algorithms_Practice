# https://www.hackerrank.com/challenges/climbing-the-leaderboard

#!/bin/python3

import math
import os
import random
import re
import sys

def climbingLeaderboard(ranked, player):
    rankingPlayer = []
    uniqueRanked = list(set(ranked))
    uniqueRanked = sorted(uniqueRanked)
    
    rank = len(uniqueRanked) + 1
    index = 0
    for score in player:
        find = False
        while (not(find)):
            if (index < len(uniqueRanked)):
                currentRanked = uniqueRanked[index]
                if(score < currentRanked):
                    find = True
                else:
                    rank -= 1
                    index += 1
            else:
                find = True
            

        
        rankingPlayer += [rank]
        
        
    
    return rankingPlayer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
