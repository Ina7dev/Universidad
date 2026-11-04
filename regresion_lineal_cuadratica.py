#x: 1, 2, 3, 4, 5, 6, 7
#y: 0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5
#y = a0 + a1 x + a2 x^2

import os
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Cuantos datos son?: "))
x = []
y = []

#sumatorias
suma_x = 0
suma_x2 = 0  
suma_x3 = 0  #nueva
suma_x4 = 0  #nueva
suma_y = 0
suma_xy = 0
suma_x2y = 0  #nueva

#recorre los datos y los va sumando
for i in range(n):
    xi = float(input("x" + str(i + 1) + ": "))
    yi = float(input("y" + str(i + 1) + ": "))
    x.append(xi)
    y.append(yi)

    suma_x = suma_x + xi
    suma_x2 = suma_x2 + xi ** 2  
    suma_x3 = suma_x3 + xi ** 3  #nueva
    suma_x4 = suma_x4 + xi ** 4  #nueva
    suma_y = suma_y + yi
    suma_xy = suma_xy + xi * yi
    suma_x2y = suma_x2y + xi ** 2 * yi  #nueva

#matriz del sistema
A = np.array([[n,       suma_x,  suma_x2],
              [suma_x,  suma_x2, suma_x3],
              [suma_x2, suma_x3, suma_x4]])

#lado derecho
b = np.array([suma_y, suma_xy, suma_x2y])

print("matriz A:")
print(A)

print("vector b:")
print(b)

#resuelve el sistema A * a = b
a = np.linalg.solve(A, b)
a_0 = a[0]
a_1 = a[1]
a_2 = a[2]

print("a_0 =", a_0)
print("a_1 =", a_1)
print("a_2 =", a_2)
print("y =", round(a_0, 4), "+", round(a_1, 4), "x +", round(a_2, 4), "x^2")

#grafico
xx = np.linspace(min(x), max(x), 300)

plt.plot(x, y, 'ko', label='datos')
plt.plot(xx, a_0 + a_1 * xx + a_2 * xx ** 2, label='polinomio grado 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(); plt.grid()

os.makedirs("figuras", exist_ok=True)
plt.savefig(os.path.join("figuras", "regresion_polinomica.png"))

plt.show()

#comparo con polyfit
print("polyfit:", np.polyfit(x, y, 2))