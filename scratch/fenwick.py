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
    # res = [0]*(len(arr)+1)
    fen = Fenwick(len(arr))
    for i, item in enumerate(arr):
        fen.calculate(i+1, item)

    print(fen.prefix[1:])
    # for i in range(1, len(arr)-1):
    #     print(
    #         print_byte(i),
    #         print_byte(get_child(i)),
    #         print_byte(get_parent(i)),
    #         str(i).zfill(2),
    #         str((i & (-i))).zfill(2),
    #         arr[i-1]
    #     )
