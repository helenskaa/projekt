from flask import Flask
from flask import render_template
from flask import url_for, request
import json


app = Flask("Quiz")

# Home Seite mit Verlinkung zur Startseite
@app.route("/")
def home():
    start_link = url_for("start")
    return render_template("index.html", link=start_link)

# Startseite mit Verbindung zur Quizhistorie, damit die Daten bei der Ausführung dort übernommen werden
@app.route("/start", methods=["GET", "POST"])
def start():
    try:
        h = open("quizhistorie.json")
        quizhistorie = json.load(h)
    except FileNotFoundError:
        quizhistorie = []

# Kategorie Auswahl erstellt, 'global' damit die Variable 'kategorie_input' auf allen Seiten funktioniert.
    if request.method == "POST":
        global kategorie_input
        kategorie_input = request.form["kategorie"]
        # Bei der Quizhistorie werden bei der Ausführung der Name, Kategorie und die erreichte Punkte übertragen
        quizhistorie.append({"Name": request.form["benutzername"], "Kategorie": kategorie_input, "Punkte": 0})

    with open("quizhistorie.json", "w") as d:
        json.dump(quizhistorie, d, indent=4, separators=(",", ":"))

    return render_template("start.html")

# Quizseite, die Fragen werden von der datenbank.json übernommen
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

# Wenn Frage richtig beantwortet wurde, wird ein Punkt hinzugefügt.
    # POST --> Wenn Knopf 'Antworten eintragen' gedrückt wird am Ende des Quiz
    if request.method == "POST":
        for element in quizdatenbank:
            if element["Kategorie"] == kategorie_input:
                if request.form[element["Frage"]] == element["richtigeAntwort"]:
                    element["punkte"] = 1

    with open("datenbank.json", "w") as d:
        json.dump(quizdatenbank, d, indent=4, separators=(",", ":"))

    return render_template("quiz.html", liste_fragen=liste_fragen, kategorie=kategorie_input)

# Auswertungsseite: Punkte, Maximalpunkte und die Fragen werden angezeigt
@app.route("/auswertung", methods=["GET", "POST"])
def auswertung():
    punkte = 0
    maximalpunkte = 0
    richtige_fragen = []
    falsche_fragen = []
    quizhistorie_html = []
    try:
        q = open("datenbank.json")
        quizdatenbank = json.load(q)
    except FileNotFoundError:
        quizdatenbank = []

    try:
        h = open("quizhistorie.json")
        quizhistorie = json.load(h)
    except FileNotFoundError:
        quizhistorie = []

    # Fragen, richtige Antwort werden der zugehörigen Liste hinzugefügt und Punkte zusammengerechnet
    for element in quizdatenbank:
        if element["Kategorie"] == kategorie_input:
            punkte = punkte + element["punkte"]
            if element["punkte"] == 1:
                richtige_fragen.append(element["Frage"])
            else:
                falsche_fragen.append([element["Frage"], element["richtigeAntwort"]])
            maximalpunkte = maximalpunkte + 1

    #Holt letztes Element von JSON, habe ich von https://www.autoscripts.net/get-last-element-of-dictionary-python/
    quizhistorie[-1]["Punkte"] = punkte

# Name, Kategorie und Punkte werden bei der Quizhistorie hinzugefügt
    for element in quizhistorie:
        quizhistorie_html.append([element["Name"], element["Kategorie"], element["Punkte"]])

    with open("quizhistorie.json", "w") as d:
        json.dump(quizhistorie, d, indent=4, separators=(",", ":"))

    return render_template("auswertung.html", punkte=punkte, maximalpunkte=maximalpunkte, falsche_fragen=falsche_fragen, richtige_fragen=richtige_fragen, quizhistorie_html=quizhistorie_html)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
