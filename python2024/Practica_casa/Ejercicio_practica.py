#EJERCICIO 1 - HACER UN HOLA MUNDO.
print("Hola mundo")

#EJERCICIO2 - HACER UNA VARIABLE Y QUE SE MUESTRE DESPUES.
v = "Hola mundo"
print(f"Nuestra variable es {v}")

#EJERCICIO 3 - USUARIO DEBE INGRESAR NOMBRE Y LUESGO DARLE LA BIENVENIDA.
n = input("Ingrese su nombre: ")
print(f"¡Bienvenido{n}!")

#EJERCICIO 4 - HACER UNA OPERACION ARITMETICA.
r = ((2+3) / (2*5)) ** 2
print(f"El resultado de la fraccion 2+3/2*5 elevado a 2 es {r}")

#EJERCICIO 5 - PREGUNTAR POR EL N° DE HRS DE TRABAJO Y EL PAGO POR HORA. MOSTRAR PAGA TOTAL.
hrs = int(input("Ingrese las horas trabajadas por día: ")) 
pago = int(input("Ingrese el pago por hora: "))
pt = hrs * pago

print(f"El pago total es de {pt}")

#EJERCICIO 6 - LEER UN ENTERO POSITIVO INGRESADO POR CONSOLA, MOSTRAR LA SUMA DE TODOS LOS N° DESDE EL 1 HASTA EL N° INGRESADO.
#FORMULA ESPECIFICA, N*N+1/2
n = int(input("Ingrese un numero entero positivo: "))
suma = n *(n+1)/2
print(f"La suma de los primeros numeros enteros desde 1 hasta {n} es {suma}")

#EJERCICIO 7 - INGRESADO POR CONSOLA, KG Y ALTURA. MENCIONAR IMC CON 2 DECIMALES.
kg = float(input("Ingrese cuanto pesa: "))
al = float(input("Ingrese cuanto mide: "))

imc = kg / (al)**2
print(F"Tu IMC es de {round(imc, 2)}")

#EJERCICIO 8 - LEER CANTIDAD DE 2 JUGUETES VENDIDOS Y CALCULAR EL PESO TOTAL DEL PAQUETE QUE SERA ENVIADO.
#payaso pesa 112 g y cada muñeca 75 g
p_p = 112
p_m = 75
p = int(input("Ingrese la cantidad de payasos a enviar: "))
m = int(input("Ingrese la cantidad de muñecas a enviar: "))

p_t = p_p * p + p_m * m
print(f"El peso total es de {p_t}")

#EJERCICIO 9 - POR CONSOLA INGRESAR DINERO DEPOSITADO, PROGRAMA DEBE CALCULAR Y MOSTRAR CANTIDAD DE AHORRO EN 1RO, 2DO Y 3R AÑO.
#INTERES 4%, REDONDEAR A 2 DECIMALES
inv = float(input("Introduce la inversion inicial: "))
int = 0.04
b1 = inv * (1+int)
print(f"Lo ahorrado el primer año es de {round(b1,2)}")
b2 = b1 * (1+int)
print(f"Lo ahorrado el segundo año es de {round(b2,2)}")
b3 = b2 * (1+int)
print(f"Lo ahorrado el tercer año es de {round(b3,2)}")

#EJERCICIO 10 - mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
vendido = float(input("Ingrese la cantidad de barras de pan que no son frescas: "))
bp = 3.49
bp_a = 0.6
cf = vendido * bp  * bp_a

print(f"El valor de las barras de pan es de {bp}")
print(f"El descuento a las barrad de pan no frescas es de {bp_a * 100}")
print(f"El costo final a pagar es de {cf}")