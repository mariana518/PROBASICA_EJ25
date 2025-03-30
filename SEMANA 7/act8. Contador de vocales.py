
def contadordevocales(cadena):
    diccionario_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for caracter in cadena.lower():
        if caracter in diccionario_vocales:
            diccionario_vocales[caracter] += 1  # Aumenta el contador

    return diccionario_vocales  # Debe estar fuera del for

mensaje = "albaricoque"
resultado = contadordevocales(mensaje)
print(resultado)
