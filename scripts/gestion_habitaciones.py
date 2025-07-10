import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

ARCHIVO_HABITACIONES = "habitaciones.json"

def cargar_habitaciones():
    if not os.path.exists(ARCHIVO_HABITACIONES):
        with open(ARCHIVO_HABITACIONES, "w") as f:
            json.dump([], f)
        return []
    try:
        with open(ARCHIVO_HABITACIONES, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def guardar_habitaciones(habitaciones):
    with open(ARCHIVO_HABITACIONES, "w") as f:
        json.dump(habitaciones, f, indent=4)

class GestionHabitaciones(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gestión de Habitaciones")
        self.geometry("750x610")
        self.resizable(True, True)

        self.habitaciones = cargar_habitaciones()
        self.ids_permitidos = {
            "Piso 1": ["101", "102", "103", "104"],
            "Piso 2": ["201", "202", "203", "204"],
            "Piso 3": ["301", "302", "303", "304"]
        }
        self.crear_widgets()
        self.mostrar_habitaciones()

    def crear_widgets(self):
        # Treeview para mostrar habitaciones
        columnas = ("id", "piso", "tipo", "estado", "capacidad")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings", height=15)
        for col in columnas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Frame de botones superiores
        btn_top_frame = tk.Frame(self)
        btn_top_frame.pack(pady=5)
        
        btn_cambiar_estado = tk.Button(btn_top_frame, text="Cambiar Estado", command=self.cambiar_estado)
        btn_cambiar_estado.pack(side=tk.LEFT, padx=5)
        
        btn_eliminar = tk.Button(btn_top_frame, text="Eliminar Habitación", command=self.eliminar_habitacion)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Formulario para agregar habitación
        form_frame = tk.LabelFrame(self, text="Agregar Nueva Habitación")
        form_frame.pack(pady=10, padx=10, fill="x", expand=True)

        # Campos del formulario
        tk.Label(form_frame, text="Piso:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.combo_piso = ttk.Combobox(form_frame, values=["Piso 1", "Piso 2", "Piso 3"], state="readonly")
        self.combo_piso.grid(row=0, column=1, padx=5, pady=5, sticky="we")
        self.combo_piso.bind("<<ComboboxSelected>>", self.actualizar_ids)

        tk.Label(form_frame, text="ID Habitación:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.combo_id = ttk.Combobox(form_frame, state="readonly")
        self.combo_id.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        tk.Label(form_frame, text="Tipo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_tipo = tk.Entry(form_frame, state="readonly")
        self.entry_tipo.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        tk.Label(form_frame, text="Estado:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.combo_estado = ttk.Combobox(form_frame, values=["Disponible", "Ocupado"], state="readonly")
        self.combo_estado.grid(row=3, column=1, padx=5, pady=5, sticky="we")
        self.combo_estado.current(0)

        tk.Label(form_frame, text="Capacidad:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_capacidad = tk.Entry(form_frame, state="readonly")
        self.entry_capacidad.grid(row=4, column=1, padx=5, pady=5, sticky="we")

        # Botones inferiores
        btn_bottom_frame = tk.Frame(form_frame)
        btn_bottom_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")
        
        btn_agregar = tk.Button(btn_bottom_frame, text="Agregar Habitación", command=self.agregar_habitacion)
        btn_agregar.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(btn_bottom_frame, text="Limpiar Formulario", command=self.limpiar_form)
        btn_limpiar.pack(side=tk.LEFT, padx=5)

        # Inicializar valores
        self.combo_piso.current(0)
        self.actualizar_ids()

    def actualizar_ids(self, event=None):
        piso = self.combo_piso.get()
        ids = self.ids_permitidos.get(piso, [])
        self.combo_id["values"] = ids
        if ids:
            self.combo_id.current(0)
        
        # Actualizar tipo y capacidad según piso
        if piso in ["Piso 1", "Piso 2"]:
            self.entry_tipo.config(state="normal")
            self.entry_tipo.delete(0, tk.END)
            self.entry_tipo.insert(0, "Estándar")
            self.entry_tipo.config(state="readonly")
            
            self.entry_capacidad.config(state="normal")
            self.entry_capacidad.delete(0, tk.END)
            self.entry_capacidad.insert(0, "2")
            self.entry_capacidad.config(state="readonly")
        elif piso == "Piso 3":
            self.entry_tipo.config(state="normal")
            self.entry_tipo.delete(0, tk.END)
            self.entry_tipo.insert(0, "Suite")
            self.entry_tipo.config(state="readonly")
            
            self.entry_capacidad.config(state="normal")
            self.entry_capacidad.delete(0, tk.END)
            self.entry_capacidad.insert(0, "4")
            self.entry_capacidad.config(state="readonly")

    def mostrar_habitaciones(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for hab in self.habitaciones:
            self.tree.insert("", "end", values=(
                hab.get("id", ""),
                hab.get("piso", ""),
                hab.get("tipo", ""),
                hab.get("estado", ""),
                hab.get("capacidad", "")
            ))

    def agregar_habitacion(self):
        id_hab = self.combo_id.get()
        piso = self.combo_piso.get()
        tipo = self.entry_tipo.get()
        estado = self.combo_estado.get()
        capacidad = self.entry_capacidad.get()

        # Validar ID único
        if any(h["id"] == id_hab for h in self.habitaciones):
            messagebox.showerror("Error", "Ya existe una habitación con ese ID.")
            return

        # Validar combinación piso-tipo
        if piso in ["Piso 1", "Piso 2"] and tipo != "Estándar":
            messagebox.showerror("Error", "Solo se permiten habitaciones estándar en este piso.")
            return
        if piso == "Piso 3" and tipo != "Suite":
            messagebox.showerror("Error", "Solo se permiten suites en este piso.")
            return

        # Crear nueva habitación
        nueva_habitacion = {
            "id": id_hab,
            "piso": piso,
            "tipo": tipo,
            "estado": estado,
            "capacidad": int(capacidad)
        }

        # Guardar y actualizar
        self.habitaciones.append(nueva_habitacion)
        guardar_habitaciones(self.habitaciones)
        self.mostrar_habitaciones()
        messagebox.showinfo("Éxito", "Habitación agregada correctamente.")
        self.limpiar_form()

    def cambiar_estado(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selección requerida", "Seleccione una habitación para cambiar su estado.")
            return

        item = selected[0]
        valores = self.tree.item(item, "values")
        id_hab = valores[0]

        # Buscar y actualizar estado
        for hab in self.habitaciones:
            if hab["id"] == id_hab:
                hab["estado"] = "Disponible" if hab["estado"] == "Ocupado" else "Ocupado"
                break

        # Guardar y actualizar
        guardar_habitaciones(self.habitaciones)
        self.mostrar_habitaciones()
        messagebox.showinfo("Estado cambiado", f"Estado de {id_hab} actualizado a {hab['estado']}")

    def eliminar_habitacion(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selección requerida", "Seleccione una habitación para eliminar.")
            return

        item = selected[0]
        valores = self.tree.item(item, "values")
        id_hab = valores[0]

        if messagebox.askyesno("Confirmar", f"¿Eliminar habitación {id_hab}?"):
            self.habitaciones = [h for h in self.habitaciones if h["id"] != id_hab]
            guardar_habitaciones(self.habitaciones)
            self.mostrar_habitaciones()
            messagebox.showinfo("Éxito", "Habitación eliminada correctamente.")

    def limpiar_form(self):
        self.combo_piso.current(0)
        self.actualizar_ids()
        self.combo_estado.current(0)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    ventana = GestionHabitaciones(root)
    ventana.mainloop()
