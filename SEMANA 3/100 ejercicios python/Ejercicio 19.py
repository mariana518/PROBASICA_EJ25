#Generar números aleatorios con distintas distribuciones.

from random import randint
listam=list()
listao=list()
elementos=int(input("introduce la cantidad de elemento:"))
for cont in range (-elementos, elementos):
    if cont<0:
        listao.append (randint(-100,0))
    elif cont>0:
        listam.append (randint(1,100))
    else:
        listam.append(randint(0,1))
#combinar lista
#forma 1
listaCompleta= listam + listao
print(listaCompleta)
#FORMA 2
listam.extend(listao)
print(listam)