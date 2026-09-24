class Doctor:
    def __init__(self, nombre, especialidad, sueldo):
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__sueldo = sueldo

    # Getter y Setter para el nombre usando @property
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
            self.__nombre = nuevo_nombre
        else:
            print("Error: El nombre no puede estar vacío")

    # Getter y Setter para la especialidad usando @property
    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        if len(nueva_especialidad) > 0:
            self.__especialidad = nueva_especialidad
        else:
            print("Error: La especialidad no puede estar vacía")

    # Getter y Setter para el sueldo usando @property
    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        if nuevo_sueldo >= 0:
            self.__sueldo = nuevo_sueldo
        else:
            print("Error: El sueldo no puede ser negativo")

    # Método para mostrar información del doctor
    def mostrar_info(self):
        print(f"Doctor: {self.__nombre}, Especialidad: {self.__especialidad}, Sueldo: {self.__sueldo}")

# Instancia de ejemplo usando @property
doctor1 = Doctor("Dr. Yoel Cea", "Cardiología", 5000000)

# Acceder a los atributos usando @property
doctor1.mostrar_info()  # Doctor: Dr. Yoel Cea, Especialidad: Cardiología, Sueldo: 5000000

# Modificar los atributos usando los setters con @property
doctor1.nombre = "Dr. Ana López"
doctor1.especialidad = "Neurología"
doctor1.sueldo = 6500000
doctor1.mostrar_info()  # Doctor: Dr. Ana López, Especialidad: Neurología, Sueldo: 6500000

# Intentar establecer un sueldo negativo
doctor1.sueldo = -2000000  # Error: El sueldo no puede ser negativo