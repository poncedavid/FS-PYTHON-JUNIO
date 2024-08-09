class CuentaBancaria:
    #Arreglo vacio de las cuentas.
    cuentas = []

    #Constructor de la clase.
    def __init__(self,tasa_inteseres,balance):
        self.tasa_interes=tasa_inteseres
        self.balance=balance
        CuentaBancaria.cuentas.append(self)


    #Metodos de instancia.
    def deposito(self,monto):
        #Aumenta el balance de la cuenta.
        self.balance += monto
        #Retorna el objeto.
        return self
    
    def retirar(self,monto):
        if(self.balance - monto ) > 0:
            self.balance -= monto
        else:
            print(f"Fondos insuficientes: su monto es de ${self.balance}")

        return self

    def mostrar_balance(self):
        print(f"Su balance es de ${self.balance}")
        return self


    def generar_intereses(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes
        else:
            print("No se puede generar intereses con saldo negativo")

    @classmethod
    def imprimr_todas_las_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_balance()



class Usuario:

    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.cuentas = {
            "cuenta_corriente": CuentaBancaria(.02,0),
            "cuenta_ahorros": CuentaBancaria(.05,0)
        }


    def mostras_balance_usuario(self):
        print(f"{self.email} tiene un balance en su cuenta corriente  de: ${self.cuentas['cuenta_corriente'].balance}")
        print(f"{self.email} tiene un balance en su cuenta de ahorros de: ${self.cuentas['cuenta_ahorros'].balance}")



juan = Usuario("Juan","Juan@gmail.com")

print(juan.email)

juan.cuentas["cuenta_corriente"].deposito(1000)
juan.cuentas["cuenta_ahorros"].deposito(9)


juan.mostras_balance_usuario()

# #Instancias de la clase.
# cuentaGold = CuentaBancaria(.05,0)
# cuentaSilver = CuentaBancaria(.02,50)
# cuentaBronce = CuentaBancaria(.01,15675670)
# cuentaBronce1 = CuentaBancaria(.01,10)
# cuentaBronce2 = CuentaBancaria(.01,1077)
# cuentaBronce3 = CuentaBancaria(.01,105767)
# cuentaBronce4 = CuentaBancaria(.01,1675675670)
# cuentaBronce5 = CuentaBancaria(.01,105675675)

# #Metodos de instancia.
# cuentaGold.deposito(1000).deposito(1000).deposito(1000).retirar(500)


# CuentaBancaria.imprimr_todas_las_cuentas()


