from random import randint

def print_byte(n):
    return format(n, '08b')

def get_parent(i):
    return i + (i & (-i))

def get_child(i):
    return i - (i & (-i))

class Fenwick:
    def __init__(self, size):
        self.size = size
        self.prefix = [0]*(size+1) # 1-indexed

    def calculate(self, index, value, subtract=False):
        i = index
        while i <= self.size:
            self.prefix[i] += value
            if subtract:
                i -= i&(-i)
            else:
                i += i&(-i)

if __name__=="__main__":
    arr = [randint(1, 4) for _ in range(8)]
    print(arr)
    fen = Fenwick(len(arr))
    for i, item in enumerate(arr):
        fen.calculate(i+1, item)

    print(fen.prefix[1:])
