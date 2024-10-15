Algoritmo  ConversionTemperatura
    Definir conversion Como Entero
	Definir temperatura, celsius, kelvin, rankine Como Real
	
    Escribir "Ingrese la temperatura en grados Fahrenheit:"
    Leer temperatura
	
    celsius = (temperatura - 32) * 5 / 9
    kelvin = celsius + 273.15
    rankine = temperatura + 459.67
	
    Escribir "Seleccione la conversión a realizar:"
    Escribir "1. Celsius"
    Escribir "2. Kelvin"
    Escribir "3. Rankine"
    Leer conversion
	
    Segun conversion Hacer
        1: Escribir "La temperatura en Celsius es: ", celsius
        2: Escribir "La temperatura en Kelvin es: ", kelvin
        3: Escribir "La temperatura en Rankine es: ", rankine
        De Otro Modo: Escribir "Opción no válida."
    Fin Segun
FinAlgoritmo
