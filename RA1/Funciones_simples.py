import math
#funcion simple de ax + b = 0
"""a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

if a != 0:
    x = -b / a
    print(f"La solución de {a}x + {b} = 0 es: x = {x}")
else:
    print("El valor de la a no puede ser 0.")"""
    
# funcion cuadratica ax^2 + bx + c = 0

a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))
c = int(input("Ingresa el valor de c: "))

if a == 0:
    print("El valor de la a no puede ser 0")
else:
    discriminante = b**2 - 4 * a * c

    #Muestra la formula para cualquier caso
    formula_x1 = f"(-({b}) - √{discriminante}) / {2*a}"
    formula_x2 = f"(-({b}) + √{discriminante}) / {2*a}"

    #valor de las x en formula
    print(f"x1 = {formula_x1}")
    print(f"x2 = {formula_x2}")

    if discriminante < 0:
        print("La ecuación no tiene solución real")
    else:
        raiz = math.sqrt(discriminante)

        x_1 = (-b - raiz) / (2 * a)
        x_2 = (-b + raiz) / (2 * a)

        # valor de las x
        print(f"   x1 = {x_1}")
        print(f"   x2 = {x_2}")