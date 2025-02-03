from random import randint


print("Variables")
#Tipo de Variables

#Tipos de datos básicos
str()
int()
float()

#Tipos d datos estructurados
list()
dict()
set()
tuple()
#enumerate()
#range()

#LISTAS
#Forma 1
lista=list()
lista=list([1,2,3])
#Forma 2
lista=[]
lista=[1,2,3]


diasSemana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
daysWeek=["Mon", "Tue", "Wed", "Thu", "Fri"]

print(diasSemana, type(diasSemana), daysWeek, type(daysWeek))

combinado=[1, 2.34, "Alzheimer", "v6", 3.14, diasSemana, daysWeek]

print(combinado, type(combinado))

#CONJUNTOS

conjunto= set()
print(conjunto, type(conjunto))

conjunto={1,2,3}
print(conjunto, type(conjunto))
#en un conjunto los datos no se pueden repetir más de una vez
#para diferenciar un conjunto de una tupla adentro de los parentesis del conjunto debe haber contenido

#ejemplo conjunto
conjunto= set()
lista= list()

from random import randint
for i in range(25):
    t= randint(90, 100)
    lista.append(t)
    conjunto.add(t)
print(lista)
print(conjunto)

#TUPLAS

tupla= tuple()
tupla=()

#las tuplas manejan valores que no se pueden modificar

#Ejemplo tupla

tupla=[3.14, 2.74, 1.62]
tupla2=("pi", "e", "phi")

tupla[0]= tupla[0]+1

print(tupla)

#DICCIONARIO

diccionario= dict()
diccionario = {}

#ejemplo diccionario
numerosLetras={"pi": 3.14, "e": 2.74, "phi": 1.62}

print(numerosLetras["pi"])

numerosLetras["tau"]= 6.28
 
print(numerosLetras)
