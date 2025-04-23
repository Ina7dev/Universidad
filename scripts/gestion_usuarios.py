import tkinter as tk  # Para la creación de interfaces gráficas
from tkinter import ttk # Para widgets más avanzados de tkinter (como estilos modernos)
from tkinter import messagebox # Para mostrar cuadros de diálogo
import json  # Para manejar el archivo JSON de usuarios
import os # Para verificar la existencia de archivos



def cargar_usuarios():
    """
    Carga los usuarios desde el archivo JSON, si existe
    """
    if os.path.exists('usuarios.json'):
        with open('usuarios.json', 'r') as archivo:
            return json.load(archivo)
    return {}

def guardar_usuarios(usuarios):
    """
    Guarda el diccionario de usuarios en el archivo JSON
    """
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)

def registrarse():
    """
    Abre una ventana para que nuevos usuarios se registren con su correo y contraseña.
    El rol asignado será siempre 'usuario'.
    """
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrarse")
    ventana_registro.geometry("300x250")

    tk.Label(ventana_registro, text="Correo:").pack(pady=5)
    correo_entry = tk.Entry(ventana_registro)
    correo_entry.pack()

    tk.Label(ventana_registro, text="Contraseña:").pack(pady=5)
    contra_entry = tk.Entry(ventana_registro, show="*")
    contra_entry.pack()

    def guardar_registro():
        correo = correo_entry.get().strip()
        contra = contra_entry.get().strip()
        usuarios = cargar_usuarios()

        if correo in usuarios:
            messagebox.showwarning("Error", "Este correo ya está registrado.")
        elif correo and contra:
            usuarios[correo] = {
                "password": contra,
                "rol": "usuario"
            }
            guardar_usuarios(usuarios)
            messagebox.showinfo("Éxito", "Cuenta creada exitosamente.")
            ventana_registro.destroy()
        else:
            messagebox.showwarning("Campos vacíos", "Completa todos los campos.")

    tk.Button(ventana_registro, text="Registrarse", command=guardar_registro).pack(pady=10)



def abrir_crud_usuarios():
    """
    Abre una ventana con el sistema CRUD (Crear, Leer, Editar, Eliminar)
    para la gestión de usuarios. Solo accesible por administradores
    """
    ventana_crud = tk.Toplevel()
    ventana_crud.title("Gestión de Usuarios")
    ventana_crud.geometry("600x400")

    usuarios = cargar_usuarios()

    # Tabla para mostrar usuarios con columnas de correo, contraseña y rol
    tree = ttk.Treeview(ventana_crud, columns=("Correo", "Contraseña", "Rol"), show='headings')
    tree.heading("Correo", text="Correo")
    tree.heading("Contraseña", text="Contraseña")
    tree.heading("Rol", text="Rol")
    tree.pack(pady=10, fill='both', expand=True)

    def actualizar_tabla():
        """
        Limpia y vuelve a llenar la tabla con los datos actuales de usuarios
        """
        tree.delete(*tree.get_children())
        for correo, data in usuarios.items():
            tree.insert("", "end", values=(correo, data["password"], data["rol"]))

    actualizar_tabla()

    def agregar_usuario():
        """
        Abre una subventana para ingresar un nuevo usuario
        """
        def guardar_nuevo():
            nuevo_correo = correo_entry.get().strip()
            nueva_contra = contra_entry.get().strip()
            nuevo_rol = rol_combobox.get()

            if nuevo_correo and nueva_contra and nuevo_rol:
                usuarios[nuevo_correo] = {
                    "password": nueva_contra,
                    "rol": nuevo_rol
                }
                guardar_usuarios(usuarios)
                actualizar_tabla()
                ventana_agregar.destroy()

        ventana_agregar = tk.Toplevel(ventana_crud)
        ventana_agregar.title("Agregar Usuario")

        tk.Label(ventana_agregar, text="Correo:").pack()
        correo_entry = tk.Entry(ventana_agregar)
        correo_entry.pack()

        tk.Label(ventana_agregar, text="Contraseña:").pack()
        contra_entry = tk.Entry(ventana_agregar)
        contra_entry.pack()

        tk.Label(ventana_agregar, text="Rol:").pack()
        rol_combobox = ttk.Combobox(ventana_agregar, values=["admin", "usuario"])
        rol_combobox.set("usuario")
        rol_combobox.pack()

        tk.Button(ventana_agregar, text="Guardar", command=guardar_nuevo).pack(pady=5)

    def eliminar_usuario():
        """
        Elimina un usuario seleccionado de la tabla
        """
        seleccion = tree.selection()
        if seleccion:
            correo = tree.item(seleccion[0])['values'][0]
            if messagebox.askyesno("Confirmar", f"¿Eliminar a {correo}?"):
                del usuarios[correo]
                guardar_usuarios(usuarios)
                actualizar_tabla()

    def editar_usuario():
        """
        Abre una subventana para editar la contraseña o el rol del usuario seleccionado
        """
        seleccion = tree.selection()
        if seleccion:
            correo_seleccionado = tree.item(seleccion[0])['values'][0]
            datos = usuarios[correo_seleccionado]

            def guardar_edicion():
                nueva_contra = nueva_contra_entry.get()
                nuevo_rol = rol_combobox.get()
                usuarios[correo_seleccionado] = {
                    "password": nueva_contra,
                    "rol": nuevo_rol
                }
                guardar_usuarios(usuarios)
                actualizar_tabla()
                ventana_editar.destroy()

            ventana_editar = tk.Toplevel(ventana_crud)
            ventana_editar.title("Editar Usuario")

            tk.Label(ventana_editar, text=f"Correo: {correo_seleccionado}").pack()
            tk.Label(ventana_editar, text="Nueva Contraseña:").pack()
            nueva_contra_entry = tk.Entry(ventana_editar)
            nueva_contra_entry.insert(0, datos["password"])
            nueva_contra_entry.pack()

            tk.Label(ventana_editar, text="Rol:").pack()
            rol_combobox = ttk.Combobox(ventana_editar, values=["admin", "usuario"])
            rol_combobox.set(datos["rol"])
            rol_combobox.pack()

            tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_edicion).pack(pady=5)

    # Botones CRUD en la parte inferior de la ventana
    frame_botones = tk.Frame(ventana_crud)
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="Agregar", command=agregar_usuario).grid(row=0, column=0, padx=5)
    tk.Button(frame_botones, text="Editar", command=editar_usuario).grid(row=0, column=1, padx=5)
    tk.Button(frame_botones, text="Eliminar", command=eliminar_usuario).grid(row=0, column=2, padx=5)



