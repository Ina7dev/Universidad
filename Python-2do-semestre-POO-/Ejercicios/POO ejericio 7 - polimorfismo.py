#Clase base: Vehículo
class Vehiculo:
    def __init__(self, nombre, velocidad_base):
        self.nombre = nombre
        self.velocidad_base = velocidad_base

    def acelerar(self):
        return f"{self.nombre} acelera a {self.velocidad_base} km/h."

    def frenar(self):
        return f"{self.nombre} está frenando."

    def __str__(self):
        return f"Vehículo: {self.nombre}, Velocidad Base: {self.velocidad_base} km/h"

#Clase específica: Terrestre
class Terrestre:
    def conducir_en_carretera(self):
        return "Conduciendo en carretera con tracción óptima."

#Clase específica: Acuático
class Acuatico:
    def navegar(self):
        return "Navegando sobre el agua con estabilidad."

#Clase específica: Aéreo
class Aereo:
    def volar(self):
        return "Volando a gran altura con precisión."

#Vehículo híbrido: Anfibio (Terrestre y Acuático)
class VehiculoAnfibio(Vehiculo, Terrestre, Acuatico):
    def __init__(self, nombre, velocidad_base, velocidad_agua):
        super().__init__(nombre, velocidad_base)
        self.velocidad_agua = velocidad_agua

    def acelerar(self):
        return f"{self.nombre} acelera en tierra a {self.velocidad_base} km/h y en agua a {self.velocidad_agua} km/h."

#Vehículo híbrido: Aéreo y Terrestre
class VehiculoAereoTerrestre(Vehiculo, Terrestre, Aereo):
    def __init__(self, nombre, velocidad_base, altitud_max):
        super().__init__(nombre, velocidad_base)
        self.altitud_max = altitud_max

    def acelerar(self):
        return f"{self.nombre} acelera en tierra a {self.velocidad_base} km/h y puede volar hasta {self.altitud_max} metros."

#Función para manejar vehículos utilizando polimorfismo
def manejar_vehiculo(vehiculo):
    print(vehiculo.acelerar())
    print(vehiculo.frenar())
    if isinstance(vehiculo, Terrestre):
        print(vehiculo.conducir_en_carretera())
    if isinstance(vehiculo, Acuatico):
        print(vehiculo.navegar())
    if isinstance(vehiculo, Aereo):
        print(vehiculo.volar())

# Instanciando vehículos de diferentes tipos
coche = Vehiculo("Auto Rápido", 200)
anfibio = VehiculoAnfibio("Anfibio X", 100, 50)
aereo_terrestre = VehiculoAereoTerrestre("JetCar", 300, 10000)

#ista de vehículos
vehiculos = [coche, anfibio, aereo_terrestre]

#Manejando vehículos de manera uniforme
for vehiculo in vehiculos:
    manejar_vehiculo(vehiculo)
    print("-" * 40)
