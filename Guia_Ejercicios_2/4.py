import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -12 - 21 * x + 18 * x**2 - 2.75 * x**3


# a) grafico
x = np.linspace(-1.5, 6, 200)
plt.plot(x, f(x))
plt.axhline(0, color="black")  # eje x
plt.title("f(x) = -12 - 21x + 18x² - 2.75x³")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# b) falsa posicion para la raiz mas pequeña, en el grafico se ve que esta entre -1 y 0
xl = -1
xu = 0
error_tolerado = 0.5 * 10 ** (2 - 3)  # para 3 cifras significativas
xr_anterior = 0
error_aprox = 100
iteracion = 0

while error_aprox > error_tolerado:
    iteracion += 1
    xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))

    if iteracion == 1:
        print(f"Iteracion {iteracion}: xl = {xl}  xu = {xu}  xr = {xr}")
    else:
        error_aprox = abs((xr - xr_anterior) / xr) * 100
        print(f"Iteracion {iteracion}: xl = {xl}  xu = {xu}  xr = {xr}  Error aproximado: {error_aprox}")

    # se revisa en que lado queda la raiz
    if f(xl) * f(xr) < 0:
        xu = xr
    else:
        xl = xr
    xr_anterior = xr

print(f"Raiz aproximada: {xr}")