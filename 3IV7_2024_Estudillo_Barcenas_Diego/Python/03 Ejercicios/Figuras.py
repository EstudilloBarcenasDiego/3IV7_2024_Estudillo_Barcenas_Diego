import math

#vaamos a crear una funcion para calcular el area y perimetro

def rectangulo(base, altura):
    area = base * altura 
    perimetro = 2*(base+altura)
    return area, perimetro 

def triangulo (base, altura, lado1, lado2, lado3):
    area = (base * altura)/2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro 

def esfera(radio):
    volumen = (4/3)*math.pi*radio**2
    return volumen

def menu():
    print("Hola bienvenido a Pytohn con funciones")
    print("Elije una opcioin")
    print("A.- Area y Perimetro de Rectangulo")
    print("B.- Area y Perimetro de Tringulo")
    print("C.- Volumen de una esfera")

#programa 
menu()
opcion = input("Introduce la opcion a desear : ").upper()
if opcion == "A":
    base= float(input("Introduce la base del rectangulo :"))
    altura= float(input("Introduce la altura del rectangulo :"))
    area, perimetro = rectangulo(base, altura)
    print("El area es de :", area)
    print("El perimetro es de :", perimetro)

elif opcion == "B":
    base= float(input("Introduce la base :"))
    altura= float(input("Introduce la altura :"))
    lado1= float(input("Introduce el lado 1 :"))
    lado2= float(input("Introduce el lado 2 :"))
    lado3= float(input("Introduce el lado 3 :"))
    area, perimetro = triangulo(base, altura, lado1, lado2, lado3)
    print("El area es de :", area)
    print("El perimetro es de :", perimetro)

elif opcion == "C":
    radio= float(input("Introduce la base :"))
    volumen = esfera(radio)
    print("El volumen es de :", volumen)

else: 
    print("Opcion no valida")


#Ejercicio realizar el programa de convertir un numero decimal en binario y un numero binaro en decimal 