#Encontrar el mayor entre tres nÚmeros dados

a=(int(input("Ingrese el primer número:")))

b=(int(input("Ingrese el segundo número:")))

c=(int(input("Ingrese el tercer número:")))

def es_mayor(a,b,c):
    if a>b and a>c:
        return "el número a es mayor"
    elif b>a and b>c:
        return "el número b es mayor"
    elif c>a and c>b:
        return "el número c es mayor"
    elif c==a==b:
        return "no hay número mayor porque todos son iguales"
print(es_mayor(a,b,c))
    