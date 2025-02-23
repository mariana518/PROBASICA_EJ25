#. Simular una cuenta bancaria con depósitos y retiros.

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        """Inicializa la cuenta bancaria con un saldo inicial."""
        self.saldo = saldo_inicial

    def depositar(self, monto):
        """Permite depositar una cantidad de dinero en la cuenta."""
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso de ${monto}. Saldo actual: ${self.saldo}")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        """Permite retirar una cantidad de dinero de la cuenta."""
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                print(f"Retiro exitoso de ${monto}. Saldo actual: ${self.saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser mayor que cero.")

    def consultar_saldo(self):
        """Muestra el saldo actual de la cuenta."""
        print(f"Saldo actual de la cuenta: ${self.saldo}")

# Crear una cuenta bancaria con un saldo inicial de $45000
mi_cuenta = CuentaBancaria(45000)

# Consultar saldo
mi_cuenta.consultar_saldo()

# Realizar depósitos y retiros
mi_cuenta.depositar(9000)  # Depósito de $9000
mi_cuenta.retirar(500)    # Retiro de $500
mi_cuenta.retirar(500000)   # Intentar retirar más de lo que hay en la cuenta

# Consultar saldo después de las operaciones
mi_cuenta.consultar_saldo()