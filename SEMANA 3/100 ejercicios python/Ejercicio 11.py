#Verificar si una cadena es un palíndromo.

def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir a minúsculas para evitar diferencias de mayúsculas/minúsculas
    palabra = palabra.replace(" ","")
    return palabra == palabra[::-1]  # Comprobar si la palabra es igual a su reverso
palabra= input("Introduce una palabra:")
if es_palindromo(palabra):

    print(f'"{palabra}" es un palíndromo.')
else:
    print(f'"{palabra}" no es un palíndromo.')

  