import numpy as np
import matplotlib.pyplot as plt


def falsa_posicion(f, xl, xu, es=None, iteraciones=None, valor_verdadero=None):
    """Método de la falsa posición. Igual que bisección pero xr sale de la recta entre (xl, f(xl)) y (xu, f(xu))."""
    print(f"{'It':>3} {'xl':>10} {'xu':>10} {'xr':>10} {'f(xr)':>11} {'ea %':>9} {'et %':>9}")
    xr_anterior = None
    n = 0
    while True:
        n += 1
        xr = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))

        if xr_anterior is None:
            ea = None
        else:
            ea = abs((xr - xr_anterior) / xr) * 100

        et = abs((valor_verdadero - xr) / valor_verdadero) * 100 if valor_verdadero else None

        texto_ea = f"{ea:>9.4f}" if ea is not None else f"{'---':>9}"
        texto_et = f"{et:>9.4f}" if et is not None else f"{'---':>9}"
        print(f"{n:>3} {xl:>10.6f} {xu:>10.6f} {xr:>10.6f} {f(xr):>11.6f} {texto_ea} {texto_et}")

        if f(xl) * f(xr) < 0:
            xu = xr
        elif f(xl) * f(xr) > 0:
            xl = xr
        else:
            break

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


# EJERCICIO 7
f7 = lambda x: (0.8 - 0.3 * x) / x

graficar(f7, 0.5, 5, "Ejercicio 7: f(x) = (0.8 - 0.3x)/x", "ej7.png")

raiz7 = 0.8 / 0.3  # analíticamente 0.8 - 0.3x = 0
print(f"a) Raíz analítica x = 0.8/0.3 = {raiz7:.6f}")

print("c) Falsa posición [1, 3], 3 iteraciones")
falsa_posicion(f7, 1, 3, iteraciones=3, valor_verdadero=raiz7)