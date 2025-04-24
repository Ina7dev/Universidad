
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os



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



class ventanaRegistro:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.window = tk.Toplevel()
        self.window.title("Registrarse")
        self.window.geometry("300x250")

        tk.Label(self.window, text="Correo:").pack(pady=5)
        self.correo_entry = tk.Entry(self.window)
        self.correo_entry.pack()

        tk.Label(self.window, text="Contraseña:").pack(pady=5)
        self.contra_entry = tk.Entry(self.window, show="*")
        self.contra_entry.pack()

        tk.Button(self.window, text="Registrarse", command=self.guardar).pack(pady=10)

    def guardar(self):
        correo = self.correo_entry.get().strip()
        contra = self.contra_entry.get().strip()
        usuarios = self.user_manager.cargar()

        if correo in usuarios:
            messagebox.showwarning("Error", "Este correo ya está registrado.")
        elif correo and contra:
            usuarios[correo] = {"password": contra, "rol": "usuario"}
            self.user_manager.guardar(usuarios)
            messagebox.showinfo("Éxito", "Cuenta creada exitosamente.")
            self.window.destroy()
        else:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")



class ventanaCRUDusuarios:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Usuarios")
        self.ventana.geometry("600x400")
        self.usuarios = self.user_manager.cargar()

        self.tree = ttk.Treeview(self.ventana, columns=("Correo", "Contraseña", "Rol"), show='headings')
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
        for correo, data in self.usuarios.items():
            self.tree.insert("", "end", values=(correo, data["password"], data["rol"]))

    def agregar_usuario(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar Usuario")

        tk.Label(ventana, text="Correo:").pack()
        correo_entry = tk.Entry(ventana)
        correo_entry.pack()

        tk.Label(ventana, text="Contraseña:").pack()
        contra_entry = tk.Entry(ventana)
        contra_entry.pack()

        tk.Label(ventana, text="Rol:").pack()
        rol_combobox = ttk.Combobox(ventana, values=["admin", "usuario"])
        rol_combobox.set("usuario")
        rol_combobox.pack()

        def guardar_nuevo():
            correo = correo_entry.get().strip()
            contra = contra_entry.get().strip()
            rol = rol_combobox.get()
            if correo and contra and rol:
                self.usuarios[correo] = {"password": contra, "rol": rol}
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
            correo = self.tree.item(seleccion[0])['values'][0]
            datos = self.usuarios[correo]

            ventana = tk.Toplevel(self.ventana)
            ventana.title("Editar Usuario")

            tk.Label(ventana, text=f"Correo: {correo}").pack()
            tk.Label(ventana, text="Nueva Contraseña:").pack()
            contra_entry = tk.Entry(ventana)
            contra_entry.insert(0, datos["password"])
            contra_entry.pack()

            tk.Label(ventana, text="Rol:").pack()
            rol_combobox = ttk.Combobox(ventana, values=["admin", "usuario"])
            rol_combobox.set(datos["rol"])
            rol_combobox.pack()

            def guardar_edicion():
                nueva_contra = contra_entry.get()
                nuevo_rol = rol_combobox.get()
                self.usuarios[correo] = {"password": nueva_contra, "rol": nuevo_rol}
                self.user_manager.guardar(self.usuarios)
                self.actualizar_tabla()
                ventana.destroy()

            tk.Button(ventana, text="Guardar Cambios", command=guardar_edicion).pack(pady=5)



class ventanaAcceso:
    def __init__(self, parent):
        self.parent = parent
        self.user_manager = gestionUsuarios()

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

        if email in usuarios and usuarios[email]["password"] == password:
            rol = usuarios[email]["rol"]
            messagebox.showinfo("Inicio de sesión correcto", f"Bienvenido ({email})")
            if rol == "admin":
                ventanaCRUDusuarios(self.user_manager)
            else:
                messagebox.showinfo("Acceso limitado", "Este usuario no tiene permisos para modificar usuarios.")
        else:
            messagebox.showinfo("Inicio de sesión inválido", "Usuario o contraseña incorrectos")
