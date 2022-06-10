from flask import Flask
from flask import render_template
from flask import url_for, request
import json


app = Flask("Quiz")

@app.route("/")
def home():
    start_link = url_for("start")
    return render_template("index.html", link=start_link)


@app.route("/start", methods=["GET", "POST"])
def start():

    return render_template("start.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():

    try:
        q = open("datenbank.json")
        quizdatenbank = json.load(q)
    except FileNotFoundError:
        quizdatenbank = []

    for element in quizdatenbank:
        print(element)

    with open("datenbank.json", "w") as d:
        json.dump(quizdatenbank, d, indent=4, separators=(",", ":"))

    return render_template("quiz.html")

@app.route("/auswertung", methods=["GET", "POST"])
def auswertung():

    return render_template("auswertung.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
