#Leer, escribir y modificar un archivo de texto.

#Método 1
''''
with open("prueba.txt", "w") as variable:
    print("Favor de revisar su correo para confirmar su cuenta", file=variable)
'''
#Método 2

variableP=open("prueba2.txt", "w")

print("No se accedió a su cuenta porque no verificó con el correo", file=variableP)

variableP.close()
