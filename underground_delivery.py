import sys
from collections import Counter

class Train:
    def __init__(self):
        self.stack = []


    def add(self, n, name):
        add_cur = [name] * n
        self.stack = self.stack + add_cur

    def delete(self, n):
        self.stack = self.stack[:-n]

    def get(self, name):
        counter = Counter(self.stack)
        sys.stdout.write(str(counter[name]))
        sys.stdout.write('\n')

if __name__=='__main__':
    t = Train()
    n = int(sys.stdin.readline())
    for _ in range(n):
        op = sys.stdin.readline().split()
        if op[0] == 'add':
            t.add(int(op[1]), op[2])
        elif op[0] == 'delete':
            t.delete(int(op[1]))
        elif op[0] == 'get':
            t.get(op[1])