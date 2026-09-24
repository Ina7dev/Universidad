import datetime
#Cada reserva tendrá atributos como nombre del cliente, la fecha de entrada, la fecha de salida, y el número de habitación.
class ReservaHostal:
    def __init__(self, nombre_cliente, fecha_entrada, fecha_salida, numero_habitacion):
        self.nombre_cliente = nombre_cliente
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.numero_habitacion = numero_habitacion

#Un método para calcular la duración de la estadía del cliente.
    def calculo_duracion_estadia(self):
        duracion = self.fecha_salida - self.fecha_entrada
        return duracion.days

#Un método mágico para mostrar la información de la reserva.
    def __str__(self):
        return f"Reserva para {self.nombre_cliente}. Habitación {self.numero_habitacion}. Entrada: {self.fecha_entrada}, Salida: {self.fecha_salida}."

#Un método para cambiar la fecha de salida.
    def cambiar_fecha_salida(self, nueva_fecha_salida):
        self.fecha_salida = nueva_fecha_salida

#Se debe eliminar un objeto ReservaHostall, además de imprimir un mensaje indicando que la reserva ha sido cancelada.

    def cancelar_reserva(self):
        print(f"La reserva para el/la huesped {self.nombre_cliente} ha sido cancelada. Su numero de habitación era {self.numero_habitacion}.\n")

#Datos 1ra reserva
fecha_entrada = datetime.date(2024, 9, 18)
fecha_salida = datetime.date(2024, 9, 22)
reserva = ReservaHostal("Ina Calderón", fecha_entrada, fecha_salida, 416)

print(reserva)
print(f"Duración de la estadía: {reserva.calculo_duracion_estadia()} noches.\n")

#Datos 2da reserva
fecha_entrada2 = datetime.date(2024, 10, 24)
fecha_salida2 = datetime.date(2024, 10, 25)
reserva2 = ReservaHostal("Nacho Millapani", fecha_entrada2, fecha_salida2, 203)

print(reserva2)
print(f"Duración de la estadía: {reserva2.calculo_duracion_estadia()} noches.\n")

#Ingresando nuevos datos con fecha salida actualizada e impriminedolos.
nueva_fecha_salida = datetime.date(2024, 9, 20)
reserva.cambiar_fecha_salida(nueva_fecha_salida)
print(f"La reserva ha sido actualizada para nueva fecha de salida: {reserva}\n")

#Imprimiendo mensaje de cancelacion.
reserva2.cancelar_reserva()
