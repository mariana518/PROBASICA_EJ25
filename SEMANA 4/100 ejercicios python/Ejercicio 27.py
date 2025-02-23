#Crear un conversor de unidades

#ongitud: metros (m), kilómetros (km), millas (mi), pulgadas (in)
#Peso: gramos (g), kilogramos (kg), libras (lb)


# Función para convertir Longitud
def convertir_longitud(valor, unidad_origen, unidad_destino):
    # Definir las conversiones a metros
    conversiones = {'m': 1,'km': 1000,'mi': 1609.34,'in': 0.0254}
    
    # Convertir el valor a metros
    valor_en_metros = valor * conversiones[unidad_origen]
    
    # Convertir el valor a la unidad destino
    valor_convertido = valor_en_metros / conversiones[unidad_destino]
    
    return valor_convertido

# Función para convertir Peso
def convertir_peso(valor, unidad_origen, unidad_destino):
    # Definir las conversiones a gramos
    conversiones = {'g': 1,'kg': 1000,'lb': 453.592 }
    
    # Convertir el valor a gramos
    valor_en_gramos = valor * conversiones[unidad_origen]
    
    # Convertir el valor a la unidad destino
    valor_convertido = valor_en_gramos / conversiones[unidad_destino]
    
    return valor_convertido


def conversor_unidades():
  
    
    tipo_conversion = input("¿Qué tipo de conversión deseas hacer? (longitud, peso,): ").lower()
    
    if tipo_conversion == "longitud":
        valor = float(input("Introduce el valor a convertir: "))
        unidad_origen = input("Introduce la unidad de origen (m, km, mi, in): ").lower()
        unidad_destino = input("Introduce la unidad de destino (m, km, mi, in): ").lower()
        resultado = convertir_longitud(valor, unidad_origen, unidad_destino)
    
    elif tipo_conversion == "peso":
        valor = float(input("Introduce el valor a convertir: "))
        unidad_origen = input("Introduce la unidad de origen (g, kg, lb): ").lower()
        unidad_destino = input("Introduce la unidad de destino (g, kg, lb): ").lower()
        resultado = convertir_peso(valor, unidad_origen, unidad_destino)
    
    
   
    
    print(f"El resultado de la conversión es: {resultado}")

# Llamar a la función principal
conversor_unidades()