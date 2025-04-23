import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


USUARIOS = { #esto deberia ser la info del json con los usuarios  para despues compararlo con la info y ver si se logea
    "cristobalalexis.onate@alumnos.ulagos.cl" : "@a507209C"
}


def Autentication(parent):
    #Frame Login
    Loginframe = ttk.Frame(parent)
    Loginframe.place(relx=0.5, rely=0.5, anchor="center")
    
    #Titulo 
    ttk.Label(Loginframe, text="REGRISTRO",font=("Arial", 18)).grid(column=0,row=0, columnspan=2, pady=10)

    #Campo de Usuario 
    ttk.Label(Loginframe, text="Usuario",font=("Arial", 12)).grid(column=0,row=1, columnspan=2, pady=10)
    userEntry = ttk.Entry(Loginframe, width=30)
    userEntry.grid(row=2, column=1, pady=5)

    #Campo de Contraseña 
    ttk.Label(Loginframe, text="Contraseña",font=("Arial", 12)).grid(column=0,row=3, columnspan=2, pady=10)
    passEntry = ttk.Entry(Loginframe, width=30)
    passEntry.grid(row=4, column=1, pady=5)

    #Submit button
    def Verify():
        """Esta es la funcion que detecta cuando el boton es presionado y  ve si esta o no en el registro de usuarios y si
        el usuario y contraseña son iguales"""
        email = userEntry.get()
        password = passEntry.get()
        if email in USUARIOS and USUARIOS[email] == password:
            messagebox.showinfo("Inicio de sesion correcto", "Usuario loggeado")
            #cuando este logeado pasara a otra pantalla para modificar usuarios y agregar nuevos o editar los que esten (CRUD)
        else: 
            messagebox.showinfo("inicio de sesion invalido", "usuario o contraseña incorrectos")

    
    btn = ttk.Button(Loginframe, text="Submit", command=Verify)
    btn.grid(column=0,row=5, columnspan=2, pady=10)

