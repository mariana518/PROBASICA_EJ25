#Implementar y operar con matrices

#SUMA DE MATRICES
matrixA=[[1,2,3], [4,5,6], [7,8,9]]
matrixB=[[15,3,5], [9,9,4], [45,84,25]]
matrixC=[]
for row in range(len(matrixA)):
    new_row=[]
    for columna in range (len(matrixA[0])):
        new_row.append(matrixA[row][columna]+matrixB[row][columna])
    matrixC.append(new_row)

for row in range (len(matrixA)):
    if row != 1:
        print(f"{matrixA[row]}   {matrixB[row]}   {matrixC[row]}")
    else:
        print(f"{matrixA[row]} +  {matrixB[row]} =  {matrixC[row]}")




"""
matrix[1][2] #el primer corchete se refiere a las filas y el segundo a las columnas


print(f"{matrix[0]} \n{matrix[1]} \n{matrix[2]} ")

n= matrix[0]
b= matrix[1]
o= matrix[2]
"""




