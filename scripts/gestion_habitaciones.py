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
    except json.JSONDecodeError:
        return []

def guardar_habitaciones(habitaciones):
    with open(ARCHIVO_HABITACIONES, "w") as f:
        json.dump(habitaciones, f, indent=4)

class GestionHabitaciones(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Gestión de Habitaciones")
        self.geometry("700x550")
        self.resizable(False, False)

        self.habitaciones = cargar_habitaciones()
        self.crear_widgets()
        self.mostrar_habitaciones()

    def crear_widgets(self):
        columnas = ("id", "piso", "tipo", "estado", "capacidad")
        self.tree = ttk.Treeview(self, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(pady=10)

        # Botón para cambiar estado
        btn_cambiar_estado = tk.Button(self, text="Cambiar Estado", command=self.cambiar_estado)
        btn_cambiar_estado.pack(pady=5)

        # Formulario para agregar habitación
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="ID Habitación:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_id = tk.Entry(form_frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Piso:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_piso = tk.Entry(form_frame)
        self.entry_piso.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Tipo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_tipo = tk.Entry(form_frame)
        self.entry_tipo.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Estado:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entry_estado = tk.Entry(form_frame)
        self.entry_estado.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Capacidad:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.entry_capacidad = tk.Entry(form_frame)
        self.entry_capacidad.grid(row=4, column=1, padx=5, pady=5)

        btn_agregar = tk.Button(form_frame, text="Agregar Habitación", command=self.agregar_habitacion)
        btn_agregar.grid(row=5, column=0, columnspan=2, pady=10)

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
        id_hab = self.entry_id.get().strip()
        piso = self.entry_piso.get().strip()
        tipo = self.entry_tipo.get().strip()
        estado = self.entry_estado.get().strip()
        capacidad = self.entry_capacidad.get().strip()

        if not all([id_hab, piso, tipo, estado, capacidad]):
            messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
            return

        if not capacidad.isdigit() or int(capacidad) <= 0:
            messagebox.showwarning("Capacidad inválida", "La capacidad debe ser un número entero positivo.")
            return

        if any(h["id"] == id_hab for h in self.habitaciones):
            messagebox.showerror("Error", "Ya existe una habitación con ese ID.")
            return

        nueva_habitacion = {
            "id": id_hab,
            "piso": piso,
            "tipo": tipo,
            "estado": estado,
            "capacidad": int(capacidad)
        }

        self.habitaciones.append(nueva_habitacion)
        guardar_habitaciones(self.habitaciones)
        self.mostrar_habitaciones()

        self.entry_id.delete(0, tk.END)
        self.entry_piso.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_estado.delete(0, tk.END)
        self.entry_capacidad.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Habitación agregada correctamente.")

    def cambiar_estado(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selección requerida", "Por favor, seleccione una habitación para cambiar su estado.")
            return

        item = selected[0]
        valores = self.tree.item(item, "values")
        id_hab = valores[0]

        # Buscar la habitación en la lista
        for hab in self.habitaciones:
            if hab["id"] == id_hab:
                estado_actual = hab.get("estado", "").lower()
                if estado_actual == "disponible":
                    hab["estado"] = "ocupado"
                else:
                    hab["estado"] = "disponible"
                break

        guardar_habitaciones(self.habitaciones)
        self.mostrar_habitaciones()
        messagebox.showinfo("Estado cambiado", f"El estado de la habitación {id_hab} ha sido actualizado.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    ventana = GestionHabitaciones(root)
    ventana.mainloop()
