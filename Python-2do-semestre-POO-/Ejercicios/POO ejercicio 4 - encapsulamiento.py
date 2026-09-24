class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True
        
    def marcar_vendido(self):
        self.__disponible = False
        
    def __str__(self):
         estado = "Disponible" if self.__disponible else "No disponible"
         return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}, Estado: {estado}"


vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
print(vehiculo1)
vehiculo1.marcar_vendido()
print(vehiculo1) 