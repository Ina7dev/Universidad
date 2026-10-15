import sympy as sp

x = sp.symbols("x")

funcion = sp.exp(x) - 3*x
derivada = sp.diff(funcion, x)

print(f"f(x) = {funcion}")
print(f"f'(x) = {derivada}")

error_relativo = 0.05

# newton-raphson con x0 = 0
xi = 0
error = 100
iteraciones_newton = 0

print("\nNewton-Raphson")
print(f"{'i':>3} {'xi':>14} {'error %':>12}")
while error > error_relativo:
    x_nuevo = xi - float(funcion.subs(x, xi)) / float(derivada.subs(x, xi))
    error = abs((x_nuevo - xi) / x_nuevo) * 100
    xi = x_nuevo
    iteraciones_newton += 1
    print(f"{iteraciones_newton:>3} {xi:>14.9f} {error:>12.6f}")

# biseccion en [0, 1]
a = 0
b = 1
anterior = a
error = 100
iteraciones_biseccion = 0

print("\nBisección")
print(f"{'i':>3} {'xr':>14} {'error %':>12}")
while error > error_relativo:
    xr = (a + b) / 2
    error = abs((xr - anterior) / xr) * 100

    if float(funcion.subs(x, a)) * float(funcion.subs(x, xr)) < 0:
        b = xr
    else:
        a = xr

    anterior = xr
    iteraciones_biseccion += 1
    print(f"{iteraciones_biseccion:>3} {xr:>14.9f} {error:>12.6f}")

print(f"\nNewton-Raphson: {xi:.9f} en {iteraciones_newton} iteraciones")
print(f"Bisección: {xr:.9f} en {iteraciones_biseccion} iteraciones")