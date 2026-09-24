class Estudiante:
    def __init__(self, nombre, promedio):
        self.__nombre = nombre
        self.__promedio = promedio
        self.estado = self.evaluar_estado()

    def evaluar_estado(self):
        return self.__promedio >= 4.0

    def actualizar_notas(self, nuevo_promedio):
        self.__promedio = nuevo_promedio
        self.estado = self.evaluar_estado()

    def __str__(self):
        return f"Nombre: {self.__nombre}, Promedio: {self.__promedio}, Aprobado: {'Sí' if self.estado else 'No'}"
    
# Creación de estudiantes
estudiante_1 = Estudiante("Harry Potter", 5.4)
estudiante_2 = Estudiante("Ron Weasly", 3.2)
estudiante_3 = Estudiante("Hermanione", 7.0)

# Imprimir el estado de cada estudiante
print(estudiante_1)
print(estudiante_2)
print(estudiante_3)

# Simular una actualización de notas
print("\nActualizando las notas de Ron weasly... ")
estudiante_2.actualizar_notas(4.1)

# Imprimir el estado actualizado de cada estudiante
print("\nEstado actualizado: ")
print(estudiante_1)
print(estudiante_2)
print(estudiante_3)