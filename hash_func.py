class Hash:
    def __init__(self):
        self.seq = [[] for _ in range(9)]
        self.delimeter = 10

    def add(self, x):
        self.seq[x % self.delimeter].append(x)

    def find(self, x):
        if x in self.seq[x % self.delimeter]:
            return True
        return False

    def rem(self, x):
        if x in self.seq[x % self.delimeter]:
            self.seq[x % self.delimeter].remove(x)


if __name__=='__main__':
    h = Hash()
    h.add(15)
    h.add(5)
    print(h.find(15))
    print(h.seq)
    h.rem(5)
    print(h.seq)