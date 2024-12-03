import random
import tkinter as tk
from tkinter import messagebox
import math

class RuletaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruleta Personalizada")
        self.valores = []
        self.colores = [
            "lightblue", "lightgreen", "lightcoral", "gold", "mediumpurple", 
            "lightsalmon", "lightpink", "lightseagreen", "khaki", "cornflowerblue"
        ]
        self.rueda_angulo = 0  # Ángulo inicial de la ruleta

        # Sección para agregar valores
        self.instruccion = tk.Label(root, text="Ingresa los valores para la ruleta:")
        self.instruccion.pack(pady=5)

        self.entrada = tk.Entry(root, width=30)
        self.entrada.pack(pady=5)

        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_valor)
        self.boton_agregar.pack(pady=5)

        self.lista_valores = tk.Listbox(root, width=30, height=10, selectmode=tk.SINGLE)
        self.lista_valores.pack(pady=5)

        # Botón para borrar valores
        self.boton_borrar = tk.Button(root, text="Borrar Seleccionado", command=self.borrar_valor)
        self.boton_borrar.pack(pady=5)

        self.boton_limpiar = tk.Button(root, text="Limpiar Todo", command=self.limpiar_todo)
        self.boton_limpiar.pack(pady=5)

        # Botón para girar la ruleta
        self.boton_girar = tk.Button(root, text="¡Girar Ruleta!", command=self.girar_ruleta)
        self.boton_girar.pack(pady=10)

        # Canvas para dibujar la ruleta
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)

        self.centro_x, self.centro_y = 200, 200  # Centro de la ruleta
        self.radio = 150  # Radio de la ruleta

    def agregar_valor(self):
        valor = self.entrada.get().strip()
        if valor:
            self.valores.append(valor)
            self.lista_valores.insert(tk.END, valor)
            self.entrada.delete(0, tk.END)
            self.dibujar_ruleta()
        else:
            messagebox.showwarning("Advertencia", "El campo no puede estar vacío.")

    def borrar_valor(self):
        seleccionado = self.lista_valores.curselection()
        if seleccionado:
            indice = seleccionado[0]
            del self.valores[indice]
            self.lista_valores.delete(indice)
            self.dibujar_ruleta()
        else:
            messagebox.showwarning("Advertencia", "Selecciona un valor para borrar.")

    def limpiar_todo(self):
        self.valores.clear()
        self.lista_valores.delete(0, tk.END)
        self.canvas.delete("all")  # Limpiar el Canvas

    def dibujar_ruleta(self):
        """Dibuja la ruleta en el Canvas."""
        self.canvas.delete("all")  # Limpiar el Canvas
        if not self.valores:
            return
        
        num_valores = len(self.valores)
        angulo_porcion = 360 / num_valores

        for i, valor in enumerate(self.valores):
            start_angle = i * angulo_porcion
            end_angle = start_angle + angulo_porcion

            # Seleccionar un color único de la lista de colores
            color = self.colores[i % len(self.colores)]

            # Dibujar la sección de la ruleta
            self.canvas.create_arc(
                self.centro_x - self.radio, self.centro_y - self.radio,
                self.centro_x + self.radio, self.centro_y + self.radio,
                start=start_angle, extent=angulo_porcion, fill=color, outline="black"
            )

            # Agregar texto al centro de cada sección
            angulo_texto = math.radians(start_angle + angulo_porcion / 2)
            texto_x = self.centro_x + (self.radio / 2) * math.cos(angulo_texto)
            texto_y = self.centro_y - (self.radio / 2) * math.sin(angulo_texto)

            self.canvas.create_text(
                texto_x, texto_y, text=valor, angle=-start_angle, font=("Arial", 10, "bold")
            )

    def girar_ruleta(self):
        if len(self.valores) < 2:
            messagebox.showerror("Error", "La ruleta necesita al menos 2 valores.")
            return

        def animar_giro(pasos, velocidad):
            if pasos > 0:
                self.rueda_angulo = (self.rueda_angulo + velocidad) % 360
                self.dibujar_ruleta_rotada()
                self.root.after(50, animar_giro, pasos - 1, velocidad)
            else:
                elegido = self.valores[int((self.rueda_angulo / 360) * len(self.valores))]
                messagebox.showinfo("Resultado", f"🎉 ¡La ruleta ha elegido: {elegido}!")

        # Iniciar animación con 50 pasos y velocidad aleatoria
        animar_giro(50, random.randint(15, 25))

    def dibujar_ruleta_rotada(self):
        """Dibuja la ruleta rotada según el ángulo actual."""
        self.canvas.delete("all")
        if not self.valores:
            return

        num_valores = len(self.valores)
        angulo_porcion = 360 / num_valores

        for i, valor in enumerate(self.valores):
            start_angle = (i * angulo_porcion + self.rueda_angulo) % 360
            end_angle = start_angle + angulo_porcion

            # Seleccionar un color único de la lista de colores
            color = self.colores[i % len(self.colores)]

            # Dibujar la sección de la ruleta
            self.canvas.create_arc(
                self.centro_x - self.radio, self.centro_y - self.radio,
                self.centro_x + self.radio, self.centro_y + self.radio,
                start=start_angle, extent=angulo_porcion, fill=color, outline="black"
            )

            # Agregar texto al centro de cada sección
            angulo_texto = math.radians(start_angle + angulo_porcion / 2)
            texto_x = self.centro_x + (self.radio / 2) * math.cos(angulo_texto)
            texto_y = self.centro_y - (self.radio / 2) * math.sin(angulo_texto)

            self.canvas.create_text(
                texto_x, texto_y, text=valor, angle=-start_angle, font=("Arial", 10, "bold")
            )

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = RuletaApp(root)
    root.mainloop()

