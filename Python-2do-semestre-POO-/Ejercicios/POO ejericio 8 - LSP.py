#Clase base simple
class MetodoDePago:
    def procesar_pago(self, monto):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")

#Subclase para tarjeta de crédito
class TarjetaDeCredito(MetodoDePago):
    def procesar_pago(self, monto):
        if self.validar_tarjeta():
            print(f"Procesando pago de ${monto} con tarjeta de crédito.")
        else:
            print("Validación de tarjeta fallida. No se puede procesar el pago.")

    def validar_tarjeta(self):
        #Lógica ficticia de validación
        print("Validando tarjeta de crédito...")
        return True  #Supongamos que siempre es válida.

#Subclase para transferencia bancaria
class TransferenciaBancaria(MetodoDePago):
    def procesar_pago(self, monto):
        codigo_confirmacion = self.obtener_codigo_confirmacion()
        if codigo_confirmacion:
            print(f"Procesando pago de ${monto} con transferencia bancaria. Código de confirmación: {codigo_confirmacion}.")
        else:
            print("Fallo al obtener el código de confirmación. No se puede procesar el pago.")

    def obtener_codigo_confirmacion(self):
        #Lógica ficticia para generar código de confirmación
        print("Generando código de confirmación...")
        return "ABC123"

#Subclase para pago en efectivo
class PagoEnEfectivo(MetodoDePago):
    def procesar_pago(self, monto):
        print(f"Pago de ${monto} en efectivo registrado exitosamente.")

#Uso de las clases
def procesar_pagos():
    pagos = [
        TarjetaDeCredito(),
        TransferenciaBancaria(),
        PagoEnEfectivo(),
    ]

    for metodo in pagos:
        metodo.procesar_pago(100)

procesar_pagos()