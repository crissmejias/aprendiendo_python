class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self,monto):
        try:
            self.saldo += monto
            return f"Nuevo saldo: {self.saldo}"
        except TypeError:
            return None
    def retirar(self,monto):
        try:
            self.saldo -= monto
            return f"Nuevo saldo: {self.saldo}"
        except TypeError:
            return None