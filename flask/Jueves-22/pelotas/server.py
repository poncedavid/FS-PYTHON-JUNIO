from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/juego")
def juego():
    return render_template("pelotas.html", cantidad=3, color="red")


@app.route("/juego/<int:cantidad>")
def juego_x(cantidad):
    return render_template("pelotas.html", cantidad=cantidad, color="red")


@app.route("/juego/<int:cantidad>/<color>")
def juego_x_color(cantidad, color):
    return render_template("pelotas.html", cantidad=cantidad, color=color)


if __name__ == "__main__":
    app.run(debug=True)
