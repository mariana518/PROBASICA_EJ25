#Determinar si un número es par, impar o multiplo de otro

a= int(input("Ingrese un número= "))
b= int(input("Ingrese otro número= "))
def núm(a,b):
    if a%b == 0:
        return "el número es múltiplo del otro"
    else:
        return "el número no es múltiplo del otro"
print(núm(a,b))

m= int(input("Ingrese un número= "))
def par_impar(o):
    if o == 0:
        return "Error"
    if m%2 == 0:
        return "el número es par"
    else:
        return "el número es impar "

print (par_impar(m))



