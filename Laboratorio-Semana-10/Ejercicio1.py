

#contador de palabras

def contador_de_palabras(texto):
    texto_l= texto.replace(",", "")
    palabras=texto_l.split()
    cantidad_de_palabras= len(palabras)
    return cantidad_de_palabras


texto1= str(input("Ingrese un texto:"))

resultado=contador_de_palabras(texto1)

print(f"La canatidad de palabras es: {resultado}")


#cantidad de palabras únicas

def palabras_unicas(texto1):
    palabras=set(texto1.split())
    return palabras 

unicas=palabras_unicas(texto1)
print(unicas)

#frecuencia de cada palabra 
def frecuencia_palabras(texto):
  
    import string
    from collections import defaultdict
    
    palabras = texto.split()
    
   
    frecuencia = defaultdict(int)
    for palabra in palabras:
        frecuencia[palabra] += 1
    
    return dict(frecuencia)

print(frecuencia_palabras(texto1))

#palabra más frecuente
def palabra_mas_frecuente(texto):

    import string
    from collections import defaultdict
    
    palabras = texto.split()
    
    frecuencia = defaultdict(int)
    for palabra in palabras:
        frecuencia[palabra] += 1
    
    # Encontramos la palabra más frecuente
    palabra_max = max(frecuencia, key=frecuencia.get)
    return palabra_max, frecuencia[palabra_max]

print(palabra_mas_frecuente(texto1))
