import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return -25 + 82 * x - 90 * x**2 + 44 * x**3 - 8 * x**4 + 0.7 * x**5


# a) grafico, entre 0 y 2 se ve bien donde corta
x = np.linspace(0, 2, 200)
plt.plot(x, f(x))
plt.axhline(0, color="black")  # eje x
plt.title("f(x) = -25 + 82x - 90x² + 44x³ - 8x⁴ + 0.7x⁵")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# b) biseccion con error tolerado de 10%
print("Biseccion")
xl = 0.5
xu = 1.0
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

# c) falsa posicion con error tolerado de 0.2%
print("\nFalsa posicion")
xl = 0.5
xu = 1.0
error_tolerado = 0.2
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