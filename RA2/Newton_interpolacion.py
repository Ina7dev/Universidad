#interpolacion de newton con diferencias divididas
#con n puntos sale un polinomio de grado n-1 (4 puntos = cubico)

import os
import numpy as np
import matplotlib.pyplot as plt


def dif_divididas(x, y):
    #devuelve los coeficientes b_k de newton (diagonal de la tabla)
    n = len(x)
    F = np.zeros((n, n))
    F[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            F[i, j] = (F[i+1, j-1] - F[i, j-1]) / (x[i+j] - x[i])
    return F[0, :]


def newton_eval(x, b, xx):
    #evalua la forma de newton con un esquema tipo horner
    p = b[-1]
    for k in range(len(b) - 2, -1, -1):
        p = p * (xx - x[k]) + b[k]
    return p


n = int(input("Cuantos datos son?: "))
x = []
y = []

#pide los pares ordenados
for i in range(n):
    x.append(float(input("x" + str(i) + ": ")))
    y.append(float(input("y" + str(i) + ": ")))

x = np.array(x)
y = np.array(y)

#coeficientes de newton
b = dif_divididas(x, y)

for k in range(n):
    print("b" + str(k) + " =", b[k])

#arma el polinomio con poly1d (igual que newton_eval pero con polinomios)
p = np.poly1d([b[-1]])
for k in range(n - 2, -1, -1):
    p = p * np.poly1d([1, -x[k]]) + b[k]

print("polinomio de grado", n - 1, ":")
print(p)

#evalua en un valor
xe = float(input("Valor de x para evaluar: "))
print("p(" + str(xe) + ") =", newton_eval(x, b, xe))

#grafico
xx = np.linspace(min(x), max(x), 300)

plt.plot(x, y, 'ko', label='datos')
plt.plot(xx, newton_eval(x, b, xx), label='newton')
plt.legend(); plt.grid()

os.makedirs("figuras", exist_ok=True)
plt.savefig(os.path.join("figuras", "interpolacion_newton.png"))

plt.show()