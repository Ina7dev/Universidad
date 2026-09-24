import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime, timedelta

ARCHIVO_HABITACIONES = "habitaciones.json"
ARCHIVO_RESERVAS = "reservas.json"

def error_response(msg, parent=None):
    messagebox.showwarning("Error", msg, parent=parent)

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

def cargar_reservas():
    if os.path.exists(ARCHIVO_RESERVAS):
        with open(ARCHIVO_RESERVAS, "r") as f:
            return json.load(f)
    return {}

def guardar_reservas(reservas):
    with open(ARCHIVO_RESERVAS, "w") as f:
        json.dump(reservas, f, indent=4)

def validar_fechas(fecha_inicio, fecha_fin):
    try:
        fi = datetime.strptime(fecha_inicio, "%d-%m-%Y")
        ff = datetime.strptime(fecha_fin, "%d-%m-%Y")
        if fi >= ff:
            return False
        return True
    except Exception:
        return False

def fechas_solapan(f1_ini, f1_fin, f2_ini, f2_fin):
    # f1: nueva reserva, f2: reserva existente
    ini1 = datetime.strptime(f1_ini, "%d-%m-%Y")
    fin1 = datetime.strptime(f1_fin, "%d-%m-%Y")
    ini2 = datetime.strptime(f2_ini, "%d-%m-%Y")
    fin2 = datetime.strptime(f2_fin, "%d-%m-%Y")
    return not (fin1 <= ini2 or ini1 >= fin2)

def ver_habitaciones_disponibles(fecha_inicio, fecha_fin, tipo=None, piso=None):
    habitaciones = cargar_habitaciones()
    reservas = cargar_reservas()
    disponibles = []
    for hab in habitaciones:
        if tipo and hab.get("tipo", "").lower() != tipo.lower():
            continue
        if piso and str(hab.get("piso", "")) != str(piso):
            continue
        ocupada = False
        for r in reservas.values():
            if r.get("habitacion") == hab["id"]:
                if fechas_solapan(fecha_inicio, fecha_fin, r["entrada"], r["salida"]):
                    ocupada = True
                    break
        if not ocupada:
            disponibles.append(hab)
    return disponibles

def historial_reservas_habitacion(id_habitacion):
    reservas = cargar_reservas()
    hist = []
    for r in reservas.values():
        if r.get("habitacion") == id_habitacion:
            hist.append(r)
    return sorted(hist, key=lambda x: datetime.strptime(x["entrada"], "%d-%m-%Y"))

def reservar_habitacion(id_habitacion, datos_reserva):
    reservas = cargar_reservas()
    # Validar solapamiento
    for r in reservas.values():
        if r.get("habitacion") == id_habitacion:
            if fechas_solapan(datos_reserva["entrada"], datos_reserva["salida"], r["entrada"], r["salida"]):
                return False, "La habitación ya está reservada en ese rango de fechas."
    clave = f"{datos_reserva['cliente_id']}_{datos_reserva['entrada']}_{id_habitacion}"
    datos_reserva["habitacion"] = id_habitacion
    reservas[clave] = datos_reserva
    guardar_reservas(reservas)
    return True, clave

def cancelar_reserva(id_reserva):
    reservas = cargar_reservas()
    if id_reserva in reservas:
        del reservas[id_reserva]
        guardar_reservas(reservas)
        return True
    return False

def estado_actual_habitacion(id_hab):
    reservas = cargar_reservas()
    hoy = datetime.now()
    for r in reservas.values():
        if r.get("habitacion") == id_hab:
            entrada = datetime.strptime(r["entrada"], "%d-%m-%Y")
            salida = datetime.strptime(r["salida"], "%d-%m-%Y")
            if entrada <= hoy < salida:
                return "ocupado"
    return "disponible"

