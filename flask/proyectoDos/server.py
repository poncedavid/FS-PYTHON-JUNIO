from flask import Flask # Importando la clase Flask
from flask import render_template # Importando la funcion render_template






app = Flask(__name__) # Creando una instancia de la clase Flask


#Para la creacion de las rutas.

@app.route("/")
def index():
    return "<h1>Hola Mundo</h1> <p>Este es un parrafo</p> <h2> Chao mundo</h2>"


@app.route("/adios")
def adios():
    return "Adios Mundo"


@app.route("/saludo")
def saludo():
    return "Saludo Mundo"

@app.route("/saludo/<nombre>")
def saludar(nombre):
    return f"Hola {nombre}"


@app.route("/saludo/<nombre>/<apellido>")
def saludoCompleto(nombre,apellido):
    return f"Hola {nombre} {apellido}"


@app.route("/bienvenida/<nombre>/<apellido>")
def bienvenida(nombre,apellido):
    return render_template("index.html", nombre=nombre,apellido=apellido)


if __name__ == '__main__':
    app.run(debug=True) # Ejecutando el servidor en modo debug