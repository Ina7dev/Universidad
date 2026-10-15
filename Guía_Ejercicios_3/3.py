import sympy as sp

x = sp.symbols("x")

funcion = sp.log(x) + x - 2  # en sympy log es logaritmo natural
derivada = sp.diff(funcion, x)

print(f"f(x) = {funcion}")
print(f"f'(x) = {derivada}")

# newton-raphson con x0 = 1, solo 4 iteraciones
xi = 1

print(f"\n{'i':>3} {'xi':>14} {'error %':>14}")
for i in range(4):
    x_nuevo = xi - float(funcion.subs(x, xi)) / float(derivada.subs(x, xi))
    error = abs((x_nuevo - xi) / x_nuevo) * 100
    xi = x_nuevo
    print(f"{i + 1:>3} {xi:>14.9f} {error:>14.10f}")

# cifras significativas: se busca el n mas grande que cumpla
# error <= 0.5 * 10^(2 - n)
n = 0
while error <= 0.5 * 10**(2 - (n + 1)):
    n += 1

print(f"\nRaíz aproximada: {xi:.9f}")
print(f"Cifras significativas garantizadas: {n}")