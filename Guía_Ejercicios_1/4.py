from math import sqrt

a = 10
valor_verdadero = sqrt(a)  # valor verdadero de raíz de 10
cifras = 6
error_tolerado = 0.5 * 10 ** (2 - cifras)  # criterio de Scarborough en %


def heron(x0, iteraciones):
    """Hace un número fijo de iteraciones y muestra el error en cada paso."""
    x = x0
    print(f"{'Iteración':>9} {'x_n':>16} {'Error verdadero %':>18}")
    for n in range(1, iteraciones + 1):
        x = 0.5 * (x + a / x)
        error_verdadero = abs((valor_verdadero - x) / valor_verdadero) * 100
        print(f"{n:>9} {x:>16.10f} {error_verdadero:>18.4e}")
    return x


def iteraciones_necesarias(x0):
    """Itera hasta que el error sea menor a la tolerancia de 6 cifras."""
    x = x0
    n = 0
    error_verdadero = 100
    error_aprox = 100
    it_verdadero = None
    print(f"{'Iteración':>9} {'x_n':>16} {'Error verdadero %':>18} {'Error aprox %':>15}")
    while error_aprox >= error_tolerado:
        anterior = x
        x = 0.5 * (x + a / x)
        n += 1
        error_verdadero = abs((valor_verdadero - x) / valor_verdadero) * 100
        error_aprox = abs((x - anterior) / x) * 100
        print(f"{n:>9} {x:>16.10f} {error_verdadero:>18.4e} {error_aprox:>15.4e}")
        if it_verdadero is None and error_verdadero < error_tolerado:
            it_verdadero = n
    print(f"-> Con el error verdadero se cumplen las 6 cifras en la iteración {it_verdadero}")
    print(f"-> Con el error aproximado el programa se detiene en la iteración {n}")
    return it_verdadero, n


print(f"Valor verdadero raíz de {a}: {valor_verdadero}")
print(f"Error tolerado (6 cifras): {error_tolerado} %")

print("\n===== a) x0 = 3, 4 iteraciones =====")
heron(3, 4)

print("\n===== b) Iteraciones para 6 cifras significativas (x0 = 3) =====")
iteraciones_necesarias(3)

print("\n===== c) x0 = 10 =====")
iteraciones_necesarias(10)