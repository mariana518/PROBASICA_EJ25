#Contar el número de vocales y consonantes en una cadena

#poner las variables solo como texto, sin comas ni parentesis ni nada, solo comillas
#las ponemos también en mayusculas para que las cuente
vocales="aeiouAEIOU"
consonantes="bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"

#esto hay que ponerlo al inicio
#definir variables e igualarlas a 0 tambien al inicio
prueba=str(input("ingresa una palabra:"))
cantidad_vocales=0
cantidad_consonantes=0

#volver a poner las variables que igualaste a 0 pero con algo más que las diferencie (si no las vuelves a poner dentro de "def" no va a funcionar)
#para que funciona y cuente hay que poner +=1
#el return va a ser con las variables que puse dentro de def y no al inicio, las del inicio solo son paea llevar un contador
def vocales_consonantes(prueba):
    cantidad_vocales_m=0
    cantidad_consonantes_m=0
    for caracter in prueba:
        if caracter in vocales:
            cantidad_vocales_m+=1
        elif caracter in consonantes:
            cantidad_consonantes_m+=1

    return cantidad_vocales_m, cantidad_consonantes_m

#hay que poner este texto de las primeras variables del contador (antes de iniciar todo) igualado a lo que pusimos en def
cantidad_vocales, cantidad_consonantes = vocales_consonantes(prueba)


#hay que imprimir para que funcione, hay que poner las primeras variables entre llaves
print(f"vocales: {cantidad_vocales}")
print(f"Consonantes:{cantidad_consonantes}")









