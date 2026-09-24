class CuentaBancaria:
    def __init__(self, titular, saldo):
        # Atributo público
        self.titular = titular  # Un atributo público es accesible desde fuera de la clase

        # Atributo privado
        self.__saldo = saldo    # Un atributo es privado, solo accesible dentro de la clase

    # Método público para mostrar información de la cuenta
    def mostrar_info(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.__saldo} CLP")

    # Método público para depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se han depositado ${monto} CLP en la cuenta")
        else:
            print("No se puede depositar una cantidad negativa")

    # Método privado para calcular intereses (no accesible desde fuera de la clase)
    def __calcular_intereses(self):
        return self.__saldo * 0.05

    # Método público para agregar intereses al saldo
    def agregar_intereses(self):
        intereses = self.__calcular_intereses()  # Se puede llamar al método privado desde dentro
        self.__saldo += intereses
        print(f"Se han agregado ${intereses} CLP en intereses")


# Crear una cuenta bancaria
cuenta = CuentaBancaria("Victor Saldivia", 100000)

# Acceder al atributo público
print(cuenta.titular) 

# No se puede acceder directamente al atributo privado (esto arrojará un error)
# print(cuenta.__saldo) 

# Mostrar información de la cuenta
cuenta.mostrar_info()

# Depositar dinero en la cuenta
cuenta.depositar(50000)
cuenta.mostrar_info()

# Agregar intereses
cuenta.agregar_intereses()
cuenta.mostrar_info()

# No se puede llamar al método privado directamente (esto arrojará un error)
# cuenta.__calcular_intereses()  