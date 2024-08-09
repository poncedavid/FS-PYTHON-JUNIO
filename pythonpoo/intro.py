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



class Laptop:

    def __init__(self,modelo,marca):
        self.modelo=modelo
        self.marca=marca


    def informacionEquipo(self):
        print(f"El equipo es {self.modelo} de la marca {self.marca}")














class Edificio:

    def __init__(self,altura,cantidad_deptos,direccion,vista_al_mar):
        self.altura=altura
        self.cantidad_deptos=cantidad_deptos
        self.direccion=direccion
        self.vista_al_mar=vista_al_mar


edificioUno = Edificio("20 metros",50,"Calle Falsa 123",False)
edificioDos = Edificio("30 metros",100,"Calle Falsa 124",True)



print(f"¿Edificio con vista al mar?:{edificioDos.vista_al_mar}")