import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from datetime import datetime

class Producto:
    def __init__(self, nombre, tipo, precio, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.cantidad = cantidad
        self.comprado = False

    def marcar_comprado(self):
        self.comprado = True

class Lista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.ultima_modificacion = "00/00/0000"

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.actualizar_fecha()

    def actualizar_fecha(self):
        self.ultima_modificacion = datetime.now().strftime("%d/%m/%Y")

class SistemaListas:
    def __init__(self):
        self.listas = [
            Lista("Lista 1"),
            Lista("Lista 2"),
            Lista("Lista 3"),
            Lista("Lista 4"),
            Lista("Lista 5"),
            Lista("Lista 6"),
            Lista("Lista 7"),
            Lista("Lista 8"),
        ]

    def crear_lista(self, nombre):
        nueva_lista = Lista(nombre)
        nueva_lista.actualizar_fecha()
        self.listas.append(nueva_lista)

    def obtener_listas_recientes(self):
        return sorted(self.listas, key=lambda x: x.ultima_modificacion, reverse=True)[:8]

    def buscar_lista_por_nombre(self, busqueda):
        return [lista for lista in self.listas if busqueda.lower() in lista.nombre.lower()]

class InterfazSistema:
    def __init__(self, root, sistema):
        self.sistema = sistema
        self.root = root
        self.root.title("Gestión de Listas")

        # Frame principal
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack()

        # Botones principales
        tk.Button(self.main_frame, text="Crear Lista", command=self.abrir_crear_lista).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.main_frame, text="Consultar Listas", command=self.abrir_consultar_listas).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.main_frame, text="Indicaciones", command=self.mostrar_indicaciones).grid(row=0, column=2, padx=5, pady=5)

        # Tabla de listas recientes
        self.tabla_frame = tk.Frame(self.main_frame, pady=10)
        self.tabla_frame.grid(row=1, column=0, columnspan=3)

        self.tabla = ttk.Treeview(self.tabla_frame, columns=("Nombre", "Última Modificación"), show="headings")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Última Modificación", text="Última Modificación")
        self.tabla.pack()

        self.mostrar_listas_recientes()

    def mostrar_listas_recientes(self):
        # Limpiar tabla
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        # Agregar listas recientes
        listas_recientes = self.sistema.obtener_listas_recientes()
        for lista in listas_recientes:
            self.tabla.insert("", "end", values=(lista.nombre, lista.ultima_modificacion))

    def mostrar_listas_en_tabla(self, listas):
        # Limpiar la tabla antes de insertar nuevas filas
        for row in self.tabla_listas.get_children():
            self.tabla_listas.delete(row)

        # Insertar las listas filtradas (o todas si no hay filtro)
        for lista in listas:
            self.tabla_listas.insert("", "end", values=(lista.nombre, lista.ultima_modificacion))

    def abrir_crear_lista(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Crear Lista")
        tk.Label(ventana, text="Nombre de la nueva lista:").pack(pady=10)
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.pack(pady=10)
        
        def crear():
            nombre = entrada_nombre.get().strip()
            if nombre:
                self.sistema.crear_lista(nombre)
                self.mostrar_listas_recientes()
                tk.Label(ventana, text=f"Lista '{nombre}' creada con éxito.").pack(pady=10)

        tk.Button(ventana, text="Crear", command=crear).pack(pady=10)

    def abrir_consultar_listas(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Consultar Listas")

        # Frame para la búsqueda
        frame_busqueda = tk.Frame(ventana, padx=10, pady=10)
        frame_busqueda.pack()

        # Barra de búsqueda
        tk.Label(frame_busqueda, text="Buscar lista por nombre:").grid(row=0, column=0, padx=5, pady=5)
        entrada_busqueda = tk.Entry(frame_busqueda)
        entrada_busqueda.grid(row=0, column=1, padx=5, pady=5)

        # Función de búsqueda
        def buscar_listas():
            busqueda = entrada_busqueda.get().strip().lower()
            listas_encontradas = self.sistema.buscar_lista_por_nombre(busqueda)
            self.mostrar_listas_en_tabla(listas_encontradas)

        # Botón de búsqueda
        tk.Button(frame_busqueda, text="Buscar", command=buscar_listas).grid(row=0, column=2, padx=5, pady=5)

        # Frame para la tabla de listas
        frame_listas = tk.Frame(ventana, padx=10, pady=10)
        frame_listas.pack()

        # Tabla de listas
        self.tabla_listas = ttk.Treeview(frame_listas, columns=("Nombre", "Última Modificación"), show="headings")
        self.tabla_listas.heading("Nombre", text="Nombre")
        self.tabla_listas.heading("Última Modificación", text="Última Modificación")
        self.tabla_listas.pack()

        # Mostrar todas las listas inicialmente
        self.mostrar_listas_en_tabla(self.sistema.listas)

        # Seleccionar una lista para ver los productos
        def seleccionar_lista(event):
            # Obtener la lista seleccionada en la tabla
            seleccion = self.tabla_listas.selection()
            if seleccion:
                item = self.tabla_listas.item(seleccion)
                nombre_lista = item["values"][0]  # Obtener el nombre de la lista
                lista_seleccionada = next((lista for lista in self.sistema.listas if lista.nombre == nombre_lista), None)
                if lista_seleccionada:
                    self.mostrar_productos_de_lista(lista_seleccionada)

        self.tabla_listas.bind("<Double-1>", seleccionar_lista)

    def mostrar_productos_de_lista(self, lista):
        # Crear una nueva ventana para mostrar los productos de la lista seleccionada
        ventana_productos = tk.Toplevel(self.root)
        ventana_productos.title(f"Productos de {lista.nombre}")

        # Crear tabla de productos
        frame_productos = tk.Frame(ventana_productos, padx=10, pady=10)
        frame_productos.pack()

        # Crear tabla
        tabla_productos = ttk.Treeview(frame_productos, columns=("Producto", "Tipo", "Precio", "Cantidad"), show="headings")
        tabla_productos.heading("Producto", text="Producto")
        tabla_productos.heading("Tipo", text="Tipo")
        tabla_productos.heading("Precio", text="Precio")
        tabla_productos.heading("Cantidad", text="Cantidad")
        tabla_productos.pack()

        # Insertar productos de la lista
        for producto in lista.productos:
            tabla_productos.insert("", "end", values=(producto.nombre, producto.tipo, f"${producto.precio:.2f}", producto.cantidad))

        # Botón para agregar un nuevo producto
        def agregar_producto():
            self.abrir_agregar_producto(lista)

        tk.Button(ventana_productos, text="Agregar Producto", command=agregar_producto).pack(pady=10)

    def abrir_agregar_producto(self, lista):
        ventana = tk.Toplevel(self.root)
        ventana.title(f"Agregar Producto a {lista.nombre}")

        # Entradas para los detalles del producto
        tk.Label(ventana, text="Nombre del producto:").pack(pady=5)
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana, text="Tipo de producto:").pack(pady=5)
        entrada_tipo = tk.Entry(ventana)
        entrada_tipo.pack(pady=5)

        tk.Label(ventana, text="Precio del producto:").pack(pady=5)
        entrada_precio = tk.Entry(ventana)
        entrada_precio.pack(pady=5)

        tk.Label(ventana, text="Cantidad del producto:").pack(pady=5)
        entrada_cantidad = tk.Entry(ventana)
        entrada_cantidad.pack(pady=5)

        def agregar_producto():
            nombre = entrada_nombre.get().strip()
            tipo = entrada_tipo.get().strip()
            try:
                precio = float(entrada_precio.get().strip())
                cantidad = int(entrada_cantidad.get().strip())
                if nombre and tipo:
                    producto = Producto(nombre, tipo, precio, cantidad)
                    lista.agregar_producto(producto)
                    messagebox.showinfo("Producto Agregado", f"Producto '{nombre}' agregado a la lista '{lista.nombre}'")
                    ventana.destroy()
                    self.mostrar_productos_de_lista(lista)  # Refrescar la vista de productos
                else:
                    messagebox.showerror("Error", "Por favor, complete todos los campos.")
            except ValueError:
                messagebox.showerror("Error", "Precio y cantidad deben ser números válidos.")

        tk.Button(ventana, text="Agregar Producto", command=agregar_producto).pack(pady=10)

    def mostrar_indicaciones(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Indicaciones")
        indicaciones = (
            "Lorem ipsum dolor sit amet consectetur adipiscing elit elementum luctus, integer habitant laoreet orci dictumst rutrum primis convallis. Quisque etiam potenti sodales ultricies ridiculus vitae orci."
        )
        tk.Label(ventana, text=indicaciones, justify=tk.LEFT).pack(padx=10, pady=10)

if __name__ == "__main__":
    sistema = SistemaListas()
    root = tk.Tk()
    app = InterfazSistema(root, sistema)
    root.mainloop()

