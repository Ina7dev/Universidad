import tkinter as tk 
from tkinter import ttk
from scripts.Registro import Autentication


def Main():
        
    root = tk.Tk()
    root.title("Proyecto TPA")
    root.geometry("1280x720")
    root.resizable(False,False)
    root.configure(background="gray")
    
    frame = ttk.Frame(root,width=1270,height=700,) 
    frame.pack(pady=10, padx=10)
    frame.pack_propagate(False)
    
    Autentication(frame)   
    
    root.mainloop()
 

if __name__ == "__main__":
    Main()

    