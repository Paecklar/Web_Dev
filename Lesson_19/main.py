from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    page_title = "Homepage"

    cities = ["Wien", "Prag", "Bratislava", "London"]

    return render_template("index.html", page_title=page_title, cities=cities)


@app.route("/impressum")
def impressum():
    return render_template("impressum.html")


if __name__ == "__main__":
    #app.debug = False
    app.run()
