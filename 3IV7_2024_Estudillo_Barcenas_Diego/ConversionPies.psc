Algoritmo  ConversionPies
    Definir pies Como Real
    Definir conversion Como Entero
    Definir pulgadas, yardas, cm, metros Como Real
	
    Escribir "Ingrese la medida en pies:"
    Leer pies
	
    pulgadas = pies * 12
    yardas = pies / 3
    cm = pulgadas * 2.54
    metros = cm / 100
	
    Escribir "Seleccione la conversi�n a realizar:"
    Escribir "1. Pulgadas"
    Escribir "2. Yardas"
    Escribir "3. Cent�metros"
    Escribir "4. Metros"
    Leer conversion
	
    Segun conversion Hacer
        1: Escribir "La medida en pulgadas es: ", pulgadas
        2: Escribir "La medida en yardas es: ", yardas
        3: Escribir "La medida en cent�metros es: ", cm
        4: Escribir "La medida en metros es: ", metros
        De Otro Modo: Escribir "Opci�n no v�lida."
    Fin Segun
FinAlgoritmo

