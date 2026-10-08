#Pedir al susuaio ingresar a,b,c,d,e,f(primero mostrando "ax + by = c , dc + ey = f" 
# para que el ususario identifique cuales son las letras y que el programa muestre la solucion

print("Ingresa los valores de A, B y C de la primera ecuacion en el sistema de ecuaciones 2x2: ")
print("Ax + By = C")
a = float(input("Ingresa A: "))
b = float(input("Ingresa B: "))
c = float(input("Ingresa C: "))

print("Ingresa los valores de D, E y F de la segunda ecuacion en el sistema de ecuaciones 2x2: ")
print("Dx + Ey = F")
d = float(input("Ingresa D: "))
e = float(input("Ingresa E: "))
f = float(input("Ingresa F: "))

determinante = b*d - e*a
determinante_x = b*f - e*c
determinante_y = d*c - a*f

if determinante != 0:
    x = determinante_x / determinante
    y = determinante_y / determinante
    
    print("El sistema tiene solucion unica")
    print(f"x = {x}")
    print(f"y = {y}")
elif determinante_x == 0 and determinante_y == 0:
    print("Tiene infinitas soluciones")
else:
    print("No tiene solucion")