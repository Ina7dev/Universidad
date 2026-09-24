class Doctor:
    def __init__(self, nombre, especialidad, salario):
        # Atributos privados
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__sueldo = salario

    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre

    # Setter para el nombre
    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("Error: El nombre no puede estar vacío")

    # Getter para la especialidad
    def get_especialidad(self):
        return self.__especialidad

    # Setter para la especialidad
    def set_especialidad(self, nueva_especialidad):
        if len(nueva_especialidad) > 0:
            self.__especialidad = nueva_especialidad
        else:
            print("Error: La especialidad no puede estar vacía")

    # Getter para el sueldo
    def get_sueldo(self):
        return self.__sueldo

    # Setter para el salario (validación para que no sea negativo)
    def set_sueldo(self, nuevo_salario):
        if nuevo_salario >= 0:
            self.__sueldo = nuevo_salario
        else:
            print("Error: El sueldo no puede ser negativo")

    # Método para mostrar información del doctor
    def mostrar_info(self):
        print(f"Doctor: {self.__nombre}, Especialidad: {self.__especialidad}, Sueldo: {self.__sueldo}")

# Instancia
doctor1 = Doctor("Dr. Yoel Cea", "Cardiología", 5000000)
print(doctor1.get_nombre())  
doctor1.set_nombre("Dr. Ana López")
print(doctor1.get_nombre()) 

# Mostrar información inicial
doctor1.mostrar_info()

# Cambiar nombre usando setters
doctor1.set_nombre("Dr. Ana López")
doctor1.mostrar_info()

# Cambiar especialidad usando setters
doctor1.set_especialidad("Neurología")
doctor1.mostrar_info()

# Cambiar sueldo usando setters
doctor1.set_sueldo(6500000)
doctor1.mostrar_info()

# Intentar establecer un salario negativo (activará la validación)
doctor1.set_sueldo(-2000000)
doctor1.mostrar_info()