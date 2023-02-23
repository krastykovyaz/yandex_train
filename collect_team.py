from typing import List
from collections import defaultdict


def get_team(players: List[int])->List[int]:
    bestsum = 0
    nowsum = 0
    last = 0
    for first in range(len(players)):
        while last < len(players) and (last == first or players[first] + players[first + 1] >= players[last]):
            nowsum += players[last]
            last += 1
        bestsum = max(bestsum, nowsum)
        nowsum -= players[first]
    return bestsum


if __name__ == '__main__':
    arr = [1, 3, 4, 6, 11]
    print(get_team(arr))
