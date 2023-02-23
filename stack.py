import sys
class Stack:
    def __init__(self):
        self.stack_abstract = []

    def get_size(self):
        return str(len(self.stack_abstract))

    def push_ok(self, n):
        self.stack_abstract.append(n)
        return 'ok'

    def get_back(self):
        return str(self.stack_abstract[-1])

    def get_pop(self):
        last = self.stack_abstract[-1]
        self.stack_abstract.pop()
        return str(last)

    def get_clear(self):
        self.stack_abstract =[]
        return 'ok'


if __name__=='__main__':
    stack = Stack()
    while True:
        row = (sys.stdin.readline()).split()
        command = row[0]
        if command == 'exit':
            sys.stdout.write('bye')
            sys.stdout.write('\n')
            break
        elif command == 'size':
            sys.stdout.write(stack.get_size())
            sys.stdout.write('\n')
        elif command == 'push':
            sys.stdout.write(stack.push_ok(row[1]))
            sys.stdout.write('\n')
        elif command == 'back':
            sys.stdout.write(stack.get_back())
            sys.stdout.write('\n')
        elif command == 'pop':
            sys.stdout.write(stack.get_pop())
            sys.stdout.write('\n')
        elif command == 'clear':
            sys.stdout.write(stack.get_clear())
            sys.stdout.write('\n')
