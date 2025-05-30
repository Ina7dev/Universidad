
class User(): 
    def __init__(self, name="", email="", password="", rol="usuario"):
        self.name = name
        self.email = email
        self.password = password
        self.rol = rol  # Nuevo parámetro para el rol

    def get_user(self):
        return {
            "rol": self.rol,
            "email": self.email,
            "password": self.password
        }