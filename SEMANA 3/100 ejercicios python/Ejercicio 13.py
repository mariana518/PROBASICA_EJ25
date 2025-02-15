#Convertir una temperatura entre distintas escalas.


escalasTemperatura={"kelvin": 273.15, "Fahrenheit":32}

a=(str(input("¿A qué escala quieres convertir los grados celsius? (K/F):")))
M=(int(input("Ingresa la cantidad en celsius:")))

if a.upper()=='K':
    print("De Celsius a Kelvin es:", M + escalasTemperatura["kelvin"])
if a.upper()=='F':
    print("De celsius a Fahrenheits es:", M*9/5 + escalasTemperatura["Fahrenheit"])



