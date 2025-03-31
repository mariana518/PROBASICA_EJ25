

import json
class Estudiante:
    """Clase para representar un estudiante con nombre y calificación."""

    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def mostrar_info(self):
        """Devuelve la información del estudiante."""
        return f"Nombre: {self.nombre}, Calificación: {self.calificacion}"


def agregar_estudiante(lista):
    """Función para agregar un estudiante a la lista."""
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación del estudiante: "))
    lista.append(Estudiante(nombre, calificacion))  # Se almacena como objeto
    print("Estudiante agregado con éxito.")


def listar_estudiantes(lista):
    """Función para listar estudiantes en orden alfabético."""
    if not lista:
        print(" No hay estudiantes registrados.")
        return
    
    print("\n Lista de estudiantes:")
    for estudiante in sorted(lista, key=lambda x: x.nombre):  # Ordena alfabéticamente
        print(f"- {estudiante.mostrar_info()}")


def buscar_estudiante(lista):
    """Función para buscar un estudiante por su nombre."""
    nombre_buscado = input("Ingrese el nombre del estudiante a buscar: ")

    for estudiante in lista:
        if estudiante.nombre.lower() == nombre_buscado.lower():
            print(f"Estudiante encontrado: {estudiante.mostrar_info()}")
            return

    print(" Estudiante no encontrado.")


def main():
    """Función principal con el menú."""
    estudiantes_lista = []  # Lista donde se almacenan los estudiantes

    while True:
        print("\n Menú de Opciones:")
        print("1. Agregar estudiante")
        print("2. Listar estudiantes")
        print("3. Buscar estudiante")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            agregar_estudiante(estudiantes_lista)
        elif opcion == '2':
            listar_estudiantes(estudiantes_lista)
        elif opcion == '3':
            buscar_estudiante(estudiantes_lista)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()