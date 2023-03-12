import sys
from typing import List
import sys

class Queue:
    def __init__(self, queue):
        self.queue = queue

    def push(self, x):
        self.queue.append(x)

    def pull(self):
        first = self.queue[0]
        self.queue = self.queue[1:]
        return first

    def size(self):
        return len(self.queue)

def winner1(card1: Queue, card2: Queue, p1: int, p2: int)->Queue:
    card1.push(p1)
    card1.push(p2)
    return card1, card2

def winner2(card1: Queue, card2: Queue, p1: int, p2: int)->Queue:
    card2.push(p1)
    card2.push(p2)
    return card1, card2


def game(player1: List[int], player2: List[int])->str:
    player1 = Queue(player1)
    player2 = Queue(player2)
    i = 0
    while player1.size() and player2.size():
        p1 = player1.pull()
        p2 = player2.pull()
        if p1 == 9 and p2 == 0:
            player1, player2 = winner2(player1, player2, p1, p2)
        elif p1 == 0 and p2 == 9:
            player1, player2 = winner1(player1, player2, p1, p2)
        elif p1 > p2:
            player1, player2 = winner1(player1, player2, p1, p2)
        else:
            player1, player2 = winner2(player1, player2, p1, p2)
        if i == 10 ** 6:
            return "botva"
        i += 1
    return f"first {i}" if player1.size() else f"second {i}"



if __name__ == '__main__':
    player1 = list(map(int, sys.stdin.readline().split()))
    player2 = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(game(player1, player2))


