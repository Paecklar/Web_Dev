from flask import Flask, render_template, request, redirect, url_for, make_response
from Lesson_18.user import User

app = Flask(__name__)

@app.route("/")
def index():
    email_address = request.cookies.get("User-email")

    if email_address:

    # get user from the database based on email address
        user = User.fetch_one(query=["email", "==", email_address])
    else:
        user=None

    return render_template("index.html", user=user)

@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")
    # create a User object
    user = User(name=name, email=email)
    user.create()  # save the object into a database

    response = make_response(redirect(url_for('index')))
    response.set_cookie("User-email", email)
    return response

@app.route("/logout")
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie("User-email", expires=0)
    return response

if __name__ == "__main__":
    app.debug = False
    app.run()
