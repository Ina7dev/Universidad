class Planta:
    def __init__(self, tipo, estado_crecimiento, agua_necesaria, fertilizante_necesario):
        self.__tipo = tipo
        self.__estado_crecimiento = estado_crecimiento
        self.__agua_necesaria = agua_necesaria
        self.__fertilizante_necesario = fertilizante_necesario
        self.__ultimo_riego = None

    # Método para obtener el estado de crecimiento
    def consultar_estado(self):
        return f"{self.__tipo}: Estado - {self.__estado_crecimiento}"

    # Método para obtener la cantidad de agua necesaria
    def consultar_agua_necesaria(self):
        return self.__agua_necesaria

    # Método para regar la planta
    def regar(self, cantidad_agua):
        if cantidad_agua >= self.__agua_necesaria:
            self.__ultimo_riego = "Hoy"  # Asumimos que se guarda la fecha
            self.__agua_necesaria = 0  # La planta ya está regada
            print(f"{self.__tipo} ha sido regada.")
        else:
            print(f"{self.__tipo} necesita más agua.")

    # Método mágico para representar el estado de la planta
    def __str__(self):
        return f"Planta: {self.__tipo}, Estado: {self.__estado_crecimiento}, Agua necesaria: {self.__agua_necesaria} litros"

class AreaJardin:
    def __init__(self, nombre_area):
        self.__nombre_area = nombre_area
        self.__plantas = []

    # Método para agregar una planta
    def agregar_planta(self, planta):
        self.__plantas.append(planta)
        print(f"Planta {planta.consultar_estado()} añadida a {self.__nombre_area}")

    # Método para eliminar una planta
    def quitar_planta(self, planta):
        if planta in self.__plantas:
            self.__plantas.remove(planta)
            print(f"Planta {planta.consultar_estado()} eliminada de {self.__nombre_area}")
        else:
            print(f"La planta no está en el área {self.__nombre_area}")

    # Método para listar las plantas en el área
    def listar_plantas(self):
        for planta in self.__plantas:
            print(planta)

class Planta:
    # Otros métodos...

    def calcular_agua_necesaria(self):
        if self.__estado_crecimiento == "semilla":
            self.__agua_necesaria = 0.5
        elif self.__estado_crecimiento == "brote":
            self.__agua_necesaria = 1.0
        else:
            self.__agua_necesaria = 2.0

class Fertilizante:
    def __init__(self, tipo, cantidad_disponible):
        self.__tipo = tipo
        self.__cantidad_disponible = cantidad_disponible

    def usar_fertilizante(self, cantidad):
        if cantidad <= self.__cantidad_disponible:
            self.__cantidad_disponible -= cantidad
            print(f"Se usaron {cantidad} kg de fertilizante {self.__tipo}.")
        else:
            print(f"No hay suficiente fertilizante {self.__tipo}.")
    
    def consultar_disponible(self):
        return self.__cantidad_disponible

class Planta:
    # Otros métodos...

    def actualizar_estado_crecimiento(self):
        if self.__estado_crecimiento == "semilla":
            self.__estado_crecimiento = "brote"
        elif self.__estado_crecimiento == "brote":
            self.__estado_crecimiento = "planta adulta"
        print(f"Estado de {self.__tipo} actualizado a {self.__estado_crecimiento}.")

# Crear plantas
planta1 = Planta("Rosa", "semilla", 0.5, 0.2)
planta2 = Planta("Tulipán", "brote", 1.0, 0.3)

# Crear un área
area1 = AreaJardin("Zona A")
area1.agregar_planta(planta1)
area1.agregar_planta(planta2)

# Usar fertilizante
fertilizante = Fertilizante("Orgánico", 10)
fertilizante.usar_fertilizante(1)

# Regar plantas
planta1.regar(0.5)
planta2.regar(1.0)
