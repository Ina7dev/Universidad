import numpy as np
import matplotlib.pyplot as plt


# sen(x) = x^2 se pasa todo a un lado y queda sen(x) - x^2 = 0
def f(x):
    return np.sin(x) - x**2


# grafico
x = np.linspace(-0.5, 1.5, 200)
plt.plot(x, f(x))
plt.axhline(0, color="black")  # eje x
plt.title("f(x) = sen(x) - x²")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# biseccion hasta que el error aproximado sea menor que 2%
xl = 0.5
xu = 1
error_tolerado = 2
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

# prueba reemplazando el resultado en la ecuacion original
print(f"sen(x) = {np.sin(xr)}")
print(f"x^2 = {xr**2}")
print(f"Diferencia: {np.sin(xr) - xr**2}")