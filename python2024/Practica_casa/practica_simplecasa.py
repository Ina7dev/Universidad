#UNA SUMA NORMAL.
sum = 5 + 6
print(f"El resultado de 5 + 6 es {sum}")

#RESTOS DE UNA DIVISION.
rest = 10%3
print(f"El resto de la division de 10/3 es de {rest}")

#NUMERO CON EXPONENTE.
elev = 5**3 #(2 ASTERISCOS SIGNIFICA EXPONENTE)
print(f"5 elevado a 3 es {elev}")

#DIVISION SOLO CON NUMERO ENTERO Y DECIMAL.
div = 9//2
DIV = 9/2
NUM=5
print(f"la division de 9/4 con solo un numero entero es {div} y con su decimal es {DIV}")

#VARIABLE DE CARACTER
name = "valentina"
print(f"Hola soy {name}")

#VER QUE TIPO DE CARACTER ES.
print(type(div))
print(type(DIV))
print(type(name))

#MENSAJE CON SALTO DE LINEA.
men="""hola soy valentina
vivo en castro
y tengo 21 años"""
print(men)

#CONDICIONAL IF
num1=5
num2=7
if num1>num2:
        print("el numero 1 es mayor")
else:
        print("El numero 2 es mayor")

#FUNCION PARA REPETIR MENSAJE.
def mensaje():
        print("Estamos viendo como funciona")
mensaje()
print("vere si vuelve a repetirse aqui abajo")
mensaje()

def suma():
        num1=5
        num2=7
        print(num1+num2)
suma()

print("Entonces la suma entre 5 y 7 es de:")
suma()

#FUNCION PARA REPETIR FORMATO CON DIFERENTES VARIABLES.
def sum(nume1, nume2):
        print(nume1+nume2)
sum(5,7)

print("veamos si vuelve a repetirse pero con distintos numeros")

sum(3,6)
sum(38, 358)
