#Desarrolla un programa para promedio, mediana, y desviación estandar





def sumaListaNumeros(*args):
    print(type(args))
    suma= sum( i for i in args)
    return suma


n = sumaListaNumeros(1,2,3,4,5,6)
print(n)


promedio = lambda suma_valores, cantidad_valores: suma_valores/cantidad_valores
print(promedio(21,6))


def calcular_mediana(lista):
    # Ordenamos la lista de menor a mayor utilizando una función lambda
    lista_ordenada = sorted(lista, key=lambda x: x)

    # Calculamos el número de elementos en la lista
    n = len(lista_ordenada)

    # Si la lista tiene un número impar de elementos, la mediana es el valor central
    if n % 2 != 0:
        mediana = lista_ordenada[n // 2]
    else:
        # Si la lista tiene un número par de elementos, la mediana es el promedio de los dos valores centrales
        mediana = (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2

    return mediana

numeros = list(map(int, input("Ingresa los números separados por espacio: ").split()))

mediana=calcular_mediana(numeros)
print(f"La mediana es: {mediana}")


