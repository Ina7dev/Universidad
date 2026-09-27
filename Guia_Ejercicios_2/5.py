from math import sin
import numpy as np
import matplotlib.pyplot as plt


def biseccion(f, xl, xu, es=None, iteraciones=None, valor_verdadero=None):
    """Método de bisección. Se detiene por número de iteraciones o cuando ea < es."""
    print(f"{'It':>3} {'xl':>10} {'xu':>10} {'xr':>10} {'f(xr)':>11} {'ea %':>9} {'et %':>9}")
    xr_anterior = None
    n = 0
    while True:
        n += 1
        xr = (xl + xu) / 2

        if xr_anterior is None:
            ea = None
        else:
            ea = abs((xr - xr_anterior) / xr) * 100

        et = abs((valor_verdadero - xr) / valor_verdadero) * 100 if valor_verdadero else None

        texto_ea = f"{ea:>9.4f}" if ea is not None else f"{'---':>9}"
        texto_et = f"{et:>9.4f}" if et is not None else f"{'---':>9}"
        print(f"{n:>3} {xl:>10.6f} {xu:>10.6f} {xr:>10.6f} {f(xr):>11.6f} {texto_ea} {texto_et}")

        # se elige el subintervalo donde cambia el signo
        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            break  # f(xr) = 0, raíz exacta

        xr_anterior = xr
        if iteraciones is not None and n >= iteraciones:
            break
        if es is not None and ea is not None and ea < es:
            break
    return xr


def graficar(f, a, b, titulo, archivo):
    x = np.linspace(a, b, 1000)
    y = [f(valor) for valor in x]
    plt.figure(figsize=(7, 4))
    plt.plot(x, y, label="f(x)")
    plt.axhline(0, color="black", linewidth=0.8)  # eje x, donde están las raíces
    plt.title(titulo)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.savefig(archivo, dpi=120, bbox_inches="tight")
    plt.show()


# EJERCICIO 5
f5 = lambda x: sin(x) - x**2  # sen(x) = x²  ->  sen(x) - x² = 0

graficar(f5, -0.5, 1.5, "Ejercicio 5: f(x) = sen(x) - x²", "ej5.png")

print("Bisección [0.5, 1] con es = 2 %")
raiz5 = biseccion(f5, 0.5, 1, es=2, valor_verdadero=0.876726215)

print(f"Prueba de error con x = {raiz5}:")
print(f"  sen(x) = {sin(raiz5):.6f}")
print(f"  x²     = {raiz5**2:.6f}")
print(f"  diferencia sen(x) - x² = {f5(raiz5):.6f}")