import tkinter as tk 
from tkinter import ttk
from scripts.gestion_usuarios import ventanaAcceso

def mostrar_login(root):
    # Destruye todas las ventanas secundarias abiertas
    for w in root.winfo_children():
        if isinstance(w, tk.Toplevel):
            w.destroy()
    # Limpia el frame principal si existe
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Frame):
            widget.destroy()
    # Muestra el login
    ventanaAcceso(root, on_all_closed=lambda: mostrar_login(root))

def main():
    root = tk.Tk()
    root.title("Sistema de Gestión Hotelera")
    root.geometry("1280x720")
    root.resizable(False, False)
    root.configure(background="gray")
    mostrar_login(root)
    root.mainloop()

if __name__ == "__main__":
    main()