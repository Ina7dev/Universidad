import sympy as sp

x = sp.symbols("x")

funcion = (x - 1)**2 * (x + 2)
derivada = sp.diff(funcion, x)

print(f"f(x) = {funcion}")
print(f"f'(x) = {derivada}")

# a) newton-raphson con x0 = 2
xi = 2
error_relativo = 0.1
error = 100
iteraciones = 0

print(f"\n{'i':>3} {'xi':>14} {'error %':>12}")
while error > error_relativo:
    x_nuevo = xi - float(funcion.subs(x, xi)) / float(derivada.subs(x, xi))
    error = abs((x_nuevo - xi) / x_nuevo) * 100
    xi = x_nuevo
    iteraciones += 1
    print(f"{iteraciones:>3} {xi:>14.9f} {error:>12.6f}")

print(f"\nRaíz aproximada: {xi:.9f} en {iteraciones} iteraciones")

# la derivada tambien vale cero en x = 1, por eso avanza lento
print(f"f'(1) = {derivada.subs(x, 1)}")

# b) se revisa si hay cambio de signo alrededor de x = 1
a = 0.5
b = 1.5
print(f"\nf({a}) = {float(funcion.subs(x, a))}")
print(f"f({b}) = {float(funcion.subs(x, b))}")

if float(funcion.subs(x, a)) * float(funcion.subs(x, b)) < 0:
    print("Hay cambio de signo, se puede usar bisección")
else:
    print("No hay cambio de signo, no se puede usar bisección")