def Autentication(parent):
    """
    Genera el formulario de login donde el usuario ingresa su correo y contraseña
    Verifica el rol y da acceso según corresponda
    """
    Loginframe = ttk.Frame(parent)
    Loginframe.place(relx=0.5, rely=0.5, anchor="center")

    # Etiquetas y campos de texto
    ttk.Label(Loginframe, text="Inicio", font=("Arial", 18)).grid(column=0, row=0, columnspan=2, pady=10)
    ttk.Label(Loginframe, text="Usuario", font=("Arial", 12)).grid(column=0, row=1, columnspan=2, pady=10)
    userEntry = ttk.Entry(Loginframe, width=30)
    userEntry.grid(row=2, column=1, pady=5)

    ttk.Label(Loginframe, text="Contraseña", font=("Arial", 12)).grid(column=0, row=3, columnspan=2, pady=10)
    passEntry = ttk.Entry(Loginframe, width=30)
    passEntry.grid(row=4, column=1, pady=5)

    # Función que se ejecuta al presionar "Aceptar"
    def Verify():
        """
        Verifica si el usuario existe y si la contraseña es correcta
        Redirige según el rol ('admin' o 'usuario')
        """
        usuarios = cargar_usuarios()
        email = userEntry.get().strip()
        password = passEntry.get().strip()

        if email in usuarios and usuarios[email]["password"] == password:
            rol = usuarios[email]["rol"]
            messagebox.showinfo("Inicio de sesión correcto", f"Bienvenido ({rol})")

            if rol == "admin":
                abrir_crud_usuarios()
            else:
                messagebox.showinfo("Acceso limitado", "Este usuario no tiene permisos para modificar usuarios.")
        else:
            messagebox.showinfo("Inicio de sesión inválido", "Usuario o contraseña incorrectos")

    # Botón de inicio de sesión
    ttk.Button(Loginframe, text="Aceptar", command=Verify).grid(column=0, row=5, columnspan=2, pady=10)
    #Botón de registro
    ttk.Button(Loginframe, text="Registrarse", command=registrarse).grid(column=0, row=6, columnspan=2, pady=5)


