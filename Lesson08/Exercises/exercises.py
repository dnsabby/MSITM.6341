"""
Lesson 8 Exercises (No Answers): Flask + HTML
=============================================

This file is scaffold-only.
Implement each route as instructed.
"""

import os

from flask import Flask, redirect, render_template, request, url_for

os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, template_folder="Templates")


@app.route("/")
def home():
    """
    Exercise 0:
    TODO: Build a simple homepage with links to exercise routes.
    """
    return "<h1>TODO: Build Lesson 8 home page.</h1>"


@app.route("/hello/<name>")
def hello_user(name):
    """
    Exercise 1:
    TODO: Render dynamic greeting for `name`.
    """
    _ = name
    return "<h2>TODO: Implement Exercise 1 greeting route.</h2>"


@app.route("/info", methods=["GET", "POST"])
def user_info():
    """
    Exercise 2:
    TODO: Build form (GET) and submission response (POST).
    """
    if request.method == "POST":
        return "<h2>TODO: Display submitted form values.</h2>"
    return "<h2>TODO: Build Exercise 2 form page.</h2>"


@app.route("/table", methods=["GET", "POST"])
def multiplication_table():
    """
    Exercise 3:
    TODO: Build multiplication table form + result output.
    """
    if request.method == "POST":
        return "<h2>TODO: Show multiplication table result.</h2>"
    return "<h2>TODO: Build Exercise 3 input form.</h2>"


@app.route("/fruits")
def fruit_list():
    """
    Exercise 4:
    TODO: Pass backend fruit list into `Templates/ex1.html`.
    """
    fruits = []
    return render_template("ex1.html", fruits=fruits)


@app.route("/users")
def users_table():
    """
    Exercise 5:
    TODO: Render list of user dictionaries as HTML table.
    """
    return "<h2>TODO: Implement Exercise 5 users table.</h2>"


@app.route("/go-home")
def go_home():
    """
    Utility route for redirect practice.
    """
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
