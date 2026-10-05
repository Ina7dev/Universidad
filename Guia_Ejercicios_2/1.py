from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -0.5 * x**2 + 2.5 * x + 4.5


# a) grafico para ver donde estan las raices
x = np.linspace(-3, 9, 200)
plt.plot(x, f(x))
plt.axhline(0, color="black")  # eje x
plt.title("f(x) = -0.5x² + 2.5x + 4.5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# b) formula cuadratica
a = -0.5
b = 2.5
c = 4.5
discriminante = b**2 - 4 * a * c
x1 = (-b + sqrt(discriminante)) / (2 * a)
x2 = (-b - sqrt(discriminante)) / (2 * a)
print(f"Raices con la formula: x1 = {x1}  x2 = {x2}")

# c) biseccion con 3 iteraciones para la raiz mas grande
valor_verdadero = x2
xl = 5
xu = 10
xr_anterior = 0
for i in range(3):
    xr = (xl + xu) / 2
    error_verdadero = abs((valor_verdadero - xr) / valor_verdadero) * 100

    if i == 0:
        print(f"Iteracion {i + 1}: xl = {xl}  xu = {xu}  xr = {xr}  Error verdadero: {error_verdadero}")
    else:
        error_aprox = abs((xr - xr_anterior) / xr) * 100
        print(f"Iteracion {i + 1}: xl = {xl}  xu = {xu}  xr = {xr}  Error aproximado: {error_aprox}  Error verdadero: {error_verdadero}")

    # se revisa en que lado queda la raiz
    if f(xl) * f(xr) < 0:
        xu = xr
    else:
        xl = xr
    xr_anterior = xr