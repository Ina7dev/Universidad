import sympy as sp

x = sp.symbols("x")

funcion = sp.atan(x)
derivada = sp.diff(funcion, x)

print(f"f(x) = {funcion}")
print(f"f'(x) = {derivada}")

# newton-raphson con x0 = 1
# se hacen 4 iteraciones, en la 5 x llega a 0 y el error divide por cero
xi = 1

print("\nCon x0 = 1")
print(f"{'i':>3} {'xi':>16} {'error %':>18}")
for i in range(4):
    x_nuevo = xi - float(funcion.subs(x, xi)) / float(derivada.subs(x, xi))
    error = abs((x_nuevo - xi) / x_nuevo) * 100
    xi = x_nuevo
    print(f"{i + 1:>3} {xi:>16.9f} {error:>18.6f}")

# newton-raphson con x0 = 1.5
xi = 1.5

print("\nCon x0 = 1.5")
print(f"{'i':>3} {'xi':>16} {'error %':>18}")
for i in range(5):
    x_nuevo = xi - float(funcion.subs(x, xi)) / float(derivada.subs(x, xi))
    error = abs((x_nuevo - xi) / x_nuevo) * 100
    xi = x_nuevo
    print(f"{i + 1:>3} {xi:>16.9f} {error:>18.6f}")

# biseccion en [-1, 2]
# como la raiz es 0 se usa error absoluto en vez de relativo
a = -1
b = 2
anterior = a
error = 1
iteraciones = 0

print("\nBisección en [-1, 2]")
print(f"{'i':>3} {'xr':>16} {'error abs':>18}")
while error > 0.0001:
    xr = (a + b) / 2
    error = abs(xr - anterior)

    if float(funcion.subs(x, a)) * float(funcion.subs(x, xr)) < 0:
        b = xr
    else:
        a = xr

    anterior = xr
    iteraciones += 1
    print(f"{iteraciones:>3} {xr:>16.9f} {error:>18.9f}")

print(f"\nBisección: {xr:.9f} en {iteraciones} iteraciones")