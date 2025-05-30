from .users import User
from .gestion_clientes import ventanaCRUDclientes,ventanaCliente
from .gestion_rol import ventanaCRUDroles, cargarRoles
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os
import re

class gestionRecepcionistas:
    def __init__(self):
        self.archivo = "recepcionistas.json"

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                return json.load(f)
        return {}

    def guardar(self, data):
        with open(self.archivo, 'w') as f:
            json.dump(data, f, indent=4)

class gestionUsuarios:
    def __init__(self):
        self.archivo = "usuarios.json"

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as f:
                return json.load(f)
        return {}

    def guardar(self, data):
        with open(self.archivo, 'w') as f:
            json.dump(data, f, indent=4)

def verificacion(text):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(regex, text)

def buscar_correo(correo, dict):
    for data in dict.values():
        if correo == data.get("email"):
            return True
    return False

class ventanaRegistro:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.window = tk.Toplevel()
        self.window.title("Registrarse")
        self.window.geometry("400x250")

        tk.Label(self.window, text="Nombre completo:").pack(pady=5)
        self.nombre_entry = tk.Entry(self.window)
        self.nombre_entry.pack()
        
        tk.Label(self.window, text="Correo:").pack(pady=5)
        self.correo_entry = tk.Entry(self.window)
        self.correo_entry.pack()

        tk.Label(self.window, text="Contraseña:").pack(pady=5)
        self.contra_entry = tk.Entry(self.window, show="*")
        self.contra_entry.pack()

        tk.Button(self.window, text="Aceptar", command=self.guardar).pack(pady=10)
    
    def guardar(self): 
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get().strip()
        contra = self.contra_entry.get().strip()
        usuarios = self.user_manager.cargar()

        if buscar_correo(correo, usuarios):
            messagebox.showwarning("Error", "Este correo ya está registrado.")
        else:
            if not verificacion(correo):
                messagebox.showwarning("Error", "Correo invalido")
            else:
                if len(contra) < 7: 
                    messagebox.showwarning("Error", "contraseña invalida")
                elif correo and contra:
                    user = User(name=nombre, email=correo, password=contra)
                    usuarios[user.name] = user.get_user()
                    self.user_manager.guardar(usuarios)
                    try:
                        with open("clientes.json", "r") as f:
                            clientes=json.load(f)
                    except FileNotFoundError:
                        clientes={}

                    clientes[correo]={
                        "nombre": nombre,
                        "correo": correo,
                        "telefono": "No asignado"
                    }

                    with open("clientes.json", "w") as f:
                        json.dump(clientes, f, indent=4)
                    messagebox.showinfo("Éxito", "Cuenta creada exitosamente.")
                    self.window.destroy()
                else:
                    messagebox.showwarning("Campos vacíos", "Completa todos los campos.")

