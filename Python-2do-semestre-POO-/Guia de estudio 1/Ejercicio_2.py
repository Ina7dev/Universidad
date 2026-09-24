"""Desarrollar un sistema de gestión de contactos, en el cual se debe crear dos clases,
Contacto y Agenda, para gestionar los contactos de una agenda. El objetivo es permitir al
usuario realizar operaciones básicas como añadir, buscar, editar y listar contactos. Además,
el programa debe finalizar correctamente cuando el usuario lo solicite.
"""
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    def modificar_datos(self, nombre=None, telefono=None, email=None):
        if nombre:
            self.__nombre = nombre
        if telefono:
            self.__telefono = telefono
        if email:
            self.__email = email

    def __str__(self):
        return f'Nombre: {self.__nombre}, Telefono: {self.__telefono}, Email: {self.__email}'
    
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto._Contacto__nombre.lower() == nombre.lower():
                return contacto
        return None

    def editar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            nuevo_nombre = input("Nuevo nombre (dejar vacío para no modificar): ")
            nuevo_telefono = input("Nuevo teléfono (dejar vacío para no modificar): ")
            nuevo_email = input("Nuevo email (dejar vacío para no modificar): ")
            contacto.modificar(nuevo_nombre or None, nuevo_telefono or None, nuevo_email or None)
            print("Contacto actualizado.")
        else:
            print("Contacto no encontrado.")


def main():
    agenda = Agenda()
    while True:
        print("\n--- Menú ---")
        print("1. Añadir contactos")
        print("2. Listar contactos")
        print("3. Buscar contactos")
        print("4. Editar contactos")
        print("5. Cerrar agenda")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            nuevo_contacto = Contacto(nombre, telefono, email)
            agenda.agregar_contacto(nuevo_contacto)
            print("Contacto añadido.")

        elif opcion == '2':
            agenda.listar_contactos()

        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print(contacto)
            else:
                print("Contacto no encontrado.")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a editar: ")
            agenda.editar_contacto(nombre)

        elif opcion == '5':
            print("Cerrando agenda. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()