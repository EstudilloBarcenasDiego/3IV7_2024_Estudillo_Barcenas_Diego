Algoritmo Cobro_Estacionamiento
	Definir horaentrada, minutoentrada, horasalida, minutosalida Como real
	Definir totalHoras, totalMinutos, minutosrestantes, fracciones15min, totalSegundos Como real
	Definir totalcobro Como real
	
	// Entrada de datos
	Escribir "Ingrese la hora de entrada (formato de 24 horas)"
	Leer horaentrada
	Escribir "Ingrese los minutos de entrada (formato de 0 - 59)"
	Leer minutoentrada
	Escribir "Ingrese la hora de salida (formato de 24 horas)"
	Leer horasalida
	Escribir "Ingrese los minutos de salida (formato de 0 - 59)"
	Leer minutosalida
	
	// Proceso
	// Calcular tiempo total en horas y minutos
	totalHoras <- horasalida - horaentrada
	totalMinutos <- minutosalida - minutoentrada
	
	// Evaluar casos
	Si totalMinutos < 0 Entonces
		totalMinutos <- totalMinutos + 60
		totalHoras <- totalHoras - 1
	FinSi
	
	// Convertir todo a minutos
	totalMinutos <- (totalHoras * 60) + totalMinutos
	
	// Inicializar cobro total
	totalcobro <- 0
	
	// Cobro por horas completas (cada hora cuesta 15 pesos)
	Si totalMinutos >= 60 Entonces
		totalcobro <- totalcobro + (totalMinutos / 60) * 15
	FinSi
	
	// Calcular minutos restantes para fracciones de 15 minutos
	minutosrestantes <- totalMinutos % 60
	
	// Cobro por cada fracción de 15 minutos
	Si minutosrestantes > 0 Entonces
		fracciones15min <- minutosrestantes / 15
		Si minutosrestantes % 15 <> 0 Entonces
			fracciones15min <- fracciones15min + 1
		FinSi
		
		// Cobrar por fracciones
		totalcobro <- totalcobro + fracciones15min * 6
	FinSi
	
	// Convertir minutos restantes a segundos
	totalSegundos <- minutosrestantes * 60
	
	// Salida
	Escribir "El total a pagar es de: ", totalcobro, " pesos"
	Escribir "El tiempo restante en segundos es: ", totalSegundos, " segundos"
FinAlgoritmo

