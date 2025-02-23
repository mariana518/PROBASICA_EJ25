#Simular el lanzamiento de un dado y de una moneda


import random

# Lanzamiento de dado (número aleatorio entre 1 y 6)
dado = random.randint(1, 6)
print(f"Resultado del lanzamiento del dado: {dado}")


#Lanzamiento de una moneda (solo dos posibilidades de respuesta)
moneda = random.choice(['cara', 'cruz'])
print(f"Resultado del lanzamiento de la moneda: {moneda}")