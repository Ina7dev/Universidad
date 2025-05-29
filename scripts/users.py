class User(): 
    def __init__(self, name = "" , email= "" , password = ""):
        self.name = name
        self.email = email
        self.password = password
        self.__is_admin = False


    def get_user(self):
        usuario = {
            "rol" :  "admin" if self.__is_admin else "usuario",   
            "email" : self.email,
            "password" : self.password 
        }
        return usuario
    
