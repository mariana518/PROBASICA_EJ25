#¿que se puede hacer con str?


mensaje="Johanne Sacreblue"
print (mensaje.capitalize())#Para convertir solo la primera en mayúscula

print(mensaje.count("n"))#Para  saber cuanto hay de lo que busco

print(mensaje.index('a'))#Para saber en que ubicación esta lo que busco (solo da la primera ubicación)


#esta es para saber en que posiciones esta lo que busco (a diferencia de la otra esta da todas las posiciones y no solo la primera)
indicesE=[]
for indice in range(len(mensaje)):
    if mensaje[indice]=="e":
        indicesE.append(indice)
print(indicesE)