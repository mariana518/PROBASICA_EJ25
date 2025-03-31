class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio


    def mostrar_informacion(self):
        """Muestra la información básica del vehículo"""
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}\nPrecio: ${self.precio}"
    
   

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        """Muestra la información completa de la motocicleta"""
        info = super().mostrar_informacion()
        return f"{info}\nCilindrada: {self.cilindrada} cc"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, numero_puertas):
        super().__init__(marca, modelo, año, precio)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        """Muestra la información completa del automóvil"""
        info = super().mostrar_informacion()
        return f"{info}\nNúmero de puertas: {self.numero_puertas}"
    


auto=Automovil("Tesla", "Modelo 3" ,2018, 1029900,4)
print("Información del Automovil:")
print(auto.mostrar_informacion())

moto = Motocicleta("Kawasaki", "Ninja H2rABS", 2024, 849990, 4)
print("Información de la Motocicleta:")
print(moto.mostrar_informacion())