class ventanaCRUDrecepcionistas:
    def __init__(self, recepcionista_manager):
        self.recepcionista_manager = recepcionista_manager
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Recepcionistas")
        self.ventana.geometry("800x500")
        self.recepcionistas = self.recepcionista_manager.cargar()

        self.tree = ttk.Treeview(self.ventana, columns=("ID", "Nombre", "Email"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Email", text="Email")
        self.tree.pack(pady=10, fill='both', expand=True)

        self.actualizar_tabla()

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_recepcionista).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Editar", command=self.editar_recepcionista).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_recepcionista).grid(row=0, column=2, padx=5)

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        for id_recep, data in self.recepcionistas.items():
            self.tree.insert("", "end", values=(id_recep, data["nombre"], data["email"]))

    def agregar_recepcionista(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar Recepcionista")

        tk.Label(ventana, text="ID:").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack()

        tk.Label(ventana, text="Nombre:").pack()
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack()

        tk.Label(ventana, text="Email:").pack()
        email_entry = tk.Entry(ventana)
        email_entry.pack()


        def guardar_nuevo():
            id_recep = id_entry.get().strip()
            if not verificacion(email_entry.get().strip()):
                messagebox.showwarning("Error", "Correo inválido")
                return
            nombre = nombre_entry.get().strip()
            email = email_entry.get().strip()

            
            if id_recep and nombre and email:
                if id_recep in self.recepcionistas:
                    messagebox.showwarning("Error", "Este ID ya está registrado")
                else:
                    self.recepcionistas[id_recep] = {
                        "nombre": nombre,
                        "email": email,
                    }
                    self.recepcionista_manager.guardar(self.recepcionistas)
                    self.actualizar_tabla()
                    ventana.destroy()
            else:
                messagebox.showwarning("Error", "Todos los campos son obligatorios")

        tk.Button(ventana, text="Guardar", command=guardar_nuevo).pack(pady=5)

    def eliminar_recepcionista(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_recep = self.tree.item(seleccion[0])['values'][0]
            if messagebox.askyesno("Confirmar", f"¿Eliminar al recepcionista {id_recep}?"):
                del self.recepcionistas[id_recep]
                self.recepcionista_manager.guardar(self.recepcionistas)
                self.actualizar_tabla()

    def editar_recepcionista(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_recep = self.tree.item(seleccion[0])['values'][0]
            datos = self.recepcionistas[id_recep]

            ventana = tk.Toplevel(self.ventana)
            ventana.title("Editar Recepcionista")

            tk.Label(ventana, text=f"ID: {id_recep}").pack()
            
            tk.Label(ventana, text="Nombre:").pack()
            nombre_entry = tk.Entry(ventana)
            nombre_entry.insert(0, datos["nombre"])
            nombre_entry.pack()

            tk.Label(ventana, text="Email:").pack()
            email_entry = tk.Entry(ventana)
            email_entry.insert(0, datos["email"])
            email_entry.pack()



            def guardar_edicion():
                nuevo_nombre = nombre_entry.get().strip()
                nuevo_email = email_entry.get().strip()
                if not verificacion(nuevo_email):
                    messagebox.showwarning("Error", "Correo inválido")
                    return
                nuevo_email = email_entry.get().strip()

                
                if nuevo_nombre and nuevo_email:
                    self.recepcionistas[id_recep] = {
                        "nombre": nuevo_nombre,
                        "email": nuevo_email,
                    }
                    self.recepcionista_manager.guardar(self.recepcionistas)
                    self.actualizar_tabla()
                    ventana.destroy()
                else:
                    messagebox.showwarning("Error", "Todos los campos son obligatorios")

            tk.Button(ventana, text="Guardar Cambios", command=guardar_edicion).pack(pady=5)

    

class ventanaCRUDusuarios:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Usuarios")
        self.ventana.geometry("800x400")
        self.usuarios = self.user_manager.cargar()

        self.tree = ttk.Treeview(self.ventana, columns=("Nombre" ,"Correo", "Contraseña", "Rol"), show='headings')
        
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Correo", text="Correo")
        self.tree.heading("Contraseña", text="Contraseña")
        self.tree.heading("Rol", text="Rol")
        self.tree.pack(pady=10, fill='both', expand=True)

        self.actualizar_tabla()

        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", command=self.agregar_usuario).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Editar", command=self.editar_usuario).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_usuario).grid(row=0, column=2, padx=5)

    def actualizar_tabla(self):
        self.tree.delete(*self.tree.get_children())
        for nombre, data in self.usuarios.items():
            self.tree.insert("", "end", values=(nombre, data["email"] , data["password"], data["rol"]))

    def agregar_usuario(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar Usuario")


        tk.Label(ventana, text="Nombre:").pack()
        Nombre_entry = tk.Entry(ventana)
        Nombre_entry.pack()

        tk.Label(ventana, text="Correo:").pack()
        correo_entry = tk.Entry(ventana)
        correo_entry.pack()

        tk.Label(ventana, text="Contraseña:").pack()
        contra_entry = tk.Entry(ventana)
        contra_entry.pack()

        tk.Label(ventana, text="Rol:").pack()
        rol_combobox = ttk.Combobox(ventana, values=[rol for rol in cargarRoles().keys()])
        rol_combobox.set("usuario")
        rol_combobox.pack()

        def guardar_nuevo():
            Nombre = Nombre_entry.get()
            correo = correo_entry.get().strip()
            if not verificacion(correo):
                messagebox.showwarning("Error", "Correo inválido")
                return
            contra = contra_entry.get().strip()
            rol = rol_combobox.get()
            if correo and contra and rol and Nombre:
                self.usuarios[Nombre] = {"email": correo , "password": contra, "rol": rol}
                self.user_manager.guardar(self.usuarios)
                self.actualizar_tabla()
                ventana.destroy()

        tk.Button(ventana, text="Guardar", command=guardar_nuevo).pack(pady=5)

    def eliminar_usuario(self):
        seleccion = self.tree.selection()
        if seleccion:
            correo = self.tree.item(seleccion[0])['values'][0]
            if messagebox.askyesno("Confirmar", f"¿Eliminar a {correo}?"):
                del self.usuarios[correo]
                self.user_manager.guardar(self.usuarios)
                self.actualizar_tabla()

    def editar_usuario(self):
        seleccion = self.tree.selection()
        if seleccion:
            Nombre = self.tree.item(seleccion[0])['values'][0]
            datos = self.usuarios[Nombre]

            ventana = tk.Toplevel(self.ventana)
            ventana.title("Editar Usuario")

            tk.Label(ventana, text=f"Nombre: {Nombre}").pack()
            

            tk.Label(ventana, text="Nueva Contraseña:").pack()
            contra_entry = tk.Entry(ventana)
            contra_entry.insert(0, datos["password"])
            contra_entry.pack()

            tk.Label(ventana, text="Rol:").pack()
            rol_combobox = ttk.Combobox(ventana, values=[rol for rol in cargarRoles().keys()])
            rol_combobox.set(datos["rol"])
            rol_combobox.pack()

            def guardar_edicion():
                nueva_contra = contra_entry.get()
                if not verificacion(datos["email"]):
                    messagebox.showwarning("Error", "Correo inválido")
                    return
                nuevo_rol = rol_combobox.get()
                self.usuarios[Nombre] = {"email": datos["email"] ,"password": nueva_contra , "rol": nuevo_rol}
                self.user_manager.guardar(self.usuarios)
                self.actualizar_tabla()
                ventana.destroy()

            tk.Button(ventana, text="Guardar Cambios", command=guardar_edicion).pack(pady=5)
    
class ventanaAcceso:
    def __init__(self, parent):
        self.parent = parent
        self.user_manager = gestionUsuarios()
        self.recepcionista_manager = gestionRecepcionistas()

        self.frame = ttk.Frame(parent)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(self.frame, text="Inicio", font=("Arial", 18)).grid(column=0, row=0, columnspan=2, pady=10)
        ttk.Label(self.frame, text="Usuario", font=("Arial", 12)).grid(column=0, row=1, columnspan=2, pady=10)
        self.user_entry = ttk.Entry(self.frame, width=30)
        self.user_entry.grid(row=2, column=1, pady=5)

        ttk.Label(self.frame, text="Contraseña", font=("Arial", 12)).grid(column=0, row=3, columnspan=2, pady=10)
        self.pass_entry = ttk.Entry(self.frame, width=30, show="*")
        self.pass_entry.grid(row=4, column=1, pady=5)

        ttk.Button(self.frame, text="Aceptar", command=self.verificar).grid(column=0, row=5, columnspan=2, pady=10)
        ttk.Button(self.frame, text="Registrarse", command=lambda: ventanaRegistro(self.user_manager)).grid(column=0, row=6, columnspan=2, pady=5)

    def verificar(self):
        usuarios = self.user_manager.cargar()
        email = self.user_entry.get().strip()
        password = self.pass_entry.get().strip()
        login = False     
        logged_user = {}
        
        for name, dato in usuarios.items():
            if email == dato["email"]: 
                if password == dato["password"]:
                    logged_user = dato
                    login = True
                    break

        if login:
            messagebox.showinfo("Inicio de sesión correcto", f"Bienvenido {name}")
            for widget in self.parent.winfo_children():
                widget.destroy()
            if logged_user.get("rol") == "admin":
                menu_admin = tk.Toplevel()
                menu_admin.title("Menú de Administrador")
                menu_admin.geometry("300x200")
                tk.Button(menu_admin, text="Gestión de Clientes",
                        command=ventanaCRUDclientes).pack(pady=10)
                tk.Button(menu_admin, text="Gestión de Usuarios", 
                        command=lambda: ventanaCRUDusuarios(self.user_manager)).pack(pady=10)
                tk.Button(menu_admin, text="Gestión de Recepcionistas", 
                        command=lambda: ventanaCRUDrecepcionistas(self.recepcionista_manager)).pack(pady=10)
                tk.Button(menu_admin, text="Gestión de Roles", 
                        command=lambda: ventanaCRUDroles()).pack(pady=10)
            else:
                ventanaCliente(logged_user)
        else:
            messagebox.showinfo("Inicio de sesión inválido", "Usuario o contraseña incorrectos")