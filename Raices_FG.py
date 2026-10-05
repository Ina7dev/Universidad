## encontrar raíces con fórmula general 
 
import cmath
import math


a = int(input("Ingrese A:"))
b = int(input("Ingrese B:"))
c = int(input("Ingrese C:"))

Contenido = ((b**2) - (4*a*c))

if Contenido >= 0:
    Raiz1 = ((-b + math.sqrt(Contenido)) / (2*a))
    Raiz2 = ((-b - math.sqrt(Contenido)) / (2*a))
    print("Raiz 1: ", int(Raiz1))
    print("Raiz 2: ", int(Raiz2))
    print("Raiz 1.2: ", -b, "+ r", "(",Contenido,")", "/", 2*a)
    print("Raiz 2.1: ", -b, "- r", "(",Contenido,")", "/", 2*a)
else:
    Raiz1_compleja = ((-b + cmath.sqrt(Contenido)) / (2*a))
    Raiz2_compleja = ((-b - cmath.sqrt(Contenido)) / (2*a))
    print("Raiz 1 compleja: ", Raiz1_compleja)
    print("Raiz 2 compleja: ", Raiz2_compleja)
    print("Raiz 1.2 compleja: ", -b, "+ r", "(",Contenido,")", "/", 2*a)
    print("Raiz 2.1 compleja: ", -b, "- r", "(",Contenido,")", "/", 2*a)
