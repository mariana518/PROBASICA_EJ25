#Calcular el área y volumen de distintas figuras geométricas

import math


#Área
#Solo vamos a poner los valores de el área que vayamos a sacar, si no los necesitamos en el área les vamos a poner un 0
b=float(input("ingrese la base:"))
h=float(input("ingrese la altura:"))
D=float(input("ingrese el valor de la Diagonal mayor:"))
d=float(input("ingrese el valor de la oytra diagonal menor:"))
B=float(input("ingrese el valor de la base mayor:"))
r=float(input("ingrese el valor de el radio:"))
l=float(input("ingrese el valor del lado:"))
pi= math.pi
áreas={"cuadrado": l*l, "rectángulo": b*h, "triangulo": (b*h)/2, "rombo": D*d, "trapecio": b*h, "circulo":pi*(r**2)}

a=(str(input("¿De que figura quieres sacar el área? (cua/rec/tri/ro/tra/cir):")))


if a.lower()== "cua":
    l=float(input("ingrese el valor del lado:"))
    print("el área del cuadrado es:", áreas["cuadrado"]) 
elif a.lower()== "rec":
    b=float(input("ingrese la base:"))
    h=float(input("ingrese la altura:"))
    print("el área del rectangulo es:", áreas["rectangulo"])
elif a.lower()== "tri":
    b=float(input("ingrese la base:"))
    h=float(input("ingrese la altura:"))
    print("el área del triangulo es:", áreas["triangulo"])
elif a.lower()== "ro":
    D=float(input("ingrese el valor de la Diagonal mayor:"))
    d=float(input("ingrese el valor de la oytra diagonal menor:"))
    print("el área del rombo es:", áreas["rombo"])
elif a.lower()== "tra":
    b=float(input("ingrese la base:"))
    h=float(input("ingrese la altura:"))
    print("el área del trapecio es:", áreas["trapecio"])
elif a.lower ()== "cir":
    print("el área del circulo es:" , áreas["circulo"])
    b=float(input("ingrese la base:"))


