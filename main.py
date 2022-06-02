from flask import Flask
from flask import render_template
from flask import url_for

app = Flask("Quiz")


@app.route("/")
def home():
    start_link = url_for("start")
    return render_template("index.html", link=start_link)


@app.route("/start")
def start():
    geografie_link = url_for("geografie")
    kunstkultur_link = url_for("kunstkultur")
    bücherfilmeserien_link = url_for("bücherfilmeserien")
    return render_template("start.html", link=geografie_link, links=kunstkultur_link, linkss=bücherfilmeserien_link)

@app.route("/goegrafie")
def geografie():
    return render_template("geografie.html")

@app.route("/kunstkultur")
def kunstkultur():
    return render_template("kunstkultur.html")

@app.route("/bücherfilmeserien")
def bücherfilmeserien():
    return render_template("bücherfilmeserien.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
