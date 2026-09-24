"""Ejercicio:
Crear un programa que gestione una lista de compras.

Requisitos:
El programa debe permitir agregar productos a una lista de compras, donde cada producto tiene un nombre y un precio.
El programa debe permitir eliminar productos de la lista usando el nombre del producto.
El programa debe calcular el total de la lista de compras.
El programa debe mostrar todos los productos en la lista junto con su precio.

Pistas:
Utiliza una lista de diccionarios, donde cada diccionario tiene claves nombre y precio para representar cada producto.
Usa funciones para organizar el código.
Asegúrate de manejar errores si se intenta eliminar un producto que no existe."""

productos = []

def agregar_producto(nombre, precio):
    # Crear un diccionario para el producto
    producto = {"nombre": nombre, "precio": precio}
    # Agregar el diccionario a la lista de productos
    productos.append(producto)

def eliminar_producto(nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            productos.remove(producto)  # Eliminar el producto
            return  # Salir de la función después de eliminar
    print("Producto no encontrado.")  # Mensaje si no se encuentra el producto

def calcular_total():
    total = 0
    for producto in productos:
        total += producto["precio"]  # Sumar el precio de cada producto
    return total

def menu():
    while True:
        print("\n1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Calcular total")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            agregar_producto(nombre, precio)
        elif opcion == "2":
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(nombre)
        elif opcion == "3":
            total = calcular_total()
            print(f"Total de la lista de compras: ${total:.2f}")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

menu()
