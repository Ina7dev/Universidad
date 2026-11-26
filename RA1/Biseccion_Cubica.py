import numpy as np
import matplotlib.pyplot as plt


def f(c):
    return c**3 + c + 1

# primero el grafico para ver por donde corta el eje
c = np.linspace(-2, 2, 400)
plt.plot(c, f(c), color='#065A82')
plt.axhline(0, color='gray', lw=0.8)
plt.xlabel('c'); plt.ylabel('f(c)')
plt.grid(alpha=0.3)
plt.show()

xl = float(input("Ingresa xl: "))
xu = float(input("Ingresa xu: "))

if f(xl) * f(xu) > 0:
    print("No hay cambio de signo, prueba con otro intervalo")
else:
    xr_anterior = 0
    for i in range(10):
        xr = (xl + xu) / 2

        if i == 0:
            print(f"Iteracion {i + 1}: xl = {xl}  xu = {xu}  xr = {xr}  f(xr) = {f(xr)}")
        else:
            error = abs((xr - xr_anterior) / xr) * 100
            print(f"Iteracion {i + 1}: xl = {xl}  xu = {xu}  xr = {xr}  f(xr) = {f(xr)}  error: {error}%")

        # se revisa en que mitad queda la raiz
        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr
        xr_anterior = xr

    print("Raiz aproximada:", xr)