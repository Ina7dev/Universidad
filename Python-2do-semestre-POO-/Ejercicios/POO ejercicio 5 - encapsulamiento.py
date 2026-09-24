class Concesionaria:
    def __init__(self):
        self.vehiculos = []  # Lista pública de vehículos

    def agregar_vehiculo(self, marca, modelo, año):
        # Crear un diccionario para representar el vehículo
        vehiculo = {
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "disponible": True
        }
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        print("Vehículos disponibles: ")
        for vehiculo in self.vehiculos:
            estado = "Disponible" if vehiculo["disponible"] else "No disponible"
            print(f"Marca: {vehiculo['marca']}, Modelo: {vehiculo['modelo']}, Año: {vehiculo['año']}, Estado: {estado}")

    def vender_vehiculo(self, marca, modelo, año):
        for vehiculo in self.vehiculos:
            if (vehiculo["marca"] == marca and 
                vehiculo["modelo"] == modelo and 
                vehiculo["año"] == año):
                if vehiculo["disponible"]:
                    vehiculo["disponible"] = False
                    print(f"Vehículo vendido: {vehiculo['marca']} {vehiculo['modelo']} ({vehiculo['año']})")
                else:
                    print(f"El vehículo {vehiculo['marca']} {vehiculo['modelo']} ({vehiculo['año']}) ya no está disponible.")
                return
        print("Vehículo no encontrado.")

# Interacción
# Paso 1: Crear una instancia de la clase Concesionaria y agregar varios vehículos
concesionaria = Concesionaria()
concesionaria.agregar_vehiculo("Toyota", "Corolla", 2020)
concesionaria.agregar_vehiculo("Honda", "Civic", 2019)
concesionaria.agregar_vehiculo("Ford", "Focus", 2021)

# Paso 2: Mostrar la lista de vehículos disponibles
concesionaria.mostrar_vehiculos()

# Paso 3: Realizar la venta de un vehículo y cambiar su estado de disponibilidad
concesionaria.vender_vehiculo("Toyota", "Corolla", 2020)

# Paso 4: Volver a mostrar la lista de vehículos, verificando que el vehículo vendido ya no está disponible
concesionaria.mostrar_vehiculos()
