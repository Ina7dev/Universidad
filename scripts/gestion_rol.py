from users import User
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

archivo_rol = "roles.json" 

def cargarRoles():
    if os.path.exists(archivo_rol):
        with open(archivo_rol, 'r') as f:
            return json.load(f)
    return {}

def guardarRol(data):
    with open(archivo_rol, 'w') as f:
        json.dump(data, f, indent=4)


class ventanaCRUDroles:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de rol")
        self.ventana.geometry("300x250")
        self.roles = cargarRoles()
        


        self.listbox = tk.Listbox(self.ventana)
        self.listbox.pack()
        self.actualizar()

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar",command=self.agregar_rol).grid(row=0, column=0, padx=5,)
        tk.Button(frame_botones, text="Editar", command=self.editar ).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar ).grid(row=0, column=2, padx=5)

    def actualizar(self):
        self.listbox.delete(0, tk.END)
        self.lista_roles = [rol for rol in self.roles.keys()]
        for item in self.lista_roles:
            self.listbox.insert(tk.END, item)

    def eliminar(self):
        from .gestion_usuarios import gestionUsuarios
        gestion = gestionUsuarios()  

        seleccion = self.listbox.curselection()
        print(seleccion)
        if seleccion:
            index = seleccion[0]
            rol_a_eliminar = self.lista_roles[index]
            if rol_a_eliminar == "admin":
                messagebox.showinfo("Atencion", "El rol a eliminar tiene permisos especiales")
            usuarios = gestion.cargar()
            for usuario , datos in usuarios.items():
                if datos["rol"] == rol_a_eliminar:
                    datos["rol"] = "none"
                    usuarios[usuario] = datos 
                    gestion.guardar(usuarios)

            del self.roles[rol_a_eliminar]
            guardarRol(self.roles)
            self.actualizar()
           





    def editar(self):
        seleccion = self.listbox.curselection()
        if seleccion: 
            index = seleccion[0]
            rol_actual = self.lista_roles[index]
            ventana = tk.Toplevel(self.ventana)
            ventana.title("Editar Rol")
            ventana.geometry("200x200")

            tk.Label(ventana, text=f"Nombre:").pack()
            nombre = tk.Entry(ventana)
            nombre.pack()
            def guardar_edicion():
                nuevo_nombre = nombre.get()
                # Actualizar usuarios con el rol antiguo
                usuarios = gestionUsuarios().cargar()
                for user, data in usuarios.items():
                    if data["rol"] == rol_actual:
                        data["rol"] = nuevo_nombre
                gestionUsuarios().guardar(usuarios)


            def guardar_edicion():
                nuevo_nombre = nombre.get()
                del self.roles[rol_actual]
                self.listbox.delete(index)
                self.listbox.insert(index, nuevo_nombre)
                self.roles[nuevo_nombre] = {   
                    
                }
                guardarRol(self.roles)
                ventana.destroy()
            tk.Button(ventana, text="Aceptar", command=guardar_edicion).pack(pady=10)

    def agregar_rol(self):

        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar rol")
        ventana.geometry("200x200")
        tk.Label(ventana, text="Nombre:").pack(pady=5)
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.pack()

        def guardar_nuevo():
            nombre = self.nombre_entry.get()
            if nombre:
                self.roles[nombre] = {}  
                guardarRol(self.roles)   
                self.actualizar()
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_nuevo).pack(pady=5)
        

