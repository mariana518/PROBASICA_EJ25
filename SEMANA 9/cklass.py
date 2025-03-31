  

numeros=[2, 4, 6, 8, 10]
def suma2(a,b, C=0):
    return a+b+C
    '''
class Sumatoria():
    def __init__(self, lista=[0]):
        self.n= len(lista)
        self.sum = sum(lista)
        print("Hola Mundo")
        
    def getSum(self):
        return self.sum
    
    def getProm(self):
        return self.getSum()/ self.n





#def __init__():
 #   print("return none")

#__init__()   #esto tambien funciona
demo= Sumatoria()
demo2= Sumatoria(numeros)
print(demo.getSum(), demo2.getSum(), demo2.getProm())

'''''

from abc import ABC, abstractmethod

class Politopo2(ABC):
    
    @staticmethod
    def __init__(self,NombreFigura='2-Politopo'):
        self.name = NombreFigura
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    

class Cuadrado(Politopo2):
    def __init__(self,l,Nombre='Cuadrado'):
        self.lado = l
        super().__init__(self,NombreFigura=Nombre)
        
    def area(self):
        return self.lado**2
    
    def perimetro(self):
        return self.lado*4
    
    
cua = Cuadrado(34)

print(cua.area(),cua.perimetro())


class Triangulo(Politopo2):
    def __init__(self,a,b,c,Nombre='Triangulo'):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c
        super().__init__(self,NombreFigura=Nombre)
        
    def area(self):
        return ((self.LadoA**2)-(self.LadoB/2)**2)**1/2
                    
    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC