from flask import Flask # Importamos flask para crear la aplicacion

app = Flask(__name__) # Creamos la aplicacion que se llama "app"

@app.route("/")
def hello():
    return "<h1>Hola Mundo</h1>" # Retornamos un string


@app.route("/adios")
def adios():
    return "<h1>Adios Mundo</h1>"

if __name__ == "__main__": # Si el archivo se ejecuta directamente
    app.run(debug=True) # Ejecutamos la aplicacion