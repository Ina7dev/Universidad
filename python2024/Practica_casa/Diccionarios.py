#1
monedas = {
    "Dollar" : "$",
    "Yen" : "¥",
    "Euro" : "€"
}

ingresar = input("Introduce la moneda o divisa: ")

print(monedas.get(ingresar.title(), "La divisa no está."))

#2
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu N° de teléfono: ")

solicitud = {
    "nombre" : nombre,
    "edad" : edad,
    "direccion" : direccion,
    "telefono" : telefono
}
print(f"Tu nombre es {solicitud['nombre']} tienes {solicitud['edad']}, tu direccion es {solicitud['direccion']} y tu N° es {solicitud['telefono']}")#Print con dict
print(f"Tu nombre es {nombre} tienes {edad}, tu direccion es {direccion} y tu numero de telefono es {telefono}")#Print normal

#3
frutas = {
    "plátano" : 1.35,
    "manzana" : 0.80,
    "naranja" : 0.70,
    "pera" : 0.85
}

fruta_a_pedir = input("Ingrese que tipo de fruta desea: ").lower()
kg = float(input("¿Cuántos kilos quieres?: "))

if fruta_a_pedir in frutas:
    print(f"{kg} de {fruta_a_pedir} cuestan {frutas[fruta_a_pedir]*kg} CLP")
else: 
    print("Esa fruta no esta")

#4
meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])

#5
persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si".lower()

#6
