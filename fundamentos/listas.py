#Esta es una lista vacia
lista = []

#Metodo Append para agregar elementos a la lista
lista.append("Hola mundo")
lista.append("Chao mundo")

#Metodos Insert para agregar elementos en una posicion especifica
lista.insert(0,"CodingDojo")

# Metodo Extends para agregar varios elementos a la lista
lista_uno = [1,2,3,4,5,44,44,44,44]
lista_dos = [6,7,8,9,10,44]

lista.extend(lista_uno)
lista.extend(lista_dos)


#Metodo Remove para eliminar un elemento de la lista
lista.remove("Coding Dojo")

#Metodo Pop para eliminar un elemento de la lista por su indice
lista.pop(2)

#Metodo Index para buscar un elemento en la lista
ubicado = lista.index("Coding Dojo")

#Metodo Count para contar cuantas veces se repite un elemento en la lista
repetido = lista.count(44)

#Metodo Sort para ordenar la lista
listaDeNuneros = [2000006,12,44,6,0,1,1000]
listaDeNuneros.sort()


#Metodo Len para saber la longitud de la lista
longitud = len(listaDeNuneros)
# print(F"El largo de la lista es {longitud}")

listaVacia=[]

def agregarElemento(elemento):
    listaVacia.append(elemento)
    return listaVacia

agregarElemento("HolaMundo")
agregarElemento("HolaMundo")
agregarElemento("HolaMundo")
agregarElemento("HolaMundo")
agregarElemento("HolaMundo")

print(listaVacia)