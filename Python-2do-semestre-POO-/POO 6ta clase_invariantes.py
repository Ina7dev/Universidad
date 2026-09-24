class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
        # Aserción para asegurar el invariante en la inicialización
        assert self.__saldo >= 0, "Error: El saldo no puede ser negativo"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("Error: El saldo no puede ser negativo")

# Se prueba el Invariante de Clase
# Crear una cuenta con saldo positivo (funciona correctamente)
cuenta_nueva = CuentaBancaria("Alejandra Saez", 10000000)
print(f"Titular: {cuenta_nueva.titular}, Saldo: {cuenta_nueva.saldo}")

# Se intenta establecer un saldo negativo en el setter (dispara una advertencia)
cuenta_nueva.saldo = -5000000  # Error: El saldo no puede ser negativo
print(f"Titular: {cuenta_nueva.titular}, Saldo: {cuenta_nueva.saldo}")

# Intentar crear una cuenta con saldo negativo (Dispara el invariante en el constructor)
cuenta2 = CuentaBancaria("Ana López", -20000000)  # AssertionError: Error: El saldo no puede ser negativo