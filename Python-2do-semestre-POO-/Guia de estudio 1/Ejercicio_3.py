""" Imagina que estás diseñando un sistema para gestionar cuentas bancarias. Para ello, crea
una clase llamada CuentaBancaria que modele el comportamiento básico de una cuenta de
banco. El sistema debe permitir realizar operaciones como depósitos, retiros y consultar el
saldo actual. Además, se debe utilizar el concepto de encapsulamiento para proteger la
información sensible de la cuenta. Asegúrate de encapsular adecuadamente los atributos
que consideres sensibles. Define métodos para interactuar con estos atributos de manera
controlada.
Consideraciones de Encapsulamiento
● ¿Qué atributos deberían ser privados y por qué?
● ¿Qué métodos utilizarías para acceder o modificar estos atributos de manera
controlada? Por ejemplo, permitiendo consultar el saldo pero no modificarlo
directamente"""

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0):
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial

    def deposito(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se ha hecho el deposito correctamente por ${cantidad:.2f}")
        else:
            print(f"Ingrese un saldo no negativo")


    def retiro(self, cantidad):
        if cantidad > self.__saldo:
            print(f"Debe ingresar un monto que no supere el valor en la cuenta")
            
        elif cantidad <= 0:
            print(f"El monto debe ser positivo")
        
        else:
            self.__saldo -= cantidad
            print(f"Retiro realiado con exito, ${cantidad:.2f}")

    def consultar_numero_cuenta(self):
        return f"Su numero de cuenta es {self.__numero_cuenta}"
    
    def consultar_saldo(self):
        return f"Su saldo es de {self.__saldo:.2f}"

cuenta = CuentaBancaria("007", 100000)

print(cuenta.consultar_saldo())
cuenta.deposito(500)
print(cuenta.consultar_saldo())
cuenta.retiro(300)
print(cuenta.consultar_saldo())