class GestionHabitaciones(tk.Toplevel):
    def __init__(self, master=None, on_close=None):
        super().__init__(master)
        self.title("Gestión de Habitaciones y Reservas")
        self.geometry("900x600")
        self.resizable(False, False)
        self.on_close = on_close
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.bind("<Escape>", lambda e: self.destroy())

        self.habitaciones = cargar_habitaciones()
        self.reservas = cargar_reservas()

        # Tabs: Habitaciones / Reservas
        self.tabs = ttk.Notebook(self)
        self.tab_hab = tk.Frame(self.tabs)
        self.tab_res = tk.Frame(self.tabs)
        self.tabs.add(self.tab_hab, text="Habitaciones")
        self.tabs.add(self.tab_res, text="Reservas")
        self.tabs.pack(fill="both", expand=True)

        self._crear_tab_habitaciones()
        self._crear_tab_reservas()

    def _on_close(self):
        self.destroy()
        if self.on_close:
            self.on_close()

    # --- TAB HABITACIONES ---
    def _crear_tab_habitaciones(self):
        # Buscador
        search_frame = tk.Frame(self.tab_hab)
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Buscar:").pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", self._filtrar_habitaciones)
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left")

        columnas = ("id", "piso", "tipo", "estado", "capacidad")
        self.tree = ttk.Treeview(self.tab_hab, columns=columnas, show="headings", height=10)
        for col in columnas:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(pady=10)

        btn_frame = tk.Frame(self.tab_hab)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Agregar Habitación", command=self.agregar_habitacion).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Ver Reservas de Habitación", command=self.ver_historial_habitacion).pack(side="left", padx=5)

        self.mostrar_habitaciones()

    def _filtrar_habitaciones(self, *args):
        filtro = self.search_var.get().lower()
        self.tree.delete(*self.tree.get_children())
        for hab in cargar_habitaciones():
            estado = estado_actual_habitacion(hab.get("id", ""))
            self.tree.insert("", "end", values=(
                hab.get("id", ""),
                hab.get("piso", ""),
                hab.get("tipo", ""),
                estado,
                hab.get("capacidad", "")
            ))

    def mostrar_habitaciones(self):
        self._filtrar_habitaciones()

    def agregar_habitacion(self):
        form = tk.Toplevel(self)
        form.title("Agregar Habitación")
        form.bind("<Escape>", lambda e: form.destroy())

        tk.Label(form, text="ID Habitación:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        entry_id = tk.Entry(form)
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Piso:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        entry_piso = tk.Entry(form)
        entry_piso.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form, text="Tipo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        entry_tipo = tk.Entry(form)
        entry_tipo.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form, text="Capacidad:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        entry_capacidad = tk.Entry(form)
        entry_capacidad.grid(row=3, column=1, padx=5, pady=5)

        def guardar():
            id_hab = entry_id.get().strip()
            piso = entry_piso.get().strip()
            tipo = entry_tipo.get().strip()
            capacidad = entry_capacidad.get().strip()

            if not id_hab or not piso or not tipo or not capacidad:
                return error_response("Todos los campos son obligatorios.", parent=self)
            if not capacidad.isdigit() or int(capacidad) <= 0 or int(capacidad) > 10:
                return error_response("La capacidad debe ser un número entero positivo (máximo 10).", parent=self)
            habitaciones = cargar_habitaciones()
            if any(h["id"] == id_hab for h in habitaciones):
                return error_response("Ya existe una habitación con ese ID.", parent=self)
            nueva_habitacion = {
                "id": id_hab,
                "piso": piso,
                "tipo": tipo,
                "capacidad": int(capacidad)
            }
            habitaciones.append(nueva_habitacion)
            guardar_habitaciones(habitaciones)
            self.mostrar_habitaciones()
            form.destroy()
            self.focus_set()

        tk.Button(form, text="Guardar", command=guardar).grid(row=4, column=0, columnspan=2, pady=10)

    def eliminar_habitacion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            error_response("Seleccione una habitación para eliminar.", parent=self)
            return
        id_hab = self.tree.item(seleccion[0], "values")[0]
        if estado_actual_habitacion(id_hab) == "ocupado":
            error_response("No se puede eliminar una habitación con reservas activas.", parent=self)
            return
        habitaciones = cargar_habitaciones()
        habitaciones = [h for h in habitaciones if h.get("id") != id_hab]
        guardar_habitaciones(habitaciones)
        self.mostrar_habitaciones()

    def ver_historial_habitacion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            error_response("Seleccione una habitación.", parent=self)
            return
        id_hab = self.tree.item(seleccion[0], "values")[0]
        historial = historial_reservas_habitacion(id_hab)
        ventana = tk.Toplevel(self)
        ventana.title(f"Reservas de Habitación {id_hab}")
        ventana.geometry("500x400")
        for r in historial:
            texto = f"Cliente: {r['cliente_id']}\nEntrada: {r['entrada']}\nSalida: {r['salida']}\nPersonas: {r.get('personas','')}"
            tk.Label(ventana, text=texto, relief="groove", padx=10, pady=5).pack(pady=5, fill="x")

    # --- TAB RESERVAS ---
    def _crear_tab_reservas(self):
        # Formulario de reserva
        form_frame = tk.Frame(self.tab_res)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Cliente:").grid(row=0, column=0, sticky="e")
        self.cliente_entry = tk.Entry(form_frame)
        self.cliente_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Fecha entrada (DD-MM-YYYY):").grid(row=1, column=0, sticky="e")
        self.entrada_entry = tk.Entry(form_frame)
        self.entrada_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Fecha salida (DD-MM-YYYY):").grid(row=2, column=0, sticky="e")
        self.salida_entry = tk.Entry(form_frame)
        self.salida_entry.grid(row=2, column=1)

        tk.Label(form_frame, text="Tipo habitación:").grid(row=3, column=0, sticky="e")
        self.tipo_var = tk.StringVar()
        self.tipo_combo = ttk.Combobox(form_frame, values=["estandar", "suite"], textvariable=self.tipo_var, state="readonly")
        self.tipo_combo.grid(row=3, column=1)
        self.tipo_combo.bind("<<ComboboxSelected>>", self._actualizar_habs_disponibles)

        tk.Label(form_frame, text="Piso:").grid(row=4, column=0, sticky="e")
        self.piso_var = tk.StringVar()
        self.piso_combo = ttk.Combobox(form_frame, values=["1", "2", "3"], textvariable=self.piso_var, state="readonly")
        self.piso_combo.grid(row=4, column=1)
        self.piso_combo.bind("<<ComboboxSelected>>", self._actualizar_habs_disponibles)

        tk.Label(form_frame, text="Habitación disponible:").grid(row=5, column=0, sticky="e")
        self.hab_var = tk.StringVar()
        self.hab_combo = ttk.Combobox(form_frame, values=[], textvariable=self.hab_var, state="readonly")
        self.hab_combo.grid(row=5, column=1)

        tk.Label(form_frame, text="Personas:").grid(row=6, column=0, sticky="e")
        self.personas_entry = tk.Entry(form_frame)
        self.personas_entry.grid(row=6, column=1)

        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Agregar Reserva", command=self.agregar_reserva).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancelar Reserva", command=self.eliminar_reserva).pack(side="left", padx=5)

        # Tabla de reservas
        columns = ("ID", "Cliente", "Habitación", "Entrada", "Salida", "Personas")
        self.tree_res = ttk.Treeview(self.tab_res, columns=columns, show="headings")
        for col in columns:
            self.tree_res.heading(col, text=col)
        self.tree_res.pack(pady=10, fill="both", expand=True)
        self.actualizar_tabla_reservas()

    def _actualizar_habs_disponibles(self, event=None):
        tipo = self.tipo_var.get()
        piso = self.piso_var.get()
        entrada = self.entrada_entry.get()
        salida = self.salida_entry.get()
        if not tipo or not piso or not entrada or not salida or not validar_fechas(entrada, salida):
            self.hab_combo.config(values=[])
            self.hab_var.set("")
            return
        disponibles = ver_habitaciones_disponibles(entrada, salida, tipo=tipo, piso=piso)
        self.hab_combo.config(values=[h["id"] for h in disponibles])
        if disponibles:
            self.hab_var.set(disponibles[0]["id"])
        else:
            self.hab_var.set("")

    def agregar_reserva(self):
        cliente = self.cliente_entry.get().strip()
        entrada = self.entrada_entry.get().strip()
        salida = self.salida_entry.get().strip()
        tipo = self.tipo_var.get()
        piso = self.piso_var.get()
        id_hab = self.hab_var.get()
        personas = self.personas_entry.get().strip()
        if not cliente or not entrada or not salida or not tipo or not piso or not id_hab or not personas:
            return error_response("Todos los campos son obligatorios.", parent=self)
        if not validar_fechas(entrada, salida):
            return error_response("Fechas inválidas.", parent=self)
        if not personas.isdigit() or int(personas) <= 0:
            return error_response("Personas debe ser un número positivo.", parent=self)
        datos_reserva = {
            "cliente_id": cliente,
            "entrada": entrada,
            "salida": salida,
            "personas": int(personas),
            "tipo_habitacion": tipo,
            "piso": piso
        }
        ok, msg = reservar_habitacion(id_hab, datos_reserva)
        if ok:
            messagebox.showinfo("Éxito", "Reserva agregada correctamente.", parent=self)
            self.actualizar_tabla_reservas()
            self._actualizar_habs_disponibles()
        else:
            error_response(msg)

    def eliminar_reserva(self):
        seleccion = self.tree_res.selection()
        if not seleccion:
            error_response("Seleccione una reserva para cancelar.", parent=self)
            return
        id_reserva = self.tree_res.item(seleccion[0], "values")[0]
        if cancelar_reserva(id_reserva):
            messagebox.showinfo("Éxito", "Reserva cancelada.", parent=self)
            self.actualizar_tabla_reservas()
            self._actualizar_habs_disponibles()
        else:
            error_response("No se pudo cancelar la reserva.", parent=self)

    def actualizar_tabla_reservas(self):
        self.tree_res.delete(*self.tree_res.get_children())
        reservas = cargar_reservas()
        for clave, r in reservas.items():
            self.tree_res.insert("", "end", values=(
                clave,
                r.get("cliente_id", ""),
                r.get("habitacion", ""),
                r.get("entrada", ""),
                r.get("salida", ""),
                r.get("personas", "")
            ))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    ventana = GestionHabitaciones(root)
    ventana.mainloop()
