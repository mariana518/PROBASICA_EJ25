#Verifica si un número es primo

a = int(input("Ingrese un número: "))
def es_primo(n):
    if n <= 1:
        return "No es primo"
    for i in range(2, int(n ** 0.5) + 1): 
        if n % i == 0:
            return "No es primo"
    return "Es primo"

print(es_primo(a))
    




