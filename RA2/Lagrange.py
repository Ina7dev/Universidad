#(0, 1), (1, 3), (2, 2)

import os
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Cuantos datos son?: "))
x = []
y = []

#pide los pares ordenados
for i in range(n):
    x.append(float(input("x" + str(i) + ": ")))
    y.append(float(input("y" + str(i) + ": ")))

#calcula el polinomio de lagrange
p = np.poly1d([0])

for i in range(n):
    L = np.poly1d([1])
    for j in range(n):
        if j != i:
            L = L * np.poly1d([1, -x[j]]) / (x[i] - x[j])
    p = p + y[i] * L

print("polinomio:")
print(p)

xe = float(input("Valor de x para evaluar: "))
print("p(" + str(xe) + ") =", p(xe))

#grafico
xx = np.linspace(min(x), max(x), 300)

plt.plot(x, y, 'ko', label='datos')
plt.plot(xx, p(xx), label='lagrange')
plt.legend(); plt.grid()

os.makedirs("figuras", exist_ok=True)
plt.savefig(os.path.join("figuras", "interpolacion_lagrange.png"))

plt.show()  
