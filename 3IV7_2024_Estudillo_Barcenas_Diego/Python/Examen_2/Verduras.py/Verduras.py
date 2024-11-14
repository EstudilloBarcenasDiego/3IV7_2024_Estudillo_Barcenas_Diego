import tkinter as tk
from tkinter import messagebox, simpledialog 
from tkinter import ttk

import os

ARCHIVO = "verduras.txt"


#lsita preestablecida de verduras
verduras = [
    {"nombre": "ajo", "nombre_cientifico": "Allium sativum", "color": "blanco", "maduracion": "6 meses", "familia": "Amaryllidaceae", "nutrientes": "vitamina C", "pais": "China", "toneladas": "200000"},
    {"nombre": "apio", "nombre_cientifico": "Apium graveolens", "color": "verde", "maduracion": "5 meses", "familia": "Apiaceae", "nutrientes": "fibra, vitamina K", "pais": "Espana", "toneladas": "150000"},
    {"nombre": "acelga", "nombre_cientifico": "Beta vulgaris", "color": "verde", "maduracion": "2 meses", "familia": "Amaranthaceae", "nutrientes": "vitamina A, calcio", "pais": "Suiza", "toneladas": "50000"},
    {"nombre": "berenjena", "nombre_cientifico": "Solanum melongena", "color": "morado", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "fibra, potasio", "pais": "India", "toneladas": "120000"},
    {"nombre": "betabel", "nombre_cientifico": "Beta vulgaris", "color": "rojo", "maduracion": "4 meses", "familia": "Amaranthaceae", "nutrientes": "hierro, acido folico", "pais": "Rusia", "toneladas": "80000"},
    {"nombre": "brocoli", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C, fibra", "pais": "China", "toneladas": "100000"},
    {"nombre": "calabaza", "nombre_cientifico": "Cucurbita pepo", "color": "naranja", "maduracion": "4 meses", "familia": "Cucurbitaceae", "nutrientes": "vitamina A, potasio", "pais": "Mexico", "toneladas": "130000"},
    {"nombre": "cebolla", "nombre_cientifico": "Allium cepa", "color": "blanco", "maduracion": "6 meses", "familia": "Amaryllidaceae", "nutrientes": "fibra, vitamina C", "pais": "Estados Unidos", "toneladas": "180000"},
    {"nombre": "champinon", "nombre_cientifico": "Agaricus bisporus", "color": "blanco", "maduracion": "1 mes", "familia": "Agaricaceae", "nutrientes": "proteina, vitamina B", "pais": "Francia", "toneladas": "30000"},
    {"nombre": "chicharo", "nombre_cientifico": "Pisum sativum", "color": "verde", "maduracion": "3 meses", "familia": "Fabaceae", "nutrientes": "proteina, fibra", "pais": "India", "toneladas": "70000"},
    {"nombre": "col", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C, potasio", "pais": "Rusia", "toneladas": "110000"},
    {"nombre": "camote", "nombre_cientifico": "Ipomoea batatas", "color": "naranja", "maduracion": "4 meses", "familia": "Convolvulaceae", "nutrientes": "carbohidratos, vitamina A", "pais": "Estados Unidos", "toneladas": "160000"},
    {"nombre": "coliflor", "nombre_cientifico": "Brassica oleracea", "color": "blanco", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra, vitamina C", "pais": "Italia", "toneladas": "90000"},
    {"nombre": "esparrago", "nombre_cientifico": "Asparagus officinalis", "color": "verde", "maduracion": "2 anos", "familia": "Asparagaceae", "nutrientes": "fibra, acido folico", "pais": "Peru", "toneladas": "45000"},
    {"nombre": "espinaca", "nombre_cientifico": "Spinacia oleracea", "color": "verde", "maduracion": "1 mes", "familia": "Amaranthaceae", "nutrientes": "hierro, calcio", "pais": "China", "toneladas": "50000"},
    {"nombre": "habichuela", "nombre_cientifico": "Phaseolus vulgaris", "color": "verde", "maduracion": "3 meses", "familia": "Fabaceae", "nutrientes": "proteina, fibra", "pais": "Mexico", "toneladas": "75000"},
    {"nombre": "jitomate", "nombre_cientifico": "Solanum lycopersicum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C, licopeno", "pais": "Mexico", "toneladas": "250000"},
    {"nombre": "lechuga", "nombre_cientifico": "Lactuca sativa", "color": "verde", "maduracion": "2 meses", "familia": "Asteraceae", "nutrientes": "fibra, vitamina A", "pais": "Espana", "toneladas": "60000"},
    {"nombre": "elote", "nombre_cientifico": "Zea mays", "color": "amarillo", "maduracion": "3 meses", "familia": "Poaceae", "nutrientes": "carbohidratos, fibra", "pais": "Estados Unidos", "toneladas": "200000"},
    {"nombre": "papa", "nombre_cientifico": "Solanum tuberosum", "color": "cafe", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "carbohidratos, potasio", "pais": "Peru", "toneladas": "300000"},
    {"nombre": "pepino", "nombre_cientifico": "Cucumis sativus", "color": "verde", "maduracion": "2 meses", "familia": "Cucurbitaceae", "nutrientes": "agua, vitamina K", "pais": "China", "toneladas": "100000"},
    {"nombre": "pimenton", "nombre_cientifico": "Capsicum annuum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C, fibra", "pais": "Espana", "toneladas": "50000"},
    {"nombre": "rabano", "nombre_cientifico": "Raphanus sativus", "color": "rojo", "maduracion": "1 mes", "familia": "Brassicaceae", "nutrientes": "fibra, vitamina C", "pais": "Mexico", "toneladas": "25000"},
    {"nombre": "remolacha", "nombre_cientifico": "Beta vulgaris", "color": "rojo", "maduracion": "4 meses", "familia": "Amaranthaceae", "nutrientes": "hierro, potasio", "pais": "Rusia", "toneladas": "30000"},
    {"nombre": "repollo", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C, fibra", "pais": "China", "toneladas": "70000"},
    {"nombre": "repollo morado", "nombre_cientifico": "Brassica oleracea", "color": "morado", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra, vitamina C", "pais": "Espana", "toneladas": "60000"},
    {"nombre": "tomate", "nombre_cientifico": "Solanum lycopersicum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C, potasio", "pais": "Italia", "toneladas": "150000"},
    {"nombre": "zanahoria", "nombre_cientifico": "Daucus carota", "color": "naranja", "maduracion": "4 meses", "familia": "Apiaceae", "nutrientes": "vitamina A, fibra", "pais": "Rusia", "toneladas": "95000"},
    {"nombre": "nabo", "nombre_cientifico": "Brassica rapa", "color": "blanco", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra, calcio", "pais": "Japon", "toneladas": "30000"},
    {"nombre": "nopal", "nombre_cientifico": "Opuntia ficus-indica", "color": "verde", "maduracion": "1 ano", "familia": "Cactaceae", "nutrientes": "fibra, vitamina C", "pais": "Mexico", "toneladas": "40000"},
]


#funcion para cargar datos
def cargar_verdura():
    verduras.clear()  
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                partes = linea.strip().split(",")
                if len(partes) >= 8:
                    nombre = partes[0]
                    nombre_c = partes[1]
                    color = partes[2]
                    maduracion = partes[3]
                    familia = partes[4]
                    nutriente = partes[5]
                    pais = partes[6]
                    toneladas = partes[7]
                    n_verdura = {
                        "nombre": nombre,
                        "nombre_cientifico": nombre_c,
                        "color": color,
                        "maduracion": maduracion,
                        "familia": familia,
                        "nutrientes": nutriente,
                        "pais": pais,
                        "toneladas": toneladas,
                    }
                    verduras.append(n_verdura)

#funcion para guardar los datos
def guardar_verdura():
    with open(ARCHIVO, "w") as f:
        for n_verdura in verduras:
            f.write(f"{n_verdura['nombre']},{n_verdura['nombre_cientifico']},{n_verdura['color']},{n_verdura['maduracion']},{n_verdura['familia']},{n_verdura['nutrientes']},{n_verdura['pais']},{n_verdura['toneladas']}\n")

#funcion que se encargue de registrar 

def registrar_verdura():
    nombre = simpledialog.askstring("Registro", "Ingresa el nombre de la verdura:")
    nombre_c = simpledialog.askstring("Registro", "Ingresa el nombre científico de la verdura:")
    color = simpledialog.askstring("Registro", "Ingresa el color de la verdura:")
    maduracion = simpledialog.askstring("Registro", "Ingresa el tiempo de maduración de la verdura:")
    familia = simpledialog.askstring("Registro", "Ingresa la familia a la que pertenece la verdura:")
    nutrientes = simpledialog.askstring("Registro", "Ingresa los nutrientes que aporta la verdura:")
    pais = simpledialog.askstring("Registro", "Ingresa el país que más cultiva la verdura:")
    toneladas = simpledialog.askstring("Registro", "Ingresa las toneladas producidas al año (aproximadamente):")

    # Defino la verdura
    n_verdura = {
        "nombre": nombre,
        "nombre_cientifico": nombre_c,
        "color": color,
        "maduracion": maduracion,
        "familia": familia,
        "nutrientes": nutrientes,
        "pais": pais,
        "toneladas": toneladas,
    }

    verduras.append(n_verdura)
        
    #mando a llamar a 
    guardar_verdura()
    messagebox.showinfo("Registro", "Verdura registrada exitosamente")

#funcion para poder consultar los datos del arreglo de alumnos(lista)
def consultar_verdura():
    ventana_consulta = tk.Toplevel(root)
    ventana_consulta.title("Consulta de Verduras")
    ventana_consulta.geometry("1000x600")
    ventana_consulta.configure(bg="lightgreen") 

    columns = ("Nombre", "Nombre Científico", "Color", "Maduración", "Familia", "Nutrientes", "País", "Toneladas")
    treeview_verduras = ttk.Treeview(ventana_consulta, columns=columns, show="headings", height=15)
    style = ttk.Style()
    style.configure("Treeview", background="lightcyan")
    scrollbar = ttk.Scrollbar(ventana_consulta, orient="vertical", command=treeview_verduras.yview)
    treeview_verduras.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    for col in columns:
        treeview_verduras.heading(col, text=col)
        treeview_verduras.column(col, width=120)

    treeview_verduras.pack(pady=20)

    treeview_verduras.delete(*treeview_verduras.get_children())

    if not verduras:
        messagebox.showwarning("No hay registros de verduras.")
        ventana_consulta.destroy()
    else:
        for n_verdura in verduras:
            treeview_verduras.insert("", tk.END, values=(
                n_verdura["nombre"],
                n_verdura["nombre_cientifico"],
                n_verdura["color"],
                n_verdura["maduracion"],
                n_verdura["familia"],
                n_verdura["nutrientes"],
                n_verdura["pais"],
                n_verdura["toneladas"]
            ))

#funcion para buscar y editar por el nombre 
def editar_verdura():
    nombre = simpledialog.askstring("Editar", "Ingresa el nombre de la verdura que deseas editar:")
    for n_verdura in verduras:
        if n_verdura['nombre'] == nombre:
            n_verdura['nombre_cientifico'] = simpledialog.askstring("Editar", "Nuevo nombre científico:", initialvalue=n_verdura['nombre_cientifico']) or n_verdura['nombre_cientifico']
            n_verdura['color'] = simpledialog.askstring("Editar", "Nuevo color:", initialvalue=n_verdura['color']) or n_verdura['color']
            n_verdura['maduracion'] = simpledialog.askstring("Editar", "Nuevo tiempo de maduración:", initialvalue=n_verdura['maduracion']) or n_verdura['maduracion']
            n_verdura['familia'] = simpledialog.askstring("Editar", "Nueva familia:", initialvalue=n_verdura['familia']) or n_verdura['familia']
            n_verdura['nutrientes'] = simpledialog.askstring("Editar", "Nuevos nutrientes:", initialvalue=n_verdura['nutrientes']) or n_verdura['nutrientes']
            n_verdura['pais'] = simpledialog.askstring("Editar", "Nuevo país:", initialvalue=n_verdura['pais']) or n_verdura['pais']
            n_verdura['toneladas'] = simpledialog.askstring("Editar", "Nueva cantidad de toneladas:", initialvalue=n_verdura['toneladas']) or n_verdura['toneladas']
            guardar_verdura()
            messagebox.showinfo("Editar", "Verdura editada exitosamente.")
            return
    messagebox.showwarning("Advertencia", "No se encontró la verdura especificada.")

# funcion pora eliminar verdura
def eliminar_verdura():
    nombre = simpledialog.askstring("Eliminar", "Ingresa el nombre de la verdura que deseas eliminar:")
    for i, n_verdura in enumerate(verduras):
        if n_verdura['nombre'] == nombre:
            del verduras[i]
            guardar_verdura()
            messagebox.showinfo("Eliminar", "Verdura eliminada exitosamente.")
            return
    messagebox.showwarning("Advertencia", "No se encontró la verdura especificada.")

#funcion para el menu
def menu():
    global root
    root = tk.Tk()
    root.title("Gestión de Verduras")
    root.geometry("1000x600")  
    root.configure(bg="lightgreen")
    
    cargar_verdura()

    # titulo
    title_label = tk.Label(root, text="Gestión de Verduras", font=("Arial", 24), bg="lightgreen")
    title_label.pack(pady=20)

    # botones
    boton_config = {"width": 30, "bg": "#b2f2b2"}
    tk.Button(root, text="Registrar Verdura", command=registrar_verdura, **boton_config).pack(pady=5)
    tk.Button(root, text="Consultar Verduras", command=consultar_verdura, **boton_config).pack(pady=5)
    tk.Button(root, text="Editar Verdura", command=editar_verdura, **boton_config).pack(pady=5)
    tk.Button(root, text="Eliminar Verdura", command=eliminar_verdura, **boton_config).pack(pady=5)
    tk.Button(root, text="Salir", command=salir, **boton_config).pack(pady=20)
    # ejecutaa la interfaz
    root.mainloop()

#funcion para salir del menu
def salir():
    messagebox.showinfo("Salida", "Hasta la próxima :3")
    root.destroy()


menu()