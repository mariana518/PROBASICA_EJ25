conjunto = {1,2,3,4}
conjunto2= {3,4,5,6}


print(type(conjunto), type(conjunto2))

##conjunto.add()  #sirve para agregar elementos
#conjunto.add(0)
#print(conjunto)


##conjunto.clear()
#print(conjunto)


##conjunto.copy()
conjunto3 = conjunto.copy()
#print(conjunto3)

##conjunto.difference()

print(conjunto.difference(conjunto2))




##conjunto.discard()

conjunto.discard(7)


##conjunto.intersection()
print(conjunto3.intersection(conjunto2))


##conjunto.isdisjoint()#creo que este es para comparar con otro}
print(conjunto.isdisjoint(conjunto2))


subset={1,4}
##conjunto.issubset()
print(subset.issubset(subset))


superset={1,2,3,4,5,6,7,8,9,10}
##conjunto.issuperset()
print(superset.issuperset(conjunto))

print(conjunto.issubset(superset))


##conjunto.pop()
#conjunto.pop
#print(conjunto)
#conjunto.add(5)
#print(conjunto)
##conjunto.remove()
#conjunto.remove(5)
#print(conjunto)

conjunto.remove
#conjunto.symmetric_difference()
print(conjunto.symmetric_difference(conjunto2))


##conjunto.union() #fuciona los conjuntos sin repetir

print(conjunto.union(conjunto2))
print(conjunto)

##conjunto.update()
conjunto.update(conjunto2)
print(conjunto)



##conjunto.difference_update() #1,2
##conjunto.intersection_update() #3,4
##conjunto.symmetric_difference_update() #1,2,5,6
#el update es un cambio "para siempre"