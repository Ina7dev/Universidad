import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (0.8 - 0.3 * x) / x


# a) analiticamente, 0.8 - 0.3x = 0 entonces x = 0.8/0.3
valor_verdadero = 0.8 / 0.3
print(f"Raiz analitica: {valor_verdadero}")

# b) grafico
x = np.linspace(0.5, 5, 200)
plt.plot(x, f(x))
plt.axhline(0, color="black")  # eje x
plt.title("f(x) = (0.8 - 0.3x) / x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# c) falsa posicion con 3 iteraciones
xl = 1
xu = 3
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