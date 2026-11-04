#x: 1, 2, 3, 4, 5, 6, 7
#y: 0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5
#y = asub0 + asub1 x
"""asub1 = n sumatoria(xsubi ysubi) - sumatoria (xsubi) sumatoria (ysubi) / n sumatoria(xsubi^2) - (sumatoria(xsubi))^2

asub0 = ȳ -asub1 x̄

n= numero de datos."""

import numpy as np
import matplotlib.pyplot as plt
import os


n = int(input("Cuantos datos son?: "))
x = []
y = []

#sumatorias
suma_x = 0
suma_y = 0
suma_xy = 0
suma_x2 = 0

#recorre los datos y los va sumando

for i in range(n):
    xi = float(input("x" + str(i + 1) + ": "))
    yi = float(input("y" + str(i + 1) + ": "))
    x.append(xi)
    y.append(yi)
    
    #aqui comienza a sumar
    suma_x = suma_x + xi
    suma_y = suma_y + yi
    suma_xy = suma_xy + xi * yi
    suma_x2 = suma_x2 + xi ** 2
    
#promedio

promedio_x = suma_x / n
promedio_y = suma_y / n

#formulas
a_1 = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x ** 2)
a_0 = promedio_y - a_1 * promedio_x

print("a_1 =", a_1)
print("a_0 =", a_0)
print("y =", round(a_0, 4), "+", round(a_1, 4), "x")


#codigo para ver la recta

# puntos para dibujar la recta
xx = np.linspace(min(x), max(x), 300)

plt.plot(x, y, 'ko', label='datos')
plt.plot(xx, a_0 + a_1 * xx, label='recta de regresion')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(); plt.grid()

os.makedirs("figuras", exist_ok=True)
plt.savefig(os.path.join("figuras", "regresion_lineal.png"))

plt.show()

# comparo con polyfit para ver si da lo mismo
print("polyfit:", np.polyfit(x, y, 1))