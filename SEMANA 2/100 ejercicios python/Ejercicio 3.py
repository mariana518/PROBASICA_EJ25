
#ACTIVIDAD 3: Calcular el factorial de un número dado

def fact(n):
    if n<0:
        return "Error" 
    if n==0 or n==1:
        return 1
    for i in range (1,n):
        n= n*i
    return n
a=int(input("ingrese el valor a calcular="))
print(fact(a))

