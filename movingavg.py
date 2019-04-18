from copy import copy

innn = [
    0,0,0,0,0,0,
    1,1,1,1,1,1,
    1,1,1,1,1,1,
    1,1,1,1,1,1,
    0,0,0,0,0,0,
    0,0,0,0,0,0,
    0,0,0,0,0,0,
    1,1,1,1,1,1,
    1,1,1,1,1,1,
    1,1,1,1,1,1,
    0,0,0,0,0,0,
    0,0,0,0,0,0,
    0,0,0,0,0,0,
]

class Moving():
    
    def __init__(self, size = 10):
        self.__sum = 0
        self.__avg = 0
        self.__size = size
        self.__count = 1
        
    def update(self, v):
        self.__sum += v - self.__avg
        self.__avg = self.__sum / min(self.__count, self.__size)
        self.__count += 1
        
    def __float__(self):
        return copy(self.__avg)
    
    def __int__(self):
        return int(self.__avg)

    def __repr__(self):
        return str(self.__avg)

if __name__ == '__main__':
    from random import randint
    import matplotlib.pyplot as plt

    X = []
    Y1 = []
    Y2 = []
    m = Moving()
    for i in range(100):
        x = randint(1, 10)
        m.update(x)
        X += [i]
        Y1 += [x]
        Y2 += [float(m)]
    
    plt.plot(X, Y1)
    plt.plot(X, Y2)

    X = []
    Y1 = []
    Y2 = []
    m = Moving(100)
    for i in range(len(innn)):
        x = innn[i]
        m.update(x)
        X += [i]
        Y1 += [x]
        Y2 += [float(m)]
        print(i, x, m)
    
    plt.plot(Y1)
    plt.plot(Y2)
    print(Y2)