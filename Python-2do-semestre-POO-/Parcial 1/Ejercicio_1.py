#1. ¿Cómo representarías a los gatos dentro del sistema?
#2. Métodos que necesita la clase Gato:
#3. Método Mágico:
class Gato:
    def __init__(self, nombre, edad, raza, nivel_de_energía=100, nivel_de_hambre=0):
        self.nombre = nombre
        self.edad = edad
        self.__nivel_de_energia = nivel_de_energía
        self.__nivel_de_hambre = nivel_de_hambre
        self.raza = raza


    def jugar(self, tiempo, energia_gastada, hambre_aumentada):

        energia_gastada = tiempo * 10 
        hambre_aumentada = tiempo * 5

        self.__nivel_de_energia = max(self.__nivel_de_energia - energia_gastada, 0)
        self.__nivel_de_hambre = min(self.__nivel_de_hambre + hambre_aumentada, 100)

        if self.__nivel_de_energia == 0:
            print(f"El gato {self.nombre} está muy cansado y necesita descansar")
        else:
            print(f"El gato {self.nombre} todavía puede jugar")

        if self.__nivel_de_hambre >= 100:
            print(f"El gato {self.nombre} tiene mucha hambre y necesita comer")


    def alimentar(self, cantidad_comida, hambre_reducida):
        hambre_reducida = cantidad_comida * 20
        
        self.__nivel_de_hambre = max(self.__nivel_de_hambre - hambre_reducida, 0)
    
        if self.__nivel_de_hambre == 0:
            self.__nivel_de_energia = min(self.__nivel_de_energia + 50, 100)
            print(f"El gato {self.nombre} ha comido y ya se encuentra con energía")

    def __str__(self):
        return f"""ESTADO DEL GATO:
                    Nombre: {self.nombre}
                    Edad: {self.edad}
                    Energía: {self.__nivel_de_energia}
                    Hambre: {self.__nivel_de_hambre}
                    Raza: {self.raza}"""


#1. ¿Cómo representarías las áreas dentro del café?
#2. Métodos que necesita la clase Area:
class Area:
    def __init__(self, area_nombre, capacidad_max, nombre):
        self.area_nombre = area_nombre
        self.capacidad_max = capacidad_max
        self.nombre = nombre
        self.gatos_presentes = []

    def agregar_gato(self, gato):
        if len(self.gatos_presentes) < self.capacidad_max:
            self.gatos_presentes.append(gato)
            print(f"El {gato.nombre} ha sido agregado al área {self.area_nombre}")
        else:
            print(f"No se pudo agregar al gato {gato.nombre}, el área {self.area_nombre} está llena")

def listar_gatos(self):
     if self.gatos_presentes:
        print(f"Gatos en el área {self.nombre}:")
        for gato in self.gatos_presentes:
            print(f"{gato.nombre}")
        else:
            print(f"No hay gatos en el área {self.nombre}.\n")


#1. ¿Cómo representarías el inventario del café?
#2. Métodos que necesita la clase Inventario:
class Inventario:
    def __init__(self, productos, cantidad):
        self.__productos = productos
        self.cantidad= cantidad

    def agregar_producto(self, nombre_producto, cantidad):
        if nombre_producto in self.__productos:
            self.__productos[nombre_producto] += cantidad
        else:
            self.__productos[nombre_producto] = cantidad
        print(f"Se han agregado {cantidad} unidades de {nombre_producto}.\n")

    def utilizar_producto(self, nombre_producto, cantidad):
        if nombre_producto in self.__productos:
            if self.__productos[nombre_producto] >= cantidad:
                self.__productos[nombre_producto] -= cantidad
                print(f"Se han usado {cantidad} unidades de {nombre_producto}.")
            else:
                print(f"No hay suficientes unidades de {nombre_producto}. Solo quedan {self.__productos[nombre_producto]} unidades.")
        else:
            print(f"El producto {nombre_producto} no está en el inventario.")


#1. ¿Cómo podrías usar un método mágico para imprimir el estado de un gato?
#2. Métodos de interacción entre las clases:
