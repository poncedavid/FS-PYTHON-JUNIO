class CuentaBancaria:

    cuentas = []
    #Constructor
    def __init__(self,tasa_inteser,balance):
        self.tasa_interes=tasa_inteser
        self.balance=balance
        CuentaBancaria.cuentas.append(self)

    #Metodos de la instancia
    def deposito(self,cantidad):
        #Sumamos la cantidad al balance
        self.balance += cantidad
        return self
    
    #Metodo de la instancia
    def retiro(self,cantidad):
        #Validando que balance no sea cero.
        if(self.balance - cantidad) > 0:
            self.balance -= cantidad
        else:
            print("No tienes suficiente dinero en tu cuenta")
        return self


    #Metodo de la instancia
    def mostrar_info_cuenta(self):
        print(f"El balance de la cuenta es: {self.balance}")

        return self
    



    def generar_intereses(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes

        return self
    
    #Metodo de la clase
    @classmethod
    def imprimir_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.
        return cls

#Instanciando la clase (Creando un objeto)

cuentaGold = CuentaBancaria(.05,10000)
cuentaSilver = CuentaBancaria(.03,200)
cuentaBronze = CuentaBancaria(.01,30)




CuentaBancaria.imprimir_cuentas()