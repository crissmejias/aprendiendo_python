class CuentaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo =  saldo
        
    def ver_saldo(self):
        return self.__saldo
    
cuenta1 = CuentaBancaria("Criss",2000)

print(cuenta1.__saldo)
print(cuenta1.ver_saldo())