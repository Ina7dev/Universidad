#ingresar la edad de una persona dentro de 6 categorias
"""
edad no valida <= 0
niño/as <= 12
adolescentes <=17
adulto<=64
adulto mayor <= 120
edad no valida >= 120

"""
edad = int(input("Ingrese su edad: "))

if edad < 0 or edad >= 120:
    categoria = ("Edad no valida")
elif edad > 0 and edad <= 12:
    categoria = ("Es un/a niño/a")
elif edad > 12 and edad <= 17:
    categoria = ("Es un/a adolescente")
elif edad > 17 and edad <= 64:
    categoria = "Es un/a adulto/a"
else:
    categoria = ("Es un/a adulto/a mayor")
print(f"La edad de la persona es de '{categoria}'")

#BUCLES
from colorama import init, Fore

num = 0
print(Fore.RED + "Inicio ciclo N°1")
while num <= 100:
      print(num)
      num = num + 2
      print(f"Cierre de ciclo n°1 {Fore.RED}")
print(Fore.RED + "Cierre de ciclo n°1")
print(Fore.CYAN + "Inicio ciclo N°2")
while num <= 200:
    print(num)
    num = num + 2
    print(Fore.CYAN + "num")
print(Fore.CYAN + "Cierre de ciclo N°2")
print(Fore.MAGENTA + "Inicio ciclo N°3")
while num <= 300:
    print(num)
    num = num+2
    if num == 250:
        print(Fore.MAGENTA + "Se detiene la ejecucion")
        break
print(num)
print(Fore.MAGENTA + "Cierre de Ciclo N°3")

#Ciclo for
print(Fore.MAGENTA + "Inicio ciclo N°4")
lista = list(range(1, 11, 1))
print(Fore.RED + "cierre de ciclo n°4")
for i in lista:
    print(i)

print(Fore.MAGENTA + "Inicio ciclo N°5(FOR)")
lista = [1,2,3,4,5,6,7,8,9,10]
print(Fore.RED + "cierre de ciclo n°5(FOR)")
for i in range(1,10):
    print(i)
