#Generar y analizar datos estadísticos




#Generar Datos
import numpy as np

# Generar 1000 datos aleatorios de una distribución uniforme entre 0 y 100
datos_uniformes = np.random.uniform(0, 100, 1000)

# Generar 1000 datos aleatorios de una distribución normal con media 50 y desviación estándar 10
datos_normales = np.random.normal(50, 10, 1000)

# Mostrar los primeros 5 datos generados
print("Primeros 5 datos de la distribución uniforme:", datos_uniformes[:5])
print("Primeros 5 datos de la distribución normal:", datos_normales[:5])