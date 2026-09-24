#POTENCIA

import math

estatura = 1.70
peso = 70
imc = peso / (estatura ** 2) 
print(math.trunc(imc))

#BOOLEANOS
print("####### 0.3 #######\n")
ampolleta = False
interruptor = True

#FUNCION TYPE

print(type(ampolleta),type (interruptor))
print(type(imc))
print(type(peso))

#SALIDAS BOOLEANAS

print(1 <= 0)
print(100 >= 10)
print(19 == 19)

#FUNCION BOOL

print(bool(0))
print(bool(1))

#LISTAS

ciudades = ["Castro", "Queilen", "Ancud", "Quellón", "Chonchi", "Castro"]
varios = ["Nicolas", 20, True]

list()
print(type(ciudades))
print(ciudades)

print(len(ciudades)) #cuenta la cantidad de elementos de una lista

print(ciudades.count("Castro")) #cuenta la cantidad de ocurrencias de una lista

#Impre4sion de un elemnto en especifico de una lista
print(ciudades[3])


#5. DUPLAS

basica = tuple()
generos = ("rock", "Blues", "Pop")
print(generos)
print(type(generos))

print(generos[2])