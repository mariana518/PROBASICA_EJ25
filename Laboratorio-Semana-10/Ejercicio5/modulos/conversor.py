'''Crea un modulo de Python llamado conversor.py que contenga funciones para
convertir:
 Kilmetros a millas.
 Celsius a Fahrenheit.
 Litros a galones.
Luego, crea un programa principal que importe el modulo y permita al usuario
realizar conversiones.'''

conversor_unidades = {"millas": 0.621371, "Fahrenheit": 32, 'galones': 0.264172}

j = input("¿Qué es lo que quieres convertir? (km/c/l): ").lower()  # Usamos .lower() para hacer la entrada insensible a mayúsculas
M = input("Ingresa la cantidad en km, c o l: ")


try:
    M = float(M)  
except ValueError:
    print("Error: La cantidad ingresada no es un número válido.")
    exit()


if j == 'km':
    print(f"De Kilómetros a millas es: {M * conversor_unidades['millas']}")
elif j == 'c':
    
    fahrenheit = (M * 9 / 5) + conversor_unidades['Fahrenheit']
    print(f"De Centígrados a Fahrenheit es: {fahrenheit}")
elif j == 'l':
    print(f"De Litros a galones es: {M * conversor_unidades['galones']}")
else:
    print("Unidad no reconocida. Por favor, ingresa una unidad válida.")
