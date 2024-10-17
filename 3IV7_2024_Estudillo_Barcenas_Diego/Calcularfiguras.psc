//Vamos a crear un programa para calcular perimetros 
//pero con el uso de subproceso 

//Vamos a crear el SubProceso del Rectangulo
SubProceso Rectangulo(base, altura)
	Definir area, perimetro Como Real
	area <- base * altura
	perimetro <- 2*(base+altura)
	Escribir "El area de un Rectangulo es de :", area
	Escribir "El perimetro de un Rectangulo es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Triangulo
SubProceso Triangulo(base, altura, lado1, lado2, lado3)
	Definir area, perimetro Como Real
	area <- (base * altura)/2
	perimetro <- lado1 + lado2 + lado3
	Escribir "El area de un Triangulo es de :", area
	Escribir "El perimetro de un Triangulo es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Paralelogramo
SubProceso Paralelogramo(base, altura, lado1, lado2)
	Definir area, perimetro Como Real
	area <- (base * altura)
	perimetro <- 2 * (lado1 + lado2)
	Escribir "El area de un Paralelogramo es de :", area
	Escribir "El perimetro de un Paralelogramo es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Trapecio
SubProceso Trapecio(baseM, basem, lado1)
	Definir area, perimetro Como Real
	area <- ((baseM + basem) * lado3) / 2
	perimetro <- baseM + basem + (2 * lado1)
	Escribir "El area de un Trapecio es de :", area
	Escribir "El perimetro de un Trapecio es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Rombo
SubProceso Rombo(diagonalM, diagonalm, lado1)
	area <- (diagonalM * diagonalm)/2
	perimetro <- lado1 * 4
	Escribir "El area de un Rombo es de :", area
	Escribir "El perimetro de un Rombo es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Pentagono 
SubProceso Pentagono(lado1, apotema)
	perimetro <- lado1 * 5
	area <- (perimetro * apotema)/2
	Escribir "El area de un Pentagono es de :", area
	Escribir "El perimetro de un Pentagono es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Hexagono 
SubProceso Hexagono(lado1, apotema)
	perimetro <- lado1 * 6
	area <- (perimetro * apotema)/2
	Escribir "El area de un Hexagono  es de :", area
	Escribir "El perimetro de un Hexagono  es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Heptagono 
SubProceso Heptagono(lado1, apotema)
	perimetro <- lado1 * 7
	area <- (perimetro * apotema)/2
	Escribir "El area de un Heptagono  es de :", area
	Escribir "El perimetro de un Heptagono  es de :", perimetro
FinSubProceso

//Vamos a crear el SubProceso del Octogono 
SubProceso Octogono(lado1, apotema)
	perimetro <- lado1 * 8
	area <- (perimetro * apotema)/2
	Escribir "El area de un Octogono  es de :", area
	Escribir "El perimetro de un Octogono  es de :", perimetro
FinSubProceso

Algoritmo Calcularfiguras
	Definir opcion Como Caracter
	Definir base, altura, lado1, lado2, lado3 Como Real
	//vamos a crear un menu 
	Escribir "Selecciona una opcion"
	Escribir "A.- Area y perimetro del Rectangulo"
	Escribir "B.- Area y perimetro del Triangulo"
	Escribir "C.- Area y perimetro del Paralelogramo"
	Escribir "D.- Area y perimetro del Trapecio"
	Escribir "E.- Area y perimetro del Rombo"
	Escribir "F.- Area y perimetro del Pentagono"
	Escribir "G.- Area y perimetro del Hexagono"
	Escribir "H.- Area y perimetro del Heptagono"
	Escribir "I.- Area y perimetro del Octogono"
	
	Leer opcion
	Segun opcion Hacer
			//para el caso 1
		Caso "A" o "b":
			Escribir "Ingresa la base del Rectanglo"
			Leer  base
			Escribir  "Ingresa la altura del Rectangulo"
			Leer altura
			Rectangulo(base, altura)
			//para el caso 2
		Caso "B" o "b":
			Escribir "Ingresa la base del Rectanglo"
			Leer  base
			Escribir  "Ingresa la altura del Rectangulo"
			Leer altura
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Escribir  "Ingresa el lado 2"
			Leer lado2
			Escribir  "Ingresa el lado 3"
			Leer lado3
			Triangulo(base, altura, lado1, lado2, lado3)
			//para el caso 2
		Caso "C" o "c":
			Escribir "Ingresa la base del Paralelogramo"
			Leer  base
			Escribir  "Ingresa la altura del Paralelogramo"
			Leer altura
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Escribir  "Ingresa el lado 2"
			Leer lado2
			Paralelogramo(base, altura, lado1, lado2)
		Caso "D" o "d":
			Escribir "Ingresa la base Mayor del Trapecio"
			Leer  baseM
			Escribir  "Ingresa la base menor del Trapecio"
			Leer basem
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Paralelogramo(base, altura, lado1, lado2)
		Caso "E" o "e":
			Escribir "Ingresa la diagonal Mayor del Rombo"
			Leer  diagonalM
			Escribir  "Ingresa la diagonal menor del Rombo"
			Leer diagonalm
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Rombo(diagonalM, diagonalm, lado1)
		Caso "F" o "f":
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Escribir  "Ingresa el apotema del Pentagono"
			Leer apotema
			Pentagono(lado1, apotema)
		Caso "G" o "g":
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Escribir  "Ingresa el apotema del Heptagono"
			Leer apotema
			Heptagono(lado1, apotema)
		Caso "H" o "h":
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Escribir  "Ingresa el apotema del Hexagono"
			Leer apotema
			Hexagono(lado1, apotema)
		Caso "I" o "i":
			Escribir "Ingresa el lado 1"
			Leer  lado1
			Escribir  "Ingresa el apotema del Octogono"
			Leer apotema
			Octogono(lado1, apotema)
		De Otro Modo:
			Escribir "Opcion no valida"
	Fin Segun
FinAlgoritmo