# Determinar si un año es bisiesto.

def es_bisiesto(año):
    # Un año es bisiesto si es divisible entre 4
    # Pero no es bisiesto si es divisible entre 100, excepto si también es divisible entre 400
    if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
        return True
    else:
        return False

año = int(input("Introduce un año: "))
if es_bisiesto(año):
    print(f"{año} es un año bisiesto.")
else:
    print(f"{año} no es un año bisiesto.")