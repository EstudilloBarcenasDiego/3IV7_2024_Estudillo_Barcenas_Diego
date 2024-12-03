import tkinter as tk
from tkinter import messagebox
def crear_interfaz(grafo, aristas, nodos, logica): 
    ventana = tk.Tk()
    ventana.title("Planificación de Rutas")
    ventana.geometry("800x600")  # Aquí se corrige la 'X' mayúscula por una 'x' minúscula

    def mostrar_caminos():
        inicio = entrada_inicio.get()
        if inicio in grafo:
            distancias = logica["dijkastra"](grafo, inicio)
            if distancias:
                resultado = "\n".join([f"{ciudad}: {distancia}" for ciudad, distancia in distancias.items()])
                messagebox.showinfo("Camino más corto:", resultado)
            else:
                messagebox.showerror("Error", "No se encontraron caminos.")
        else:
            messagebox.showerror("Error", "Ciudad de inicio no válida")
    
    def mostrar_arbol():
        mst = logica["kruskal"](aristas, nodos)
        resultado = "\n".join([f"{u} --- {v} [Peso: {peso}]" for u, v, peso in mst])
        messagebox.showinfo("Árbol de Expansión Mínima:", resultado)
    
    tk.Label(ventana, text="Planificación de Rutas").pack(pady=10)
    tk.Label(ventana, text="Ciudad de inicio:").pack(pady=5)
    entrada_inicio = tk.Entry(ventana)
    entrada_inicio.pack(pady=5)
    tk.Button(ventana, text="Mostrar camino más corto", command=mostrar_caminos).pack(pady=10)
    tk.Button(ventana, text="Mostrar árbol de expansión mínima", command=mostrar_arbol).pack(pady=10)
    ventana.mainloop()