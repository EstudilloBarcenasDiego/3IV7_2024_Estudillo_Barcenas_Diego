Algoritmo Gestion_Reservas_Hotel_Budapest
	Definir opcion, numReserva, habitacionesTotales, habitacionesDisponibles, reservas Como entero
	Definir nombreCliente, habitacionSeleccionada, fechaEntrada, fechaSalida Como cadena
	habitacionesTotales <- 10 
	habitacionesDisponibles <- 10 
	reservas <- 0  
		
		// Menú del sistema
		Mientras opcion <> 5 Hacer
			Escribir "Bienvenido al Sistema de Gestión de Reservas de Hotel Budapest"
			Escribir "Seleccione una opción:"
			Escribir "1. Registro de Reserva"
			Escribir "2. Cancelación de Reserva"
			Escribir "3. Consulta de Disponibilidad"
			Escribir "4. Gestión de Ocupación"
			Escribir "5. Salir"
			Leer opcion
			
			Segun opcion Hacer
				Caso 1:
					Si habitacionesDisponibles > 0 Entonces
						Escribir "Ingrese su nombre:"
						Leer nombreCliente
						Escribir "Seleccione una habitación (1-", habitacionesTotales, "):"
						Leer habitacionSeleccionada
						Escribir "Ingrese la dia de entrada (dd):"
						Leer diaEntrada
						Escribir "Ingrese la mes de entrada (mm):"
						Leer mesEntrada
						Escribir "Ingrese la año de entrada (aaaa):"
						Leer añoEntrada
						Escribir "Ingrese la dia de salida (dd):"
						Leer diaSalida
						Escribir "Ingrese la mes de salida (mm):"
						Leer mesSalida
						Escribir "Ingrese la año de 2023da (aaaa):"
						Leer añoSalida
						reservas <- reservas + 1
						habitacionesDisponibles <- habitacionesDisponibles - 1
						Escribir "Reserva registrada exitosamente. Número de reserva: ", reservas
					SiNo
						Escribir "Lo sentimos, no hay habitaciones disponibles."
					FinSi
				Caso 2:
					Escribir "Ingrese el número de reserva a cancelar:"
					Leer numReserva
					Si numReserva <= reservas Entonces
						reservas <- reservas - 1
						habitacionesDisponibles <- habitacionesDisponibles + 1
						Escribir "Reserva cancelada exitosamente."
					SiNo
						Escribir "Número de reserva inválido."
					FinSi
				Caso 3:
					Escribir "Habitaciones disponibles: ", habitacionesDisponibles, "/", habitacionesTotales
				Caso 4:
					ocupacion <- ((habitacionesTotales - habitacionesDisponibles) / habitacionesTotales) * 100
					Escribir "El porcentaje de ocupación del hotel es: ", ocupacion, "%"
			FinSegun
		FinMientras
		
		Escribir "Gracias por utilizar el Sistema de Gestión de Reservas de Hotel Budapest"
FinAlgoritmo
