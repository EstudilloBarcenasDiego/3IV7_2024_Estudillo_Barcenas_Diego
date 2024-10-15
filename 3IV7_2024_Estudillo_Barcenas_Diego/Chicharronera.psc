Algoritmo Chicharronera
    Definir a, b, c Como Real
    Definir formulageneral Como Real
    Definir raizp, raizn Como Real
    Definir sumap, suman Como Real
    
    Escribir "Ingrese el coeficiente a :"
    Leer a 
    Escribir "Ingrese el coeficiente b :"
    Leer b
    Escribir "Ingrese el coeficiente c :"
    Leer c
    
    formulageneral = b^2 - 4 * a * c
    
    Si a = 0 Entonces
        Escribir "No es una ecuaci�n de segundo grado."
    Sino
        Si formulageneral >= 0 Entonces
            raizp = (-b + Raiz(formulageneral)) / (2 * a)
            raizn = (-b - Raiz(formulageneral)) / (2 * a)
            Escribir "Ra�ces reales: ", raizp, " y ", raizn
            
            // Si las ra�ces son enteras, realiza suma o resta
            Si raizp = Trunc(raizp) Entonces
                sumap = raizp + raizn
                Escribir "La suma de las ra�ces enteras es: ", sumap
            Fin Si
            
            Si raizn = Trunc(raizn) Entonces
                suman = raizn - raizp
                Escribir "La resta de las ra�ces enteras es: ", suman
            Fin Si
            
        Sino
            Escribir "Ra�ces imaginarias:"
            Escribir "Ra�z 1: ", -b / (2 * a), " + ", Raiz(-formulageneral) / (2 * a), "i"
            Escribir "Ra�z 2: ", -b / (2 * a), " - ", Raiz(-formulageneral) / (2 * a), "i"
        Fin Si
    Fin Si
FinAlgoritmo

