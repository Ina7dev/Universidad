#(0, 1), (1, 3), (2, 2)

import os
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Cuantos datos son?: "))
x = []
y = []

#pide los pares ordenados
for i in range(n):
    xi = float(input("x" + str(i) + ": "))
    yi = float(input("y" + str(i) + ": "))
    x.append(xi)
    y.append(yi)

#matriz de vandermonde
#cada fila es 1, x, x^2, x^3... de un punto
mv = []

for i in range(n):
    fila = []
    for j in range(n):
        fila.append(x[i] ** j)
    mv.append(fila)

print("matriz de vandermonde:")
for fila in mv:
    print(fila)

print("vector y:")
print(y)

#resuelve el sistema mv * a = y
a = np.linalg.solve(mv, y)

for i in range(n):
    print("a_" + str(i) + " =", a[i])

#muestra el polinomio
polinomio = "p(x) = " + str(round(a[0], 4))

for i in range(1, n):
    if a[i] >= 0:
        polinomio = polinomio + " + " + str(round(a[i], 4)) + "x^" + str(i)
    else:
        polinomio = polinomio + " - " + str(round(-a[i], 4)) + "x^" + str(i)

print(polinomio)

#grafico
xx = np.linspace(min(x), max(x), 300)

#arma el polinomio sumando cada termino
yy = 0
for i in range(n):
    yy = yy + a[i] * xx ** i

plt.plot(x, y, 'ko', label='datos')
plt.plot(xx, yy, label='polinomio interpolador')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(); plt.grid()

os.makedirs("figuras", exist_ok=True)
plt.savefig(os.path.join("figuras", "interpolacion_vandermonde.png"))

plt.show()

#comparo con polyfit
print("polyfit:", np.polyfit(x, y, n - 1))

