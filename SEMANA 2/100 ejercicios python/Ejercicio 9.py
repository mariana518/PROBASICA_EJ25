#ACTIVIDAD 9: Genera una lista de numeros e impares hasta un limite dado
limit=int(input("ingrese un límite: "))
par=[]
impar=list()

for num in range (1,limit+1):
    if num%2==0:
        par.append(num)
    else:
        impar.append

tamanio= max(len(par), len(impar))
print(tamanio)

for item in range(tamanio):
    try:
        print(par[item], impar[item], sep= '|')
    except IndexError:
        print('-', impar[item], sep= '|')