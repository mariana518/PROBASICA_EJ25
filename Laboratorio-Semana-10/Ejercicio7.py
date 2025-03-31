import random

# Función para realizar el algoritmo de Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Función para realizar la búsqueda binaria
def busqueda_binaria(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1  # Si no se encuentra el número

# Función principal
def main():
    # Generar una lista de n números aleatorios
    n = int(input("¿Cuántos números aleatorios quieres generar? "))
    lista = [random.randint(1, 100) for _ in range(n)]
    
    # Mostrar la lista antes del ordenamiento
    print("\nLista original:")
    print(lista)
    
    # Ordenar la lista usando Quicksort
    lista_ordenada = quicksort(lista)
    
    # Mostrar la lista después del ordenamiento
    print("\nLista ordenada:")
    print(lista_ordenada)
    
    # Realizar búsqueda binaria
    objetivo = int(input("\nIngresa el número que deseas buscar: "))
    resultado = busqueda_binaria(lista_ordenada, objetivo)
    
    # Mostrar los resultados de la búsqueda
    if resultado != -1:
        print(f"\nEl número {objetivo} se encuentra en la posición {resultado}.")
    else:
        print(f"\nEl número {objetivo} no fue encontrado en la lista.")

if __name__ == "__main__":
    main()