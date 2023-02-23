import sys
from typing import List

def path_train(train: List[int]):
    stack = []
    sorted_train = []
    last = None
    for cur in train:
        if stack:
            if stack[-1] < cur:
                while stack and stack[-1] < cur:
                    last = stack[-1]
                    sorted_train.append(stack[-1])
                    stack.pop()
                stack.append(cur)
            elif stack[-1] > cur:
                stack.append(cur)
            else:
                return 'NO'
        else:
            stack.append(cur)
    # if stack and last and last + 1 != stack[0]:
    #     return 'NO'
    # print(last, stack[-1])
    if sorted_train + stack[::-1] != sorted(train):
        return 'NO'
    return 'YES'


if __name__=='__main__':
    n = int(sys.stdin.readline())
    train = list(map(int, sys.stdin.readline().split()))
    sys.stdout.write(path_train(train))

