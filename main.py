from flask import Flask, request, url_for, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/alfa-romeo")
def alfa_romeo():
    return render_template("alfa-romeo.html")


if __name__ == "__main__":
    app.run(debug=True)
