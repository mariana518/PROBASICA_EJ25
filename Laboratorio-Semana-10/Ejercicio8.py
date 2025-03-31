def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    # Dividimos la lista en dos mitades
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    ordenado = []
    i = j = 0
    
    # Combinamos las dos mitades ordenadas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            ordenado.append(izquierda[i])
            i += 1
        else:
            ordenado.append(derecha[j])
            j += 1
    
    # Agregamos los elementos restantes (si los hay)
    ordenado.extend(izquierda[i:])
    ordenado.extend(derecha[j:])
    
    return ordenado

# Función principal
def main():
    # Solicitamos los números al usuario
    lista = list(map(int, input("Ingresa los números separados por espacio: ").split()))
    
    # Mostramos la lista antes del ordenamiento
    print("\nLista original:")
    print(lista)
    
    # Ordenamos la lista con MergeSort
    lista_ordenada = merge_sort(lista)
    
    # Mostramos la lista después del ordenamiento
    print("\nLista ordenada:")
    print(lista_ordenada)

if __name__ == "__main__":
    main()