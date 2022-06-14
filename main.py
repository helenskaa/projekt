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
# Kategorie Auswahl erstellt, global damit die Variable auf allen Seiten funktioniert.
    if request.method == "POST":
        global kategorie_input
        kategorie_input = request.form["kategorie"]

    return render_template("start.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    liste_fragen = []

    try:
        q = open("datenbank.json")
        quizdatenbank = json.load(q)
    except FileNotFoundError:
        quizdatenbank = []

    for element in quizdatenbank:
        if element["Kategorie"] == kategorie_input:
            liste_fragen.append([element["Frage"], element["A"], element["B"], element["C"], element["D"]])

# Wenn Frage richtig beantwortet wurde, wird ein Punkt hinzugefügt. POST --> Wenn Knopf 'Antworten eintragen' gedrückt wird am Ende des Quiz
    if request.method == "POST":
        for element in quizdatenbank:
            if request.form[element["Frage"]] == element["richtigeAntwort"]:
                element["punkte"] = 1

    with open("datenbank.json", "w") as d:
        json.dump(quizdatenbank, d, indent=4, separators=(",", ":"))

    return render_template("quiz.html", liste_fragen=liste_fragen)

@app.route("/auswertung", methods=["GET", "POST"])
def auswertung():

    return render_template("auswertung.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
