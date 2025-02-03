#ACTIVIDAD 4: Generar la secuencia de fibonacci hasta un número determinado de términos

def fibonacci_sequence(n, sequence):
    if n in sequence:
        return sequence[n]
    if n <= 0:
        return "Número inválido"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    sequence[n] = fibonacci_sequence(n - 1, sequence) + fibonacci_sequence(n - 2, sequence)
    return sequence[n]

    





