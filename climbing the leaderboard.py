#!/bin/python3

import sys

def climbingLeaderboard(ranked, player):
    # remove duplicates and sort descending
    scores = sorted(set(ranked), reverse=True)
    result = []
    n = len(scores)
    i = n - 1  # start from the lowest rank in scores
    
    for p in player:
        while i >= 0 and p >= scores[i]:
            i -= 1
        result.append(i + 2)  # rank is index+2 because rank starts at 1
    return result


if __name__ == '__main__':
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
