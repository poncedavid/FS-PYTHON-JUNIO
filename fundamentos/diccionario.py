#Los diccionarios estan compuestos por claves y valores. Siempre la clave va entre comillas.
mi_diccionario = {
    "claveUno":True,
    "claveDos":2024,
    "claveTres":"Hola",
    "claveCuatro":20.1
}

#Para acceder a un valor de un diccionario se puede hacer de dos formas
valorClave = mi_diccionario.get("claveDos")
valor_clave = mi_diccionario["claveCuatro"]


#Para mostrar solamente las claves del diccionarios keys()

clavesDelDiccionario = mi_diccionario.keys()


#Para mostrar solamente los valores del diccionario values()
valoresDelDiccionario = mi_diccionario.values()

#Para actualizar el diccionario es Update()

# print(f"sin updated: {mi_diccionario}")

mi_diccionario.update(
    {
        "claveUno": 1,
        "claveDos": 2,
        "claveTres": 3,
        "claveCuatro": 4
    }

)

# print(f"con updated: {mi_diccionario}")

#Para eliminar un elemento del diccionario se usa pop()

mi_diccionario.pop("claveCuatro")


print(mi_diccionario)


#Para limpiar el diccionario se usa clear()
mi_diccionario.clear()

print(mi_diccionario)