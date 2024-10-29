# saludo_gui.py

import tkinter as tk
from tkinter import messagebox

def mostrar_saludo():
    nombre = entrada_nombre.get()
    saludo = f"¡Hola, {nombre}! Bienvenido a tu primer programa ejecutable."
    messagebox.showinfo("Saludo", saludo)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Programa de Saludo")
ventana.geometry("300x150")

# Etiqueta y campo de entrada
etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack(pady=10)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

# Botón para mostrar el saludo
boton = tk.Button(ventana, text="Saludar", command=mostrar_saludo)
boton.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
