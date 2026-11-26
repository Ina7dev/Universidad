#parqa f() x = x^3- 6x^2 + 11x - 6 
#aplicar metodo de biseccion y metodo newton
#y comparar ¿cuantas iteraciones requiere cada una? error relativo<0.01%?
import sympy as sp

x = sp.symbols("x")

funcion = x**3 - 6*x**2 + 11*x - 6
derivada = sp.diff(funcion, x)

print(f"f(x) = {funcion}")
print(f"f'(x) = {derivada}")

a = float(input("Ingrese el inicio del intervalo: "))
b = float(input("Ingrese el fin del intervalo: "))
xi = float(input("Ingrese el valor inicial para Newton: "))
error_relativo = float(input("Ingrese el error relativo %: "))

#biseccion
anterior = a
error = 100 #parte del 100%
iteraciones_biseccion = 0

print("Bisección")
while error > error_relativo:
    xr = (a + b) / 2  #punto medio
    error = abs((xr - anterior) / xr) * 100

    #si los signos son distintos la raiz esta en la mitad izquierda
    if float(funcion.subs(x, a)) * float(funcion.subs(x, xr)) < 0:
        b = xr
    else:
        a = xr

    anterior = xr
    iteraciones_biseccion += 1
    print(iteraciones_biseccion, xr, error)

#newton-raphson
error = 100
iteraciones_newton = 0

print("\nNewton-Raphson")
while error > error_relativo:
    x_nuevo = xi - float(funcion.subs(x, xi)) / float(derivada.subs(x, xi))  #la formula
    error = abs((x_nuevo - xi) / x_nuevo) * 100
    xi = x_nuevo  #el x_nuevo pasa a ser el actual xi
    iteraciones_newton += 1
    print(iteraciones_newton, xi, error)

print(f"\nBisección: {xr} en {iteraciones_biseccion} iteraciones")
print(f"Newton-Raphson: {xi} en {iteraciones_newton} iteraciones")