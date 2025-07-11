import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

ARCHIVO_FEEDBACK = "feedback.json"

# Cargar feedback
def cargar_feedback():
    if os.path.exists(ARCHIVO_FEEDBACK):
        with open(ARCHIVO_FEEDBACK, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Guardar feedback
def guardar_feedback(data):
    with open(ARCHIVO_FEEDBACK, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

class ventanaCRUDfeedback:
    def __init__(self):
        self.feedback = cargar_feedback()
        self.ventana = tk.Toplevel()

        self.ventana.transient()
        self.ventana.grab_set()
        self.ventana.focus_set()
        
        self.ventana.title("Gestión de Sugerencias y Reclamos")
        self.ventana.geometry("900x500")

        frame = ttk.Frame(self.ventana, style="Login.TFrame", width=880, height=480)
        frame.pack(expand=True, fill="both")
        frame.grid_propagate(False)

        columnas = ("ID", "Email", "Tipo", "Mensaje", "Estado", "Respuesta")
        self.tree = ttk.Treeview(frame, columns=columnas, show="headings")
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor="center")
        self.tree.pack(pady=10, fill="both", expand=True)
        self.actualizar_tabla()

        frame_botones = ttk.Frame(frame, style="Login.TFrame")
        frame_botones.pack(pady=10)
        ttk.Button(frame_botones, text="Agregar", command=self.agregar_feedback, style="Login.TButton").grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Responder/Editar", command=self.editar_feedback, style="Login.TButton").grid(row=0, column=1, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_feedback, style="Login.TButton").grid(row=0, column=2, padx=5)
        ttk.Button(frame_botones, text="Marcar como Resuelto", command=self.marcar_resuelto, style="Login.TButton").grid(row=0, column=3, padx=5)

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for fid, data in self.feedback.items():
            self.tree.insert("", "end", iid=fid, values=(fid, data["email"], data["tipo"], data["mensaje"], data["estado"], data.get("respuesta", "")))

    def agregar_feedback(self):
        self.ventana_formulario("Agregar Sugerencia/Reclamo")

    def editar_feedback(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Seleccionar", "Seleccione un feedback para editar/responder.", parent=self.ventana)
            return
        fid = seleccionado[0]
        self.ventana_formulario("Responder/Editar Feedback", fid)

    def eliminar_feedback(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Seleccionar", "Seleccione un feedback para eliminar.", parent=self.ventana)
            return
        fid = seleccionado[0]
        if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este feedback?", parent=self.ventana):
            del self.feedback[fid]
            guardar_feedback(self.feedback)
            self.actualizar_tabla()

    def marcar_resuelto(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Seleccionar", "Seleccione un feedback para marcar como resuelto.", parent=self.ventana)
            return
        fid = seleccionado[0]
        self.feedback[fid]["estado"] = "resuelto"
        guardar_feedback(self.feedback)
        self.actualizar_tabla()

    def ventana_formulario(self, titulo, fid=None):
        ventana = tk.Toplevel(self.ventana)

        self.ventana.transient()
        self.ventana.grab_set()
        self.ventana.focus_set()

        ventana.title(titulo)
        ventana.geometry("400x400")
        form_frame = ttk.Frame(ventana, style="Login.TFrame", width=380, height=380)
        form_frame.pack(expand=True, fill="both")
        form_frame.grid_propagate(False)

        if fid:
            datos = self.feedback[fid]
        else:
            datos = {"email": "", "tipo": "Sugerencia", "mensaje": "", "estado": "pendiente", "respuesta": ""}

        ttk.Label(form_frame, text="Email:", style="Login.TLabel").pack(pady=5)
        email_entry = ttk.Entry(form_frame)
        email_entry.pack()
        email_entry.insert(0, datos["email"])
        email_entry.config(state="normal" if not fid else "disabled")

        ttk.Label(form_frame, text="Tipo:", style="Login.TLabel").pack(pady=5)
        tipo_var = tk.StringVar(value=datos["tipo"])
        tipo_combo = ttk.Combobox(form_frame, values=["Sugerencia", "Reclamo"], textvariable=tipo_var, state="readonly")
        tipo_combo.pack()
        tipo_combo.config(state="normal" if not fid else "disabled")

        ttk.Label(form_frame, text="Mensaje:", style="Login.TLabel").pack(pady=5)
        mensaje_text = tk.Text(form_frame, height=5, width=40)
        mensaje_text.pack()
        mensaje_text.insert("1.0", datos["mensaje"])
        mensaje_text.config(state="normal" if not fid else "disabled")

        ttk.Label(form_frame, text="Estado:", style="Login.TLabel").pack(pady=5)
        estado_var = tk.StringVar(value=datos["estado"])
        estado_entry = ttk.Entry(form_frame, textvariable=estado_var, state="readonly")
        estado_entry.pack()

        ttk.Label(form_frame, text="Respuesta (admin):", style="Login.TLabel").pack(pady=5)
        respuesta_text = tk.Text(form_frame, height=3, width=40)
        respuesta_text.pack()
        respuesta_text.insert("1.0", datos.get("respuesta", ""))

        def guardar():
            if not fid:
                email = email_entry.get().strip()
                tipo = tipo_var.get()
                mensaje = mensaje_text.get("1.0", "end").strip()
                if not email or not mensaje:
                    messagebox.showerror("Error", "Email y mensaje son obligatorios.", parent=self.ventana)
                    return
                nuevo_id = f"{email}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
                self.feedback[nuevo_id] = {
                    "email": email,
                    "tipo": tipo,
                    "mensaje": mensaje,
                    "estado": "pendiente",
                    "respuesta": ""
                }
            else:
                self.feedback[fid]["respuesta"] = respuesta_text.get("1.0", "end").strip()
                self.feedback[fid]["estado"] = "resuelto" if self.feedback[fid]["respuesta"] else self.feedback[fid]["estado"]
            guardar_feedback(self.feedback)
            self.actualizar_tabla()
            ventana.destroy()

        ttk.Button(form_frame, text="Guardar", command=guardar, style="Login.TButton").pack(pady=10)

class ventanaFeedbackCliente:
    def __init__(self, usuario):
        self.usuario = usuario
        self.feedback = cargar_feedback()
        self.ventana = tk.Toplevel()

        self.ventana.transient()
        self.ventana.grab_set()
        self.ventana.focus_set()

        self.ventana.title("Mis Sugerencias y Reclamos")
        self.ventana.geometry("900x500")

        # Aplica el estilo Login.TFrame al fondo
        frame = ttk.Frame(self.ventana, style="Login.TFrame")
        frame.pack(expand=True, fill="both")
        columnas = ("ID", "Tipo", "Mensaje", "Estado", "Respuesta", "Acciones")
        self.tree = ttk.Treeview(frame, columns=columnas, show="headings")
        for col in columnas[:-1]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="center")
        self.tree.heading("Acciones", text="Acciones")
        self.tree.column("Acciones", width=100, anchor="center")
        self.tree.pack(pady=10, fill="both", expand=True)
        self.actualizar_tabla()

        frame_botones = ttk.Frame(frame, style="Login.TFrame")
        frame_botones.pack(pady=10)
        ttk.Button(frame_botones, text="Agregar", command=self.agregar_feedback, style="Login.TButton").grid(row=0, column=0, padx=5)
        ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_feedback, style="Login.TButton").grid(row=0, column=1, padx=5)

    def filtrar_feedbacks_cliente(self):
        email = self.usuario.get("email")
        return {fid: data for fid, data in self.feedback.items() if data.get("email") == email}

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for fid, data in self.filtrar_feedbacks_cliente().items():
            estado = data["estado"]
            respuesta = data.get("respuesta", "")
            acciones = ""
            # Solo puede eliminar si no ha sido respondido
            if estado == "pendiente" and not respuesta:
                acciones = "Eliminar"
            self.tree.insert(
                "", "end", iid=fid,
                values=(fid, data["tipo"], data["mensaje"], estado, respuesta, acciones)
            )

    def agregar_feedback(self):
        self.ventana_formulario("Agregar Sugerencia/Reclamo")

    def eliminar_feedback(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Seleccionar", "Seleccione un feedback para eliminar.", parent=self.ventana)
            return
        fid = seleccionado[0]
        data = self.feedback.get(fid)
        # Validación backend: solo puede eliminar si es suyo y no ha sido respondido
        if data and data.get("email") == self.usuario.get("email") and data.get("estado") == "pendiente" and not data.get("respuesta"):
            if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar este feedback?", parent=self.ventana):
                del self.feedback[fid]
                guardar_feedback(self.feedback)
                self.actualizar_tabla()
        else:
            messagebox.showwarning("No permitido", "Solo puede eliminar feedbacks propios que no han sido respondidos.", parent=self.ventana)

    def ventana_formulario(self, titulo, fid=None):
        ventana = tk.Toplevel(self.ventana)

        self.ventana.transient()
        self.ventana.grab_set()
        self.ventana.focus_set()

        ventana.title(titulo)
        ventana.geometry("400x400")
        # Aplica el estilo Login.TFrame al fondo
        form_frame = ttk.Frame(ventana, style="Login.TFrame", width=380, height=380)
        form_frame.pack(expand=True, fill="both")
        form_frame.grid_propagate(False)
        datos = {"email": self.usuario.get("email"), "tipo": "Sugerencia", "mensaje": "", "estado": "pendiente", "respuesta": ""}

        # Usa Login.TLabel para los textos, fuente grande y negrita
        ttk.Label(form_frame, text="Email:", style="Login.TLabel").pack(pady=5)
        email_entry = ttk.Entry(form_frame)
        email_entry.pack()
        email_entry.insert(0, datos["email"])
        email_entry.config(state="disabled")

        ttk.Label(form_frame, text="Tipo:", style="Login.TLabel").pack(pady=5)
        tipo_var = tk.StringVar(value=datos["tipo"])
        tipo_combo = ttk.Combobox(form_frame, values=["Sugerencia", "Reclamo"], textvariable=tipo_var, state="readonly")
        tipo_combo.pack()

        ttk.Label(form_frame, text="Mensaje:", style="Login.TLabel").pack(pady=5)
        mensaje_text = tk.Text(form_frame, height=5, width=40)
        mensaje_text.pack()

        def guardar():
            mensaje = mensaje_text.get("1.0", "end").strip()
            if not mensaje:
                messagebox.showerror("Error", "El mensaje es obligatorio.", parent=self.ventana)
                return
            nuevo_id = f"{self.usuario.get('email')}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            self.feedback[nuevo_id] = {
                "email": self.usuario.get("email"),
                "tipo": tipo_var.get(),
                "mensaje": mensaje,
                "estado": "pendiente",
                "respuesta": ""
            }
            guardar_feedback(self.feedback)
            self.actualizar_tabla()
            ventana.destroy()

        ttk.Button(form_frame, text="Guardar", command=guardar, style="Login.TButton").pack(pady=10)
