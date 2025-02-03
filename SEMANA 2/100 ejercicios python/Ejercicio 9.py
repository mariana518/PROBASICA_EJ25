#ACTIVIDAD 9: Genera una lista de numeros e impares hasta un limite dado
limit=int(input("ingrese un límite: "))
par=[]
impar=[]

for i in range (1,limit+1):
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)
print("numeros pares:", par)
print("numeros impares:", impar)