Algoritmo Sumadenumeros
	Definir N Como Entero
	Definir Suma Como Entero
	N <- 0
	Suma <- 0
	Escribir "Realiza la suma de N numeros"
	Leer limite
	Para acumulador<-1 Hasta limite Con Paso 1 Hacer
		N <- N + 1
		Suma <- Suma + N
	Fin Para
	Escribir "La suma es : ", Suma
FinAlgoritmo