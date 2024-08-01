'''
    Actualiza los valores en diccionarios y listas.
'''

'''
    Ejercicio 1
    Cambia el valor de 3 en matriz por 6. 
    Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

'''
matriz = [ [10, 15, 20], [3, 7, 14] ]

matriz = [ 
    #0
    [
        #0
        10,
        #1
        15,
        #2
        20],
    #1
    [
        #0
        3,
        #1
        7,
        #2
        14] ]

matriz[1][0]= "Coding Dojo"

# print(matriz)

matriz = [ [10, 15, 20], [3, 7, 14] ]

'''
    Ejericio 2.
    Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
'''

cantantes = [ 
    {
        "nombre": "Ricky Martin",
        "pais": "Puerto Rico"
     }, 
    {
        "nombre": "Chayanne",
        "pais": "Puerto Rico"
        } 
    
]

cantantes[0]["nombre"] ="Coding Dojo"
cantantes[1]["pais"] ="Latinoamerica"

# print(cantantes)

'''
    Ejercicio 3.
    En ciudades, cambia “Cancún” por “Monterrey”
'''

ciudades = {
    "Mexico": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

ciudades["Mexico"][2] = "Monterrey"
ciudades["Chile"][0] = "Rancagua"

print(ciudades)

'''
    Ejercicio 4.
    En las coordenadas, cambia el valor de “latitud” por 9.9355431
'''

coordenadas = [ {"latitud": 8.2588997, "longitud": -84.9399704} ]

coordenadas[0]["latitud"] = 9.9355431

print(coordenadas)