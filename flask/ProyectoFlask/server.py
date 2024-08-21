from flask import Flask, render_template # Importando la clase Flask

app = Flask(__name__) # Creando una instancia de la clase Flask

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/usuario")
def usuario():
    return render_template("/usuario/home.html")


@app.route("/contacto")
def contacto():
    return render_template("/contact.html")


@app.route("/login")
def login():
    return render_template("/login/login.html")



if __name__ == '__main__':
    app.run(debug=True) # Ejecutando el servidor en modo debug