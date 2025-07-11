import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
from .gestion_habitaciones import cargar_habitaciones, guardar_habitaciones


ARCHIVO_INCIDENCIAS = "incidencias.json"

def cargar_incidencias():
    
    if not os.path.exists(ARCHIVO_INCIDENCIAS):
        with open(ARCHIVO_INCIDENCIAS, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4)
        return {}
    try:
        with open(ARCHIVO_INCIDENCIAS, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        messagebox.showwarning("Advertencia", "El archivo de incidencias está corrupto o vacío. Se creará uno nuevo.")
        with open(ARCHIVO_INCIDENCIAS, "w", encoding="utf-8") as f:
            json.dump({}, f, indent=4)
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar incidencias: {e}")
        return {}

def guardar_incidencias(incidencias):
    
    try:
        with open(ARCHIVO_INCIDENCIAS, "w", encoding="utf-8") as f:
            json.dump(incidencias, f, indent=4, ensure_ascii=False)
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar incidencias: {e}")


class GestionIncidencias:
    def __init__(self):
        self.incidencias = cargar_incidencias()

    def generar_id_incidencia(self):
        
        return datetime.now().strftime("INC%d%m%Y%H%M%S")

    def crear_incidencia(self, id_habitacion, tipo_incidencia, descripcion):
       
        if not id_habitacion or not tipo_incidencia or not descripcion:
            return False, "Todos los campos son obligatorios."

        id_incidencia = self.generar_id_incidencia()
        self.incidencias[id_incidencia] = {
            "id_habitacion": id_habitacion,
            "tipo_incidencia": tipo_incidencia,
            "descripcion": descripcion,
            "fecha_reporte": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "estado": "Pendiente", # Estado inicial
            "notas": "" # Notas adicionales sobre la resolución
        }
        guardar_incidencias(self.incidencias)

        
        self._actualizar_estado_habitacion(id_habitacion, "en_mantenimiento")

        return True, "Incidencia creada exitosamente."

    def obtener_incidencia(self, id_incidencia):
        
        return self.incidencias.get(id_incidencia)

    def obtener_todas_incidencias(self):
        
        return self.incidencias

    def actualizar_incidencia(self, id_incidencia, nuevo_tipo, nueva_descripcion, nuevo_estado, nuevas_notas=""):
        
        if id_incidencia not in self.incidencias:
            return False, "Incidencia no encontrada."
        if not nuevo_tipo or not nueva_descripcion or not nuevo_estado:
            return False, "Tipo, descripción y estado son obligatorios para la actualización."

        incidencia = self.incidencias[id_incidencia]
        incidencia["tipo_incidencia"] = nuevo_tipo
        incidencia["descripcion"] = nueva_descripcion
        incidencia["estado"] = nuevo_estado
        incidencia["notas"] = nuevas_notas

        guardar_incidencias(self.incidencias)

 
        if nuevo_estado == "Resuelta":
            self._actualizar_estado_habitacion(incidencia["id_habitacion"], "disponible")
        
        elif nuevo_estado in ["Pendiente", "En Proceso"]:
            self._actualizar_estado_habitacion(incidencia["id_habitacion"], "en_mantenimiento")


        return True, "Incidencia actualizada exitosamente."

    def eliminar_incidencia(self, id_incidencia):
        
        if id_incidencia in self.incidencias:
            incidencia = self.incidencias[id_incidencia]
            del self.incidencias[id_incidencia]
            guardar_incidencias(self.incidencias)
            
            if incidencia["estado"] in ["Pendiente", "En Proceso"]:
                pass
            return True, "Incidencia eliminada exitosamente."
        return False, "Incidencia no encontrada."

    def _actualizar_estado_habitacion(self, id_habitacion, nuevo_estado):

        habitaciones = cargar_habitaciones()
        encontrada = False
        for hab in habitaciones:
            if hab.get("id") == id_habitacion:
                hab["estado"] = nuevo_estado
                encontrada = True
                break
        if encontrada:
            guardar_habitaciones(habitaciones)
        else:
            messagebox.showwarning("Advertencia", f"Habitación {id_habitacion} no encontrada para actualizar su estado.")



class ventanaCRUDMantenimiento:
    def __init__(self):
        self.gestor_incidencias = GestionIncidencias()
        self.ventana = tk.Toplevel()
        self.ventana.title("Gestión de Mantenimiento / Incidencias")
        self.ventana.geometry("850x650")

       
        self.id_habitacion_var = tk.StringVar()
        self.tipo_incidencia_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()
        self.estado_var = tk.StringVar(value="Pendiente")
        self.notas_var = tk.StringVar()

       
        self.habitaciones_ids = [h["id"] for h in cargar_habitaciones()]

        
        frame_form = ttk.LabelFrame(self.ventana, text="Detalles de la Incidencia")
        frame_form.pack(pady=10, padx=10, fill="x")

        ttk.Label(frame_form, text="ID Habitación / Área:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Combobox(frame_form, textvariable=self.id_habitacion_var,
                     values=self.habitaciones_ids + ["General"]).grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_form, text="Tipo de Incidencia:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Combobox(frame_form, textvariable=self.tipo_incidencia_var,
                     values=["Fontanería", "Eléctrica", "Limpieza", "Mobilario", "Otro"]).grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_form, text="Descripción:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(frame_form, textvariable=self.descripcion_var).grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_form, text="Estado:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        ttk.Combobox(frame_form, textvariable=self.estado_var,
                     values=["Pendiente", "En Proceso", "Resuelta", "Cancelada"]).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        ttk.Label(frame_form, text="Notas de Resolución:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(frame_form, textvariable=self.notas_var).grid(row=4, column=1, padx=5, pady=5, sticky="ew")

        
        frame_botones = ttk.Frame(self.ventana)
        frame_botones.pack(pady=5)

        ttk.Button(frame_botones, text="Crear Incidencia", command=self.crear_incidencia).grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Actualizar Incidencia", command=self.actualizar_incidencia).grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Eliminar Incidencia", command=self.eliminar_incidencia).grid(row=0, column=2, padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar_campos).grid(row=0, column=3, padx=5)

        
        columnas = ("ID Incidencia", "ID Habitación", "Tipo", "Descripción", "Fecha Reporte", "Estado", "Notas")
        self.tree = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center") 
        
        self.tree.column("ID Incidencia", width=120)
        self.tree.column("Descripción", width=200)
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        # Cargar datos al seleccionar una fila
        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_seleccionados)

        self.actualizar_tabla()

    def limpiar_campos(self):
        self.id_habitacion_var.set("")
        self.tipo_incidencia_var.set("")
        self.descripcion_var.set("")
        self.estado_var.set("Pendiente")
        self.notas_var.set("")
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def crear_incidencia(self):
        id_habitacion = self.id_habitacion_var.get().strip()
        tipo = self.tipo_incidencia_var.get().strip()
        descripcion = self.descripcion_var.get().strip()

        exito, mensaje = self.gestor_incidencias.crear_incidencia(id_habitacion, tipo, descripcion)
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)

    def actualizar_incidencia(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una incidencia de la tabla para actualizar.")
            return

        id_incidencia = self.tree.item(seleccion[0], "values")[0] # Obtener el ID de la incidencia seleccionada
        nuevo_tipo = self.tipo_incidencia_var.get().strip()
        nueva_descripcion = self.descripcion_var.get().strip()
        nuevo_estado = self.estado_var.get().strip()
        nuevas_notas = self.notas_var.get().strip()

        exito, mensaje = self.gestor_incidencias.actualizar_incidencia(
            id_incidencia, nuevo_tipo, nueva_descripcion, nuevo_estado, nuevas_notas
        )
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.limpiar_campos()
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", mensaje)

    def eliminar_incidencia(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una incidencia de la tabla para eliminar.")
            return

        id_incidencia = self.tree.item(seleccion[0], "values")[0]

        if messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar la incidencia {id_incidencia}?"):
            exito, mensaje = self.gestor_incidencias.eliminar_incidencia(id_incidencia)
            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.limpiar_campos()
                self.actualizar_tabla()
            else:
                messagebox.showerror("Error", mensaje)

    def cargar_datos_seleccionados(self, event):
        
        seleccion = self.tree.selection()
        if seleccion:
            item = seleccion[0]
            valores = self.tree.item(item, "values")
            # Los valores en Treeview son: ID Incidencia, ID Habitación, Tipo, Descripción, Fecha Reporte, Estado, Notas
            self.id_habitacion_var.set(valores[1])
            self.tipo_incidencia_var.set(valores[2])
            self.descripcion_var.set(valores[3])
            
            self.estado_var.set(valores[5])
            self.notas_var.set(valores[6])

    def actualizar_tabla(self):
        
        # Limpiar tabla existente
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Cargar y mostrar incidencias actualizadas
        incidencias = self.gestor_incidencias.obtener_todas_incidencias()
        for id_incidencia, datos in incidencias.items():
            self.tree.insert("", "end", iid=id_incidencia, values=(
                id_incidencia,
                datos.get("id_habitacion", ""),
                datos.get("tipo_incidencia", ""),
                datos.get("descripcion", ""),
                datos.get("fecha_reporte", ""),
                datos.get("estado", ""),
                datos.get("notas", "")
            ))
        
        self.habitaciones_ids = [h["id"] for h in cargar_habitaciones()]
        self.habitaciones_ids.append("General") # Asegurarse que "General" siempre esté
        self.id_habitacion_var.set("") # Limpiar la selección actual
        
        for widget in self.ventana.winfo_children():
            if isinstance(widget, ttk.LabelFrame) and widget.cget("text") == "Detalles de la Incidencia":
                for child_widget in widget.winfo_children():
                    if isinstance(child_widget, ttk.Combobox) and child_widget.cget("textvariable") == str(self.id_habitacion_var):
                        child_widget.config(values=self.habitaciones_ids)
                        break
                break
