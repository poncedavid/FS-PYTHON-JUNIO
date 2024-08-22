from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", row= 8,col = 8, color_one="red", color_two="black")

@app.route("/<int:row>")
def row(row):
        return render_template("index.html", row= row,col = 8, color_one="red", color_two="black")

@app.route("/<int:row>/<int:col>")
def row_col(row,col):
        return render_template("index.html", row= row,col = col, color_one="red", color_two="black")

@app.route("/<int:row>/<int:col>/<color_one>")
def row_col_color_one(row,col,color_one):
        return render_template("index.html", row= row,col = col, color_one=color_one, color_two="black")

@app.route("/<int:row>/<int:col>/<color_one>/<color_two>")
def row_col_color_two(row,col,color_one,color_two):
        return render_template("index.html", row= row,col = col, color_one=color_one, color_two=color_two)



if __name__ == "__main__":
    app.run(debug=True)
