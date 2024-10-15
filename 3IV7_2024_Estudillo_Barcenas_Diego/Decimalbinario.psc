Algoritmo Decimalbinario
	Definir n Como Entero
	Definir binario Como Texto
	n = 0
	binario = ""
	Escribir "Ingresa el numero decimal"
	Leer n
	
	Si n >= 0 Entonces
		Mientras n > 0 Hacer
			residuo = n%2
			nuevobinario = ConvertirATexto(residuo)
			binario = nuevobinario + binario
			
			n = Trunc(n/2)
		Fin Mientras
		Si binario = "" Entonces
			binario = "0"
		Fin Si
	Fin Si
	Escribir "El numero binario es :", binario
FinAlgoritmo
