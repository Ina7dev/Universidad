import math
import sympy as sp


def f(x):
    return math.exp(-x) - x   #funcion inicial e^-x -x

def derivada(x):
    return -math.exp(-x) - 1  #derivada de funcion inicial -e^-x - 1

x = 0

for i in range(5):
    x = x-f(x) /derivada(x)
    print(x)
    
#hacer codigo pedir al ususario ingresar funcion y q pida al usuario
# que ingresa un error, con que error relatico aprox la raiz

