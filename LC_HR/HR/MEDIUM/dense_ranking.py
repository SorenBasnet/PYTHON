import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):

    return_list = []

    for score in player:

        ranked.append(score)
        ranked = set(ranked)
        ranked = list(ranked)
        ranked.sort(reverse=True)

        index_map = {v: i for i, v in enumerate(ranked)}

        print(f"index_map: {index_map}")

        return_list.append(index_map[score])


        """
        for i in range(len(ranked)):
            ranked = list(ranked)
            ranked.sort(reverse=True)
            if ranked[i] == score:
                return_list.appen(i+1)

        """

    return return_list


if __name__ == '__main__':

    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    result = climbingLeaderboard(ranked, player)

    print(result)
