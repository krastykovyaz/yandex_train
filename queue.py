# push n
# Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.
#
# pop
# Удалить из очереди первый элемент. Программа должна вывести его значение.
#
# front
# Программа должна вывести значение первого элемента, не удаляя его из очереди.
#
# size
# Программа должна вывести количество элементов в очереди.
#
# clear
# Программа должна очистить очередь и вывести ok.
#
# exit
# Программа должна вывести bye и завершить работу.
# size
# push 1
# size
# push 2
# size
# push 3
# size
# exit
import sys


class Queue_:
    def __init__(self):
        self.queue = []

    def push(self, el):
        self.queue.append(el)
        return 'ok'

    def pop(self):
        first = self.queue[0]
        self.queue = self.queue[1:]
        return first

    def front(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
        return 'ok'

    def exit(self):
        return 'bye'

def fprint(item):
    sys.stdout.write(str(item) + '\n')

if __name__=='__main__':
    move = None
    queue = Queue_()
    while move != 'exit':
        move = sys.stdin.readline().split()
        if move[0] == 'push':
            fprint(queue.push(int(move[1])))
        elif move[0] == 'pop':
            fprint(queue.pop())
        elif move[0] == 'front':
            fprint(queue.front())
        elif move[0] == 'size':
            fprint(queue.size())
        elif move[0] == 'clear':
            fprint(queue.clear())
        elif move[0] == 'exit':
            fprint(queue.exit())
        move = move[0]
