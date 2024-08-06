class Usuario:
# Estos son los atributos del objeto.
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        self.balance_cuenta=0


#Metodos del objeto
    def hacer_deposito(self,cantidad):
        self.balance_cuenta+=cantidad

    def hacer_retiro(self,cantidad):
        self.balance_cuenta-=cantidad










class Automovil:

    def __init__(self,marca,modelo,anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio
        self.kilometraje=0


dojo = Usuario("Coding Dojo","dojo@coding.cl",5)


print(dojo.balance_cuenta)

dojo.hacer_deposito(2000)

print(dojo.balance_cuenta)

dojo.hacer_retiro(500)

print(dojo.balance_cuenta)