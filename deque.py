# push_front n
# Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.
#
# push_back n
# Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.
#
# pop_front
# Извлечь из дека первый элемент. Программа должна вывести его значение.
#
# pop_back
# Извлечь из дека последний элемент. Программа должна вывести его значение.
#
# front
# Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.
#
# back
# Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.
#
# size
# Вывести количество элементов в деке.
#
# clear
# Очистить дек (удалить из него все элементы) и вывести ok.
#
# exit
# Программа должна вывести bye и завершить работу.
# Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением операций pop_front, pop_back, front, back программа должна проверять, содержится ли в деке хотя бы один элемент. Если во входных данных встречается операция pop_front, pop_back, front, back, и при этом дек пуст, то программа должна вместо числового значения вывести строку error.

class Deque:
    def __init__(self):
        self.deque = []

    def push_b(self, val):
        self.deque.append(val)
        return 'ok'

    def push_f(self, val):
        self.deque = [val] + self.deque
        return 'ok'

    def front(self):
        if any(self.deque):
            return self.deque[0]
        return 'error'

    def back(self):
        if any(self.deque):
            return self.deque[-1]
        return 'error'

    def size(self):
        return len(self.deque)

    def clear(self):
        self.deque = []
        return 'ok'

    def pop_front(self):
        if any(self.deque):
            f = self.deque[0]
            self.deque = self.deque[1:]
            return f
        return 'error'

    def pop_back(self):
        if any(self.deque):    
            l = self.deque[-1]
            self.deque.pop()
            return l
        return 'error'

    def exit(self):
        return "bye"

if __name__=='__main__':
    deque = Deque()
    while True:
        move = input().split()
        if move[0] == 'push_front':
            print(deque.push_f(move[1]))
        elif move[0] == 'push_back':
            print(deque.push_b(move[1]))
        elif move[0] == 'exit':
            print(deque.exit())
            break
        elif move[0] == 'back':
            print(deque.back())
        elif move[0] == 'front':
            print(deque.front())
        elif move[0] == 'size':
            print(deque.size())
        elif move[0] == 'clear':
            print(deque.clear())
        elif move[0] == 'pop_front':
            print(deque.pop_front())
        elif move[0] == 'pop_back':
            print(deque.pop_back())


