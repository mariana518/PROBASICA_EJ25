#Calcuar la suma de una serie númerica


n = int(input("ingrese el número de terminos:"))  
a1 =int (input("ingrese el primer término:"))  
an = int(input("ingrese el último término:"))  
# Calcular la suma
suma_serie = (n * (a1 + an)) / 2
print(f"Suma de la serie numérica: {suma_serie}")