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

    def mostrar_listas_recientes(self):
        listas_recientes = self.obtener_listas_recientes()
        print("Listas recientes:")
        for lista in listas_recientes:
            print(f"Nombre: {lista.nombre}, Última modificación: {lista.ultima_modificacion}")

    def consultar_listas(self, busqueda):
        listas_encontradas = self.buscar_lista_por_nombre(busqueda)
        if listas_encontradas:
            print("Listas encontradas:")
            for lista in listas_encontradas:
                print(f"Nombre: {lista.nombre}, Última modificación: {lista.ultima_modificacion}")
        else:
            print("No se encontraron listas que coincidan con la búsqueda.")

    def mostrar_productos_de_lista(self, lista):
        if not lista.productos:
            print(f"No hay productos en la lista {lista.nombre}.")
        else:
            print(f"Productos en la lista '{lista.nombre}':")
            for producto in lista.productos:
                print(f"Producto: {producto.nombre}, Tipo: {producto.tipo}, Precio: ${producto.precio:.2f}, Cantidad: {producto.cantidad}")

    def agregar_producto(self, nombre_lista, nombre_producto, tipo, precio, cantidad):
        lista = next((lista for lista in self.listas if lista.nombre == nombre_lista), None)
        if lista:
            producto = Producto(nombre_producto, tipo, precio, cantidad)
            lista.agregar_producto(producto)
            print(f"Producto '{nombre_producto}' agregado a la lista '{nombre_lista}'.")
        else:
            print(f"No se encontró la lista '{nombre_lista}'.")

# Funciones de interacción con el usuario
def menu_principal():
    sistema = SistemaListas()
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear nueva lista")
        print("2. Consultar listas recientes")
        print("3. Buscar lista por nombre")
        print("4. Agregar producto a una lista")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_lista = input("Ingrese el nombre de la nueva lista: ")
            sistema.crear_lista(nombre_lista)
            print(f"Lista '{nombre_lista}' creada con éxito.")
        
        elif opcion == "2":
            sistema.mostrar_listas_recientes()

        elif opcion == "3":
            busqueda = input("Ingrese el nombre de la lista a buscar: ")
            sistema.consultar_listas(busqueda)

        elif opcion == "4":
            nombre_lista = input("Ingrese el nombre de la lista a la que agregar el producto: ")
            nombre_producto = input("Ingrese el nombre del producto: ")
            tipo = input("Ingrese el tipo de producto: ")
            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                sistema.agregar_producto(nombre_lista, nombre_producto, tipo, precio, cantidad)
            except ValueError:
                print("Error: Precio y cantidad deben ser números válidos.")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu_principal()
