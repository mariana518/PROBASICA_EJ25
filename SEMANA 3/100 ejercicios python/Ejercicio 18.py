# Resolver ecuaciones cuadráticas.

import cmath #el cmath se usa para operaciones un poco más complejas

a=float(input("ingrese el primer valor:"))
b=float(input("ingrese al segundo valor:"))
c=float(input("ingrese el tercer valor:"))

def solucion_ecuación_cuadrática (a,b, c):

    discriminante= b**2-4*a*c  #primero tenemos que calcular el discriminante para ver si vamos a tener soluciones reales o complejas y tambien para poderlo usar después como variable

    #ahora hay que calcular las dos posibles soluciones
    #el "cmath.sqrt" se usa para las raices cuadradas o solo el "sqrt"
    x1= -b + cmath.sqrt(discriminante)/2*a
    x2= -b - cmath.sqrt(discriminante)/2*a
    return x1,x2

#se tiene que poner este texto para al final que queramos imprimir podamos usarlo
soluciónes= solucion_ecuación_cuadrática(a,b,c)

#la letra "f" siempre va al inicio
#el 0 y el 1 en este caso se usan porque nos van a quedar dos resultados, tambien sirven para que en el resultado especifique si sale complejo
print(f"Las soluciones son= {soluciónes[0]} y x2 = {soluciónes[1]}")