d1=dict()
d1[1]= 'uno'
d1[2]= "dos"
d1[3]= '''tres''' #las comillas no afectan en nada y todos son str
d1[6]="""seis"""
d2 = {}
d2['a']="a"
d2['b']="be"
d2['c']="ce"
d2['d']="de"
print(d1,type(d1), '\n',d2, type(d2))

#d1.clear() #para borrarlo
#print(d1)
#d1.copy() #copiarlo
d3=d1.copy()
d3[2169421]= 'matricula mariana'
print(d1,d3)
#d1.fromkeys() #llaves
#d3=d1.copy()
#d3[4224242]= 'matricula'
#print(d1,d3)

print(d1.fromkeys({1,2,3}))
#d1.get() #el get sirve para que me de el significado
print(d1.get(2))  
#d1.items() #poner los elementos del diccionario como si fueran tuplas
print(d1.items())

for k,v in d1.items():
    print(k,v)
#d1.keys #llaves 
print(d1.keys()) #me los va a devolver como lista
#d1.pop #elimina el ultimo elemento

#d3.pop(2169421)
#print(d3)
#d1.popitem #elimina el elemento que le pidamos (para borrar una tupla)

#d3.popitem()
#print(d3)
#d1.setdefault
d1.setdefault(7)
d1[8]=None
print(d1)
#d1.update #para actualizar
d1.update({17:'diecisiete', 18:'dieciocho', 19: 'diecinueve'})
print(d1)


#d1.values
print(d1.values())