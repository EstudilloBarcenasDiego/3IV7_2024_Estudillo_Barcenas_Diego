Algoritmo ContarNumeros
    Definir cantidad, numero Como Entero
    Definir contadorPositivos, contadorNegativos Como Entero
    contadorPositivos = 0
    contadorNegativos = 0
	
    Escribir "�Cu�ntos n�meros desea ingresar?"
    Leer cantidad
	
    Para i Desde 1 Hasta cantidad Hacer
        Escribir "Ingrese el n�mero ", i, ":"
        Leer numero
		
        Si numero = 0 Entonces
            Escribir "El 0 no se cuenta como positivo ni negativo."
        Sino
            Si numero > 0 Entonces
                contadorPositivos = contadorPositivos + 1
            Sino
                contadorNegativos = contadorNegativos + 1
            Fin Si
        Fin Si
    Fin Para
	
    Escribir "Total de n�meros positivos: ", contadorPositivos
    Escribir "Total de n�meros negativos: ", contadorNegativos
FinAlgoritmo