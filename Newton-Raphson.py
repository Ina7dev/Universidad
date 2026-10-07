import math 

def f(x):
    return math.exp(-x) - x   #funcion inicial e^-x -x

def derivada(x):
    return -math.exp(-x) - 1  #derivada de funcion inicial -e^-x - 1

x = 0

for i in range(5):
    x = x-f(x) /derivada(x)
    print(x)