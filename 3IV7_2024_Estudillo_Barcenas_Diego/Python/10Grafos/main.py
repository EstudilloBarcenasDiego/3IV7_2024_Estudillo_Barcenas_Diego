# Importamos los módulos creados anteriormente
try:
    import grafo
    import logica
    import interfaz
except ImportError as e:
    print(f"Error al importar los módulos: {e}")
    exit(1)  # Finaliza el programa si hay errores de importación

def main():
    try:
        # Crear grafo y obtener nodos y aristas
        mi_grafo = grafo.crear_grafo()
        aristas = grafo.obtener_aritas()
        nodos = grafo.obtener_nodos()

        # Lógica de los algoritmos (Dijkstra y Kruskal)
        algoritmos_logica = {
            "dijkastra": logica.dijkastra,
            "kruskal": logica.kruskal
        }

        # Crear la interfaz para visualizar el grafo y los algoritmos
        interfaz.crear_interfaz(mi_grafo, aristas, nodos, algoritmos_logica)
    except AttributeError as e:
        print(f"Error al acceder a una función del módulo: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
