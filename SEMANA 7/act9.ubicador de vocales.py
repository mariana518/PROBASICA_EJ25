'''Cree una función llamada 'ubicadorDeVocales' que tome una cadena como parámetro.
Dentro de la función, inicialice un diccionario vacío para almacenar las vocales y sus ubicaciones.
Recorre cada carácter de la cadena:
Comprueba si el carácter es una vocal (a, e, i, o, u). INCLUYENDO ACENTOS
Si es una vocal, actualiza el diccionario para devolver la ubicación de las vocales.
Devuelve el diccionario con la lista de las ubicaciones de las vocales..'
'''''
'''''
def ubicadorDevocales (cadena):
    '''
'''
def ubicadorDeVocales(cadena):
    vocales = "aáeéiíoóuú"
    ubicaciones = {}
    
    for indice, caracter in enumerate(cadena):
        if caracter.lower() in vocales:
            if caracter.lower() not in ubicaciones:
                ubicaciones[caracter()] = []
            ubicaciones[caracter.lower()].append(indice)
        return ubicaciones


'print(ubicadorDeVocales("murcielago"))' 
'print(ubicadorDeVocales("eucalipto"))'
'print(ubicadorDeVocales("Albericoque"))'

'''
def ubicadorDeVocales(cadena):
    vocales = "aáeéiíoóuú"
    ubicaciones = {}
    
    for indice, caracter in enumerate(cadena):
        if caracter.lower() in vocales:
            if caracter.lower() not in ubicaciones:
                ubicaciones[caracter.lower()] = []
            ubicaciones[caracter.lower()].append(indice)
    
    return ubicaciones

# Ejemplo de uso
mensaje = "albaricoque"
resultado = ubicadorDeVocales(mensaje)
print(resultado)
