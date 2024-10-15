Algoritmo Senso_población
	Repetir
        Escribir "Ingrese la cantidad de personas:"
        Leer N
    Hasta Que N >= 1 Y N <= 100000 
	
    Dimension nacimientos[N], fallecimientos[N]
	
    Para i <- 1 Hasta N Con Paso 1 Hacer
        Repetir
            Escribir "Ingrese el año de nacimiento de la persona ", i
            Leer nacimientos[i]
        Hasta Que nacimientos[i] >= 1 Y nacimientos[i] <= 1000000000
        
        Repetir
            Escribir "Ingrese el año de fallecimiento de la persona ", i
            Leer fallecimientos[i]
        Hasta Que fallecimientos[i] >= nacimientos[i] Y fallecimientos[i] <= 1000000000 
    FinPara
	Escribir "Ingrese el año que desea consultar:"
    Leer añoConsulta
	
    contadorVivos <- 0
    edadMasJoven <- 10000
    edadMasAnciano <- -1
	
    Para j <- 1 Hasta N Con Paso 1 Hacer
        Si añoConsulta >= nacimientos[j] Y añoConsulta <= fallecimientos[j] Entonces
            contadorVivos <- contadorVivos + 1
            edad <- añoConsulta - nacimientos[j]
			
            Si edad < edadMasJoven Entonces
                edadMasJoven <- edad
            FinSi
			
            Si edad > edadMasAnciano Entonces
                edadMasAnciano <- edad
            FinSi
        FinSi
    FinPara
	
    Si contadorVivos > 0 Entonces
        Escribir "En el año ", añoConsulta, ":"
        Escribir "Cantidad de personas vivas: ", contadorVivos
        Escribir "Edad de la persona más joven: ", edadMasJoven
        Escribir "Edad de la persona más anciana: ", edadMasAnciano
    SiNo
        Escribir "No hay personas vivas en el año ", añoConsulta
    FinSi
FinAlgoritmo

