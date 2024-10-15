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
        Escribir "No es una ecuación de segundo grado."
    Sino
        Si formulageneral >= 0 Entonces
            raizp = (-b + Raiz(formulageneral)) / (2 * a)
            raizn = (-b - Raiz(formulageneral)) / (2 * a)
            Escribir "Raíces reales: ", raizp, " y ", raizn
            
            // Si las raíces son enteras, realiza suma o resta
            Si raizp = Trunc(raizp) Entonces
                sumap = raizp + raizn
                Escribir "La suma de las raíces enteras es: ", sumap
            Fin Si
            
            Si raizn = Trunc(raizn) Entonces
                suman = raizn - raizp
                Escribir "La resta de las raíces enteras es: ", suman
            Fin Si
            
        Sino
            Escribir "Raíces imaginarias:"
            Escribir "Raíz 1: ", -b / (2 * a), " + ", Raiz(-formulageneral) / (2 * a), "i"
            Escribir "Raíz 2: ", -b / (2 * a), " - ", Raiz(-formulageneral) / (2 * a), "i"
        Fin Si
    Fin Si
FinAlgoritmo

