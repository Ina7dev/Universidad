import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 5 * x**3 - 5 * x**2 + 6 * x - 2


# a) grafico
x = np.linspace(-0.5, 1.5, 200)
plt.plot(x, f(x))
plt.axhline(0, color="black")  # eje x
plt.title("f(x) = 5x³ - 5x² + 6x - 2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# b) biseccion hasta que el error aproximado sea menor que 10%
xl = 0
xu = 1
error_tolerado = 10
xr_anterior = 0
error_aprox = 100
iteracion = 0

while error_aprox > error_tolerado:
    iteracion += 1
    xr = (xl + xu) / 2

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