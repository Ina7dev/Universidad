""" 1.- Calcular el perimetro de
un circulo de radio r
(perimetro=2*pi*r). Ingresar el 
valor por consola"""
'''import math

r = float(input("Ingresa el valor del radio del circulo: "))

perimetro = 2 * math.pi * r

print(f"El valor del perimetro es de: {float(perimetro)}")'''

""" 2.- Determinar si un
estudiante esta aprobado o
reprobado de acuerdo a la siguiente
ponderacion.
N_F = P1*0,2+P2*0,6+t*0,1+ppt*0,1
El estudiante aprueba si tiene nota
mayor o igual a 4.0 y en caso
contrario reprueba. El usuario debe
ingresar las notas."""

#Se le da la instruccion al usuario.
#print("Ingresa tus notas segun como se vayan solicitando para calcular la nota final\n")

#Se piden los datos al usuario
'''nota_1 = float(input("Ingresa tu primer nota: "))
nota_2 = float(input("Ingresa tu segunda nota: "))
nota_tarea = float(input("Ingresa la nota de la tarea: "))
nota_ppt = float(input("Ingresa la nota del ppt: "))

#Se realiza el calculo
nota_final = nota_1 * 0.2 + nota_2 * 0.6 + nota_tarea * 0.1 + nota_ppt * 0.1

#Se le avisa si reprobo o no
if nota_final >= 4.0:
    print(f"Has aprobado con nota {nota_final:.2f}")
else:
    print(f"Has reprobado con nota {nota_final:.2f}")'''

""" 3.- Crear un algoritmo que permita leer 2 números. Si son iguales se deben multiplicar, si el
primero es mayor que el segundo se deben restar, sino se deben sumar. Los valores deben
inicializarse en el código."""

'''numero_1 = int(input("Ingresa el primer numero: "))
numero_2 = int(input("Ingresa el segundo numero: "))

multiplicacion = numero_1 * numero_2
resta = numero_1 - numero_2
suma = numero_1 + numero_2

if numero_1 == numero_2:
    print(f"Los numeros son iguales, resultado de la multiplicaion: {multiplicacion}")
if numero_1 > numero_2:
    print(f"El primer numero es mayor, resultado de la resta: {resta}")
if numero_1 != numero_2 and numero_1 < numero_2:
    print(f"Los numeros no son iguales y el primero no es mayor, Resultado de la suma: {suma}")'''

"""Desarrollar un algoritmo que permita ingresar un número de 7 dígitos y que muestre los
dígitos impares de dicho número, y la suma de los dígitos pares.
"""

# Solicitar al usuario que ingrese un número de 7 dígitos
numero = input("Ingresa un número de 7 dígitos: ")

# Verificar si el número tiene 7 dígitos
if len(numero) != 7:
    print("El número ingresado no tiene 7 dígitos.")
else:
    impares = []
    suma_pares = 0

    # Iterar sobre cada dígito del número
    for digito in numero:
        digito_int = int(digito)
        if digito_int % 2 != 0:
            impares.append(digito_int)
        else:
            suma_pares += digito_int

    # Mostrar los resultados
    print(f"Dígitos impares: {impares}")
    print(f"Suma de los dígitos pares: {suma_pares}")
