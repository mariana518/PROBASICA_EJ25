#Implementar búsqueda binaria y lineal


#lista
num=(int(input("¿Qué número quieres buscar?:")))
listaCompleta=(1,2,3,4,5,6,7,8,9)

#Busqueda lineal
for itm in listaCompleta:
    if itm== num:
        print("el número se encuentra en la posición", listaCompleta.index(itm))
        break


#Busqueda binaria
izquierda=0
derecha=len(listaCompleta)-1
encontrado=False

while izquierda <= derecha:
    medio=(izquierda+derecha)//2
    if listaCompleta[medio]== num:
        print(f"El número {num} se encuentra en la posición {medio}")
        encontrado=True
        break
    elif listaCompleta[medio] < num:
        izquierda=medio+1
    else:
        derecha=medio-1
