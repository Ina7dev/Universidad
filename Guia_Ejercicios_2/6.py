from math import exp
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log(x**2) - 0.7


# a) grafico
x = np.linspace(0.2, 3, 200)
plt.plot(x, f(x))
plt.axhline(0, color="black")  # eje x
plt.title("f(x) = ln(x²) - 0.7")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# despejando queda x = e^0.35
valor_verdadero = exp(0.35)
print(f"Valor verdadero: {valor_verdadero}")

# b) biseccion con 3 iteraciones
print("Biseccion")
xl = 0.5
xu = 2
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

# c) falsa posicion con 3 iteraciones
print("\nFalsa posicion")
xl = 0.5
xu = 2
xr_anterior = 0
for i in range(3):
    xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))
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