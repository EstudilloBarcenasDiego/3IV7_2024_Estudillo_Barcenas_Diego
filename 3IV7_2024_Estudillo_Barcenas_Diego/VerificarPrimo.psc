Algoritmo VerificarPrimo
    Definir n, i, contador Como Entero
    Escribir "Ingrese un número: "
    Leer n
    contador <- 0
    Para i <- 1 Hasta n Hacer
        Si n % i == 0 Entonces
            contador <- contador + 1
        FinSi
    FinPara
    Si contador == 2 Entonces
        Escribir "El número ", n, " es primo."
    SiNo
        Escribir "El número ", n, " no es primo."
    FinSi
FinAlgoritmo