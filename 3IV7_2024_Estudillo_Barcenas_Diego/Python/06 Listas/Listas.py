#derivado a que es necesario poder almacenar diferentes fuentes de datos
#en python se utiliza la variable diccionario
#un diccionario es capaz de poder almacenar diferentes tipos de dato en formato de lista
import tkinter as tk
from tkinter import messagebox, simpledialog

#para poder guardar los datos correspondientes de la lista es necesario utilizar un archivo, para ello vamos a ocupar la libreria os
import os

#vamos a declarar un archivo, tenemos dos opciones una ruta dinamica o una ruta estatica, eso queda de tarea 
ARCHIVO = "alumnos.txt"

#el examen debe de tener almenos 8 elementos de la lista que deseen guardar el examen debe de posee elementos de dialogo y mensajes de salida con tkinter, la lista debe de implementar al menos 30 diferentes elementos y debe verse una interfaz mediante la cual los imprima en formato de lista

#primero vamos a crear una lista de alumnos
alumnos = [
    {"nombre": "ajo", "nombre_cientifico": "Allium sativum", "color": "blanco", "maduracion": "6 meses", "familia": "Amaryllidaceae", "nutrientes": "vitamina C", "pais": "China", "toneladas": "200000"},
    {"nombre": "apio", "nombre_cientifico": "Apium graveolens", "color": "verde", "maduracion": "5 meses", "familia": "Apiaceae", "nutrientes": "vitamina K", "pais": "España", "toneladas": "150000"},
    {"nombre": "acelga", "nombre_cientifico": "Beta vulgaris", "color": "verde", "maduracion": "2 meses", "familia": "Amaranthaceae", "nutrientes": "vitamina A", "pais": "Suiza", "toneladas": "50000"},
    {"nombre": "berenjena", "nombre_cientifico": "Solanum melongena", "color": "morado", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "fibra", "pais": "India", "toneladas": "120000"},
    {"nombre": "betabel", "nombre_cientifico": "Beta vulgaris", "color": "rojo", "maduracion": "4 meses", "familia": "Amaranthaceae", "nutrientes": "hierro", "pais": "Rusia", "toneladas": "80000"},
    {"nombre": "brócoli", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C", "pais": "China", "toneladas": "100000"},
    {"nombre": "calabaza", "nombre_cientifico": "Cucurbita pepo", "color": "naranja", "maduracion": "4 meses", "familia": "Cucurbitaceae", "nutrientes": "vitamina A", "pais": "México", "toneladas": "130000"},
    {"nombre": "cebolla", "nombre_cientifico": "Allium cepa", "color": "blanco", "maduracion": "6 meses", "familia": "Amaryllidaceae", "nutrientes": "fibra", "pais": "Estados Unidos", "toneladas": "180000"},
    {"nombre": "champiñón", "nombre_cientifico": "Agaricus bisporus", "color": "blanco", "maduracion": "1 mes", "familia": "Agaricaceae", "nutrientes": "proteína", "pais": "Francia", "toneladas": "30000"},
    {"nombre": "chícharo", "nombre_cientifico": "Pisum sativum", "color": "verde", "maduracion": "3 meses", "familia": "Fabaceae", "nutrientes": "proteína", "pais": "India", "toneladas": "70000"},
    {"nombre": "col", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C", "pais": "Rusia", "toneladas": "110000"},
    {"nombre": "camote", "nombre_cientifico": "Ipomoea batatas", "color": "naranja", "maduracion": "4 meses", "familia": "Convolvulaceae", "nutrientes": "carbohidratos", "pais": "Estados Unidos", "toneladas": "160000"},
    {"nombre": "coliflor", "nombre_cientifico": "Brassica oleracea", "color": "blanco", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra", "pais": "Italia", "toneladas": "90000"},
    {"nombre": "espárrago", "nombre_cientifico": "Asparagus officinalis", "color": "verde", "maduracion": "2 años", "familia": "Asparagaceae", "nutrientes": "fibra", "pais": "Perú", "toneladas": "45000"},
    {"nombre": "espinaca", "nombre_cientifico": "Spinacia oleracea", "color": "verde", "maduracion": "1 mes", "familia": "Amaranthaceae", "nutrientes": "hierro", "pais": "China", "toneladas": "50000"},
    {"nombre": "habichuela", "nombre_cientifico": "Phaseolus vulgaris", "color": "verde", "maduracion": "3 meses", "familia": "Fabaceae", "nutrientes": "proteína", "pais": "México", "toneladas": "75000"},
    {"nombre": "jitomate", "nombre_cientifico": "Solanum lycopersicum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C", "pais": "México", "toneladas": "250000"},
    {"nombre": "lechuga", "nombre_cientifico": "Lactuca sativa", "color": "verde", "maduracion": "2 meses", "familia": "Asteraceae", "nutrientes": "fibra", "pais": "España", "toneladas": "60000"},
    {"nombre": "elote", "nombre_cientifico": "Zea mays", "color": "amarillo", "maduracion": "3 meses", "familia": "Poaceae", "nutrientes": "carbohidratos", "pais": "Estados Unidos", "toneladas": "200000"},
    {"nombre": "papa", "nombre_cientifico": "Solanum tuberosum", "color": "café", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "carbohidratos", "pais": "Perú", "toneladas": "300000"},
    {"nombre": "pepino", "nombre_cientifico": "Cucumis sativus", "color": "verde", "maduracion": "2 meses", "familia": "Cucurbitaceae", "nutrientes": "agua", "pais": "China", "toneladas": "100000"},
    {"nombre": "pimentón", "nombre_cientifico": "Capsicum annuum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C", "pais": "España", "toneladas": "50000"},
    {"nombre": "rábano", "nombre_cientifico": "Raphanus sativus", "color": "rojo", "maduracion": "1 mes", "familia": "Brassicaceae", "nutrientes": "fibra", "pais": "México", "toneladas": "25000"},
    {"nombre": "remolacha", "nombre_cientifico": "Beta vulgaris", "color": "rojo", "maduracion": "4 meses", "familia": "Amaranthaceae", "nutrientes": "hierro", "pais": "Rusia", "toneladas": "30000"},
    {"nombre": "repollo", "nombre_cientifico": "Brassica oleracea", "color": "verde", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "vitamina C", "pais": "China", "toneladas": "70000"},
    {"nombre": "repollo morado", "nombre_cientifico": "Brassica oleracea", "color": "morado", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra", "pais": "España", "toneladas": "60000"},
    {"nombre": "tomate", "nombre_cientifico": "Solanum lycopersicum", "color": "rojo", "maduracion": "3 meses", "familia": "Solanaceae", "nutrientes": "vitamina C", "pais": "Italia", "toneladas": "150000"},
    {"nombre": "zanahoria", "nombre_cientifico": "Daucus carota", "color": "naranja", "maduracion": "4 meses", "familia": "Apiaceae", "nutrientes": "vitamina A", "pais": "Rusia", "toneladas": "95000"},
    {"nombre": "nabo", "nombre_cientifico": "Brassica rapa", "color": "blanco", "maduracion": "2 meses", "familia": "Brassicaceae", "nutrientes": "fibra", "pais": "Japón", "toneladas": "30000"},
    {"nombre": "nopal", "nombre_cientifico": "Opuntia ficus-indica", "color": "verde", "maduracion": "1 año", "familia": "Cactaceae", "nutrientes": "fibra", "pais": "México", "toneladas": "40000"},
    
]

#vamos a crear una funcion para cargar datos
def cargar_datos():
    #verificar si existe el archivo
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                #que voy a obtener por cada linea
                #es un metodo de cadena que nos ayuda a eliminar espacios al inicio y final de una cadena " habia     "
                partes = linea.strip().split(",")
                if len(partes) >= 6:
                    boleta = partes[0]
                    nombre = partes[1]
                    appat = partes[2]
                    apmat = partes[3]
                    fecnac = partes[4]
                    calificaciones  = list(map(float, partes[5:]))
                    #defino al alumno
                    alumno = {
                        "boleta" : boleta,
                        "nombre" : nombre,
                        "apellido_paterno" : appat,
                        "apellido_materno" : apmat,
                        "fecha_nacimiento" : fecnac,
                        "calificaciones" : calificaciones
                    }
                    alumnos.append(alumno)

#vamos a crear la funcion para guardar los datos
def guardar_datos():
    with open(ARCHIVO, "w") as f:
        for alumno in alumnos:
            f.write(f"{alumno['boleta']},{alumno['nombre']},{alumno['apellido_paterno']},{alumno['apellido_materno']},{alumno['fecha_nacimiento']}, {','.join(map(str,alumno['calificaciones']))}\n")




#vamos a crear una funcion que se encargue de registrar un alumno

def registrar_alumno():
    boleta = simpledialog.askstring("Entrada","Ingresa la boleta del alumno: ") or nombre = simpledialog.askstring("Ingresa el nombre del alumno: ")
    appat = input("Ingresa el apellido paterno del alumno: ")
    apmat = input("Ingresa el apellido materno del alumno: ")
    fecnac = input("Ingresa la fecha de nacimiento(dd/mm/aaaa) del alumno: ")

    calificaciones = []
    #vamos a solicitar 3 calificaciones
    for i in range(1,4):
        calificacionparcial = float(input("Ingrese la calificacion del parcial: "))
        calificaciones.append(calificacionparcial)

    #defino al alumno
    alumno = {
        "boleta" : boleta,
        "nombre" : nombre,
        "apellido_paterno" : appat,
        "apellido_materno" : apmat,
        "fecha_nacimiento" : fecnac,
        "calificaciones" : calificaciones
    }

    alumnos.append(alumno)
    #aqui tengo que mandar a llamar a 
    guardar_datos()
    messagebox.showinfo("Exito", "Alumno registrado exitosamente")

#funcion para poder consultar los datos del arreglo de alumnos(lista)
def consultar_alumnos() :
    if not alumnos :
        print("No hay registros solo juguito contigo")
    else :
        print("Lista de Alumnos: \n")
        for alumno in alumnos :
            print(f"Boleta: {alumno['boleta']}, Nombre: {alumno['nombre']}{alumno['apellido_paterno']}{alumno['apellido_materno']}, Fecha de Nacimiento: {alumno['fecha_nacimiento']}, Calificaciones: {alumno['calificaciones']} \n" )

#funcion para buscar y editar por la boleta
def editar_alumno() :
    boleta = input("Ingrese la boleta del alumnos que desea editar: ")
    for alumno in alumnos :
        if alumno['boleta'] == boleta :
            alumno['nombre'] = input("Ingresa el nuevo nombre o presiona Enter para mantener el actual:") or alumno['nombre']
            alumno['apellido_paterno'] = input("Ingresa el nuevo apellido paterno o presiona Enter para mantener el actual:") or alumno['apellido_paterno']
            alumno['apellido_materno'] = input("Ingresa el nuevo apellido materno o presiona Enter para mantener el actual:") or alumno['apellido_materno']
            alumno['fecha_nacimiento'] = input("Ingresa la nueva fecha de nacimiento o presiona Enter para mantener el actual:") or alumno['fecha_nacimiento']
            #editamos las calificaciones
            for i in range(3) :
                nueva_calificacion = input("Ingresa ela nueva calificacion o presiona Enter para mantener el actual:")
                if nueva_calificacion: 
                    alumno['calificaciones'][i] = float(nueva_calificacion)
    return
    print("No hay mas alumnos")

#eliminar alumno
def eliminar_alumno():
    print("esto es parte del examen")

#vamos a crear un menu
def main() :
    while True:
        print("Menu de Gestión de Proximos Extras")
        print("1.- Registrar Alumno")
        print("2.- Consultar lista de Alumnos")
        print("3.- Editar Alumno")
        print("4.- Eliminar Alumno")
        print("5.- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1" :
            registrar_alumno()
        elif opcion == "2" :
            consultar_alumnos()
        elif opcion == "3" :
            editar_alumno()
        elif opcion == "4" :
            #ahi la crean
            eliminar_alumno()
        elif opcion == "5" :
            print("Ayos")
            break
        else : 
            print("opcion no valida")

main()