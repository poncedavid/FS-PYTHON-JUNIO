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


pcTrabajo = Laptop("Macbook Pro","Apple")
pcCasa = Laptop("Asus","Asus")

pcCasa.informacionEquipo()

pcTrabajo.informacionEquipo()




