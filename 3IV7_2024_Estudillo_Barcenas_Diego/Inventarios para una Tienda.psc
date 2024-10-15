Algoritmo Inventarios_Tienda
	Definir producto como texto
	Definir codigoproducto, cantidad como entero
	Definir precio como real 
	
	//crear menu de selección
	
	Mientras opcion <> 5 Hacer
		Escribir "1 - Ingresar un nuevo Producto"
		Escribir "2 - Actualiza un Producto"
		Escribir "3 - Consulta el Inventario"
		Escribir "4 - Generar Reporte"
		Escribir "5 - Salir"
		
		Leer opcion
		
		Segun opcion Hacer
			Caso 1:
				Escribir "Ingresa el nombre del producto"
				Leer producto
				Escribir "Ingresa el código del producto"
				Leer codigoproducto
				Escribir "Ingresa la cantidad"
				Leer cantidad
				Escribir "Ingresa el precio"
				Leer precio
			Caso 2:
				Escribir "Ingresa el codigo del producto a actualizar"
				Leer codigoproducto
				Escribir "Ingresa la nueva cantidad"
				Leer cantidad
			Caso 3:
				Escribir "Consultar Inventario "
				Leer codigoproducto
				Escribir "Nombre del producto ", producto
				Escribir "Código del producto ", codigoproducto
				Escribir "Pecio del producto ", precio
				Escribir "Cantidad del producto ", cantidad
			Caso 4:
				Escribir "Le reporto que no le entendí nada :D"
		FinSegun
	FinMientras
FinAlgoritmo