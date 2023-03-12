import sys
from typing import List

def active_os(oslst: List[List[int]])->int:
    cards = []
    for os_ in oslst:
        if cards:
            tmp_cards = []
            for card in cards:
                if not (card[0] <= os_[1] and os_[0] <= card[1]):
                    tmp_cards.append(card)
            tmp_cards.append(os_)
            cards = tmp_cards
        else:
            cards.append(os_)

    return len(cards)



if __name__=='__main__':
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    items = []
    for _ in range(n):
        items.append(list(map(int, sys.stdin.readline().split())))
    sys.stdout.write(str(active_os(items)))
