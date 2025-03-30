#### Función Global

#def generadorPorMateriaPorPromediosPorGrupo():

palabra ="Generador depromedio por materia por grupo" 

palabra = palabra.title().replace(" ", "")

palabra=palabra[:1].lower() + palabra[1:]


print(palabra)
#anitalavalatina
def Nombrefuncion(args, radio=1):
    print("operaciones", args, radio)
    return False

Nombrefuncion('A')
import math
Nombrefuncion('B', math.pi)



### Función de clase o función local

class NombreClase():
    def __init__(self):  #es de afuerzas poner el self
       self.NombreVariable="valor"
       print("hola mundoo")

    def printNombreVariable(self):
        print(self.NombreVariable)
objetoClase= NombreClase()
objetoClase.printNombreVariable()





#Función en linea o función Lamba (functionline)


pesoNewton = lambda masa, gravedad: masa * gravedad

print(pesoNewton(49,9.81))



def sumaListaDeNumeros(*args):
    print(type(args))
    suma= sum( i for i in args)
    return suma

n = sumaListaDeNumeros(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
print(n)