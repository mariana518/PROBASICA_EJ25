

# Función para agregar un nuevo contacto
def agregar_contacto():
    nombre = str(input("Ingresa el nombre del contacto: "))
    numero = str(input("Ingresa el número de teléfono del contacto: "))
    correo = str(input("Ingresa el correo electrónico del contacto: "))

    '''# Crear la tupla para el contacto y agregarla a la lista
    contacto = (nombre, numero, correo)
    agenda.append(contacto)
    print(f"Contacto '{nombre}' agregado exitosamente.")

# Función para buscar un contacto por nombre
def buscar_contacto():
    nombre_a_buscar = str(input("Ingresa el nombre del contacto a buscar: "))

    # Buscar el contacto en la lista
    encontrado = False
    for contacto in agenda:
        if nombre_a_buscar == contacto[0].lower():  # Compara el nombre sin importar mayúsculas/minúsculas
            print(f"Información del contacto '{contacto[0]}':")
            print(f"Teléfono: {contacto[1]}")
            print(f"Correo electrónico: {contacto[2]}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"No se encontró el contacto con el nombre '{nombre_a_buscar}'.")

# Función para listar todos los contactos ordenados alfabéticamente
def listar_contactos():
    if not agenda:
        print("No hay contactos registrados.")
    else:
        # Ordenamos la lista por el nombre del contacto (primer elemento de cada tupla)
        agenda_ordenada = sorted(agenda, key=lambda contacto: contacto[0].lower())
        print("\nLista de contactos ordenada alfabéticamente:")
        for i, contacto in enumerate(agenda_ordenada, 1):
            print(f"{i}. Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Correo: {contacto[2]}")'''