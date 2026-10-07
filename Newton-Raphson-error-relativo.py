import sympy as sp

x = sp.symbols("x")

pedir_funcion = input("Ingrese la funcino f(x): ") #funcin como texto
funcion = sp.sympify(pedir_funcion) #texto pasad a funcion
derivada = sp.diff(funcion, x)  #diff es para q derive sola

print(f"f(x) = {funcion}")
print(f"f'(x) = {derivada}")

xi = float(input("Ingrese el valor inicial: "))
error_relativo = float(input("Ingrese el error relativo %: "))

error = 100 #parte del  100%

with error > error_relativo:
    x_nuevo = xi - float(funcion.subs(x, xi)) / float(derivada.subs(x, xi))  #la formula
    error = abs((x_nuevo - xi) / x_nuevo) * 100
    xi = x_nuevo   #el x_nuevo pasa a ser el actual xi
    print(xi, error)

print("Raíz aproximada:", xi)