#Calcule el interés compuesto dado una capital, tasa y tiempo 


def calcular_interes_compuesto(capital, tasa, tiempo):
   
    monto_final = capital * (1 + tasa / 100) ** tiempo
    return monto_final

capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés anual (%): "))
tiempo = int(input("Ingrese el tiempo en años: "))


monto = calcular_interes_compuesto(capital, tasa, tiempo)


print(f"\nEl monto final después de {tiempo} años será: ${monto:.2f}")

   