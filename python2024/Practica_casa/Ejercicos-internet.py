#pedir al usuario su imc
kg = float(input("Ingrese cuanto pesa: "))
al = float(input("Ingrese su altura: "))

pt = kg * al**2
print(f"Tu IMC es de {pt:.2f}")


#2hacer una lista que tenga 3 objetos escritos por el usuario, cada ob debe tener precio y sumar todos los precios.
ob1=(input("Ingresa el primer objeto: "))
ob2=(input("Ingresa el segundo objeto: "))
ob3=(input("Ingresa el tercer objeto: "))

p1 = int(input("Ingresa el precio del primer objeto: "))
p2 = int(input("Ingresa el segundo del primer objeto: "))
p3 = int(input("Ingresa el tercero del primer objeto: "))

vt = p1 + p2 + p3


print(f"El primer objeto es {ob1} y su valor es {int(p1)}")
print(f"El segundo objeto es {ob2} y su valor es {int(p2)}")
print(f"El tercer objeto es {ob3} y su valor es {int(p3)}")

print(f"El valor de todos los objetos es {vt}")

#hacer una ficha medica la cual ocupe una lista que se vaya actualizando a medida que se entrega datos, imprimir con espacios vacios.
datos = []
n = input("Ingrese su nombre: ")
datos.append(n)
a = input("Ingrese su apellido: ")
datos.append(a)
datos = " " .join(datos)
print(datos)

#sacar el minimo comun multiplo de 10
v = 10 % 2

#adivina el numero secreto, sera 12.

v = 12
print("Adivina cual es el numero secreto")
n = int(input("Ingresa el numero: "))

while True:
    if n > v or n < v:
        print("Numero erroneo")
        n = int(input("Ingresa el numero: "))
    elif n == 12:
        print("Nunmero correcto")
        break

#crear una tienda con dif productos, valores, a todo el inventario sacar promedio y restarle el valor mas bajo.

p = input("Ingresa tu primer produto: ")
p2 = input("Ingresa tu segundo produto: ")
p3 = input("Ingresa tu tercer produto: ")
p4 = input("Ingresa tu cuarto produto: ")
p5 = input("Ingresa tu quinto produto: ")

v1 = float(input("Ingresa el valor de tu primer produto: "))
v2 = float(input("Ingresa el valor de tu segundo produto: "))
v3 = float(input("Ingresa el valor de tu tercer produto: "))
v4 = float(input("Ingresa el valor de tu cuarto produto: "))
v5 = float(input("Ingresa el valor de tu quinto produto: "))

vt = (v1+v2+v3+v4+v5)/5
print(f"El promedio del inventario es de {float(vt)}")

v_m = min(v1, v2, v3, v4, v5)
vsm = vt - v_m
print(f"El valor de los productos restados con el minimo es {vsm}")

print(type(v_m))

#ingresar 5 numeros por consola y colocarlos en una lista de mayor a menor
n = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))
n4 = int(input("Ingrese el cuarto numero: "))
n5 = int(input("Ingrese el quinto numero: "))

l = [n,n2,n3,n4,n5]
lo = []
a = min(l)
lo.append(a)
l.remove(a)
b = min(l)
lo.append(b)
l.remove(b)
c = min(l)
lo.append(c)
l.remove(c)
d = min(l)
lo.append(d)
l.remove(d)
e = min(l)
lo.append(e)
print(lo)