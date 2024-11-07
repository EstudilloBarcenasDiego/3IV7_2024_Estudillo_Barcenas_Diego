import tkinter as tk
from tkinter import messagebox, simpledialog 
from tkinter import ttk

import os

ARCHIVO = "verduras.txt"


#lsita preestablecida de verduras
verduras = [
    {"nombre": "ajo", "nombre_cientifico": "Allium sativum", "color": "blanco", "maduracion": "6 meses", "familia": "Amaryllidaceae", "nutrientes": "vitamina C, manganeso", "pais": "China", "toneladas": "200000"},
    {"nombre": "apio", "nombre_cientifico": "Apium graveolens", "color": "verde", "maduracion": "5 meses", "familia": "Apiaceae", "nutrientes": "fibra, vitamina K", "pais": "España", "toneladas": "150000"},
    {"nombre": "acelga", "nombre_cientifico": "Beta vulgaris", "color": "verde", "maduracion": "2 meses", "familia": "Amaranthaceae", "nutrientes": "vitamina A, calcio", "pais": "Suiza", "toneladas": "50000"},
    {"nombre": "berenjena", "nombre_cientifico": "Solanum melongena", "color": "morado", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "fibra, potasio", "pais": "India", "toneladas": "120000"},
    {"nombre": "betabel", "nombre_cientifico": "Beta vulgaris", "color": "rojo", "maduracion": "4 meses", "familia": "Amaranthaceae", "nutrientes": "hierro, ácido fólico", "pais": "Rusia", "toneladas": "80000"},
    {"nombre": "brócoli", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C, fibra", "pais": "China", "toneladas": "100000"},
    {"nombre": "calabaza", "nombre_cientifico": "Cucurbita pepo", "color": "naranja", "maduracion": "4 meses", "familia": "Cucurbitaceae", "nutrientes": "vitamina A, potasio", "pais": "México", "toneladas": "130000"},
    {"nombre": "cebolla", "nombre_cientifico": "Allium cepa", "color": "blanco", "maduracion": "6 meses", "familia": "Amaryllidaceae", "nutrientes": "fibra, vitamina C", "pais": "Estados Unidos", "toneladas": "180000"},
    {"nombre": "champiñón", "nombre_cientifico": "Agaricus bisporus", "color": "blanco", "maduracion": "1 mes", "familia": "Agaricaceae", "nutrientes": "proteína, vitamina B", "pais": "Francia", "toneladas": "30000"},
    {"nombre": "chícharo", "nombre_cientifico": "Pisum sativum", "color": "verde", "maduracion": "3 meses", "familia": "Fabaceae", "nutrientes": "proteína, fibra", "pais": "India", "toneladas": "70000"},
    {"nombre": "col", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C, potasio", "pais": "Rusia", "toneladas": "110000"},
    {"nombre": "camote", "nombre_cientifico": "Ipomoea batatas", "color": "naranja", "maduracion": "4 meses", "familia": "Convolvulaceae", "nutrientes": "carbohidratos, vitamina A", "pais": "Estados Unidos", "toneladas": "160000"},
    {"nombre": "coliflor", "nombre_cientifico": "Brassica oleracea", "color": "blanco", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra, vitamina C", "pais": "Italia", "toneladas": "90000"},
    {"nombre": "espárrago", "nombre_cientifico": "Asparagus officinalis", "color": "verde", "maduracion": "2 años", "familia": "Asparagaceae", "nutrientes": "fibra, ácido fólico", "pais": "Perú", "toneladas": "45000"},
    {"nombre": "espinaca", "nombre_cientifico": "Spinacia oleracea", "color": "verde", "maduracion": "1 mes", "familia": "Amaranthaceae", "nutrientes": "hierro, calcio", "pais": "China", "toneladas": "50000"},
    {"nombre": "habichuela", "nombre_cientifico": "Phaseolus vulgaris", "color": "verde", "maduracion": "3 meses", "familia": "Fabaceae", "nutrientes": "proteína, fibra", "pais": "México", "toneladas": "75000"},
    {"nombre": "jitomate", "nombre_cientifico": "Solanum lycopersicum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C, licopeno", "pais": "México", "toneladas": "250000"},
    {"nombre": "lechuga", "nombre_cientifico": "Lactuca sativa", "color": "verde", "maduracion": "2 meses", "familia": "Asteraceae", "nutrientes": "fibra, vitamina A", "pais": "España", "toneladas": "60000"},
    {"nombre": "elote", "nombre_cientifico": "Zea mays", "color": "amarillo", "maduracion": "3 meses", "familia": "Poaceae", "nutrientes": "carbohidratos, fibra", "pais": "Estados Unidos", "toneladas": "200000"},
    {"nombre": "papa", "nombre_cientifico": "Solanum tuberosum", "color": "café", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "carbohidratos, potasio", "pais": "Perú", "toneladas": "300000"},
    {"nombre": "pepino", "nombre_cientifico": "Cucumis sativus", "color": "verde", "maduracion": "2 meses", "familia": "Cucurbitaceae", "nutrientes": "agua, vitamina K", "pais": "China", "toneladas": "100000"},
    {"nombre": "pimentón", "nombre_cientifico": "Capsicum annuum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C, fibra", "pais": "España", "toneladas": "50000"},
    {"nombre": "rábano", "nombre_cientifico": "Raphanus sativus", "color": "rojo", "maduracion": "1 mes", "familia": "Brassicaceae", "nutrientes": "fibra, vitamina C", "pais": "México", "toneladas": "25000"},
    {"nombre": "remolacha", "nombre_cientifico": "Beta vulgaris", "color": "rojo", "maduracion": "4 meses", "familia": "Amaranthaceae", "nutrientes": "hierro, potasio", "pais": "Rusia", "toneladas": "30000"},
    {"nombre": "repollo", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C, fibra", "pais": "China", "toneladas": "70000"},
    {"nombre": "repollo morado", "nombre_cientifico": "Brassica oleracea", "color": "morado", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra, vitamina C", "pais": "España", "toneladas": "60000"},
    {"nombre": "tomate", "nombre_cientifico": "Solanum lycopersicum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C, potasio", "pais": "Italia", "toneladas": "150000"},
    {"nombre": "zanahoria", "nombre_cientifico": "Daucus carota", "color": "naranja", "maduracion": "4 meses", "familia": "Apiaceae", "nutrientes": "vitamina A, fibra", "pais": "Rusia", "toneladas": "95000"},
    {"nombre": "nabo", "nombre_cientifico": "Brassica rapa", "color": "blanco", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra, calcio", "pais": "Japón", "toneladas": "30000"},
    {"nombre": "nopal", "nombre_cientifico": "Opuntia ficus-indica", "color": "verde", "maduracion": "1 año", "familia": "Cactaceae", "nutrientes": "fibra, vitamina C", "pais": "México", "toneladas": "40000"},
]


#funcion para cargar datos
def cargar_verdura():
    verduras.clear()  # Limpia la lista para evitar duplicados
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
    nombre = simpledialog.askstring("Ingresa el nombre de la verdura:")
    nombre_c = simpledialog.askstring("Ingresa el nombre cientifico de la verdura:")
    color = simpledialog.askstring("Ingresa el color de la verdura:")
    maduracion = simpledialog.askstring("Ingresa el tiempo de maduración (meses, años) de la verdura:")
    familia = simpledialog.askstring("Ingresa la familia a la que pertenece la verdura:")
    nutrientes = simpledialog.askstring("Ingresa los nutrientes que aporta la verdura:")
    pais = simpledialog.askstring("Ingresa el pais que más cultiva la verdura:")
    toneladas = simpledialog.askstring("Ingresa las toneladas producidas al año (aproximadamente):")

    #defino la verdura
    n_verdura = {
        "nombre" : nombre,
        "nombre_cientifico" : nombre_c,
        "color" : color,
        "maduracion" : maduracion,
        "familia" : familia,
        "nutrientes" : nutrientes,
        "pais" : pais,
        "toneladas" : toneladas,
    }

    verduras.append(n_verdura)
    
    #mando a llamar a 
    guardar_verdura()
    messagebox.showinfo("Verdura registrada exitosamente")

#funcion para poder consultar los datos del arreglo de alumnos(lista)
def consultar_verdura():
    ventana_consulta = tk.Toplevel(root)
    ventana_consulta.title("Consulta de Verduras")
    ventana_consulta.geometry("1000x600") 

    columns = ("Nombre", "Nombre Científico", "Color", "Maduración", "Familia", "Nutrientes", "País", "Toneladas")
    treeview_verduras = ttk.Treeview(ventana_consulta, columns=columns, show="headings", height=15)

    for col in columns:
        treeview_verduras.heading(col, text=col)
        treeview_verduras.column(col, width=120)

    treeview_verduras.pack(pady=20)

    treeview_verduras.delete(*treeview_verduras.get_children())

    if not verduras:
        messagebox.showwarning("No hay registros de verduras.")
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
    nombre = simpledialog.askstring("Ingresa el nombre de la verdura que deseas editar:")
    for n_verdura in verduras:
        if n_verdura['nombre'] == nombre:
            n_verdura['nombre_cientifico'] = simpledialog.askstring(f"Ingrese el nuevo nombre cientifico (o presione Enter para mantener '{n_verdura['nombre_cientifico']}'):", initialvalue=n_verdura['nombre_cientifico']) or n_verdura['nombre_cientifico']
            n_verdura['color'] = simpledialog.askstring(f"Ingrese el nuevo color (o presione Enter para mantener '{n_verdura['color']}'):", initialvalue=n_verdura['color']) or n_verdura['color']
            n_verdura['maduracion'] = simpledialog.askstring(f"Ingrese el nuevo tiempo de maduración (o presione Enter para mantener '{n_verdura['maduracion']}'):", initialvalue=n_verdura['maduracion']) or n_verdura['maduracion']
            n_verdura['familia'] = simpledialog.askstring(f"Ingrese la nueva familia (o presione Enter para mantener '{n_verdura['familia']}'):", initialvalue=n_verdura['familia']) or n_verdura['familia']
            n_verdura['nutrientes'] = simpledialog.askstring(f"Ingrese los nuevos nutrientes (o presione Enter para mantener '{n_verdura['nutrientes']}'):", initialvalue=n_verdura['nutrientes']) or n_verdura['nutrientes']
            n_verdura['pais'] = simpledialog.askstring(f"Ingrese el nuevo país (o presione Enter para mantener '{n_verdura['pais']}'):", initialvalue=n_verdura['pais']) or n_verdura['pais']
            n_verdura['toneladas'] = simpledialog.askstring(f"Ingrese la nueva cantidad de toneladas (o presione Enter para mantener '{n_verdura['toneladas']}'):", initialvalue=n_verdura['toneladas']) or n_verdura['toneladas']
            guardar_verdura()
            messagebox.showinfo("Verdura editada exitosamente.")
            return
    messagebox.showwarning("No se encontró la verdura especificada.")

# funcion pora eliminar verdura
def eliminar_verdura():
    nombre = simpledialog.askstring("Ingrese el nombre de la verdura que desea eliminar:")
    for i, n_verdura in enumerate(verduras):
        if n_verdura['nombre'] == nombre:
            del verduras[i]
            guardar_verdura()
            messagebox.showinfo("Verdura eliminada exitosamente.")
            return
    messagebox.showwarning("No se encontró la verdura especificada.")

#funcion para el menu
def menu():
    global root
    root = tk.Tk()
    root.title("Gestión de Verduras")
    root.geometry("1000x600")  
    
    cargar_verdura()

    # titulo
    title_label = tk.Label(root, text="Gestión de Verduras", font=("Arial", 24))
    title_label.pack(pady=20)

    # botones
    tk.Button(root, text="Registrar Verdura", command=registrar_verdura, width=30).pack(pady=5)
    tk.Button(root, text="Consultar Verduras", command=consultar_verdura, width=30).pack(pady=5)
    tk.Button(root, text="Editar Verdura", command=editar_verdura, width=30).pack(pady=5)
    tk.Button(root, text="Eliminar Verdura", command=eliminar_verdura, width=30).pack(pady=5)
    tk.Button(root, text="Salir", command=salir, width=30).pack(pady=20)

    # ejecutaa la interfaz
    root.mainloop()

#funcion para salir del menu
def salir():
    messagebox.showinfo("Salida", "Hasta la próxima :3")
    root.destroy()


menu()