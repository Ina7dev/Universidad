#Cada libro tiene un título, autor, año de publicación, y cantidad disponible.
class Libro:
    def __init__(self, titulo, autor, año_publicacion, cantidad_disponible):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.cantidad_disponible = cantidad_disponible

##Para que cuando imprimamos el libro, se vea bonitojiji.
    def __str__(self):
        return f"""Libro: {self.titulo}
        - Autor: {self.autor}  
        - Año: {self.año_publicacion}
        - cantidad disponible: {self.cantidad_disponible}.\n"""

#Clase biblioteca debe manejar múltiples instancias de la clase Libro utilizando un diccionario.
class Biblioteca:
    def __init__(self):
        self.libros = {}

#Metodo para agregar libros.
    def agregar_libro(self, libro):
        if libro.titulo not in self.libros:
            self.libros[libro.titulo] = libro
            print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.\n")
        else:
            print("El libro ya existe en la biblioteca.\n")

#Metodo para buscar libros.
    def buscar_libro(self, titulo):
        if titulo in self.libros:
            print(self.libros[titulo])
        else:
            print("El libro no ha sido encontrado\n.")

#Metodo para actualizar libros.
    def actualizar_cantidad(self, titulo, nueva_cantidad_disponible):
        if titulo in self.libros:
            self.libros[titulo].cantidad_disponible = nueva_cantidad_disponible
            print(f"La cantidad disponible ha sido actualizada para el libro '{titulo}'': Nueva cantidad {nueva_cantidad_disponible}\n")
        else:
            print("El libro no ha sido encontrado.\n")


biblioteca = Biblioteca()

#Se crean dos libros para agregarlos
libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, 22)
biblioteca.agregar_libro(libro1)
libro2 = Libro("El pozo de la ascención", "Brandon Sanderson", 2016, 14)
biblioteca.agregar_libro(libro2)

#Buscando libros
biblioteca.buscar_libro("Harry Potter y la piedra filosofal") #Buscando un libro que SI esta en la biblioteca.
biblioteca.buscar_libro("Hush Hush")#Buscando un libro que NO esta en la biblioteca.

#Actualizando la cantidad de un libro existente
biblioteca.actualizar_cantidad("El pozo de la ascención", 10)