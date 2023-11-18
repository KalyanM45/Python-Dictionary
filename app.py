from flask import Flask, render_template, request
from PyDictionary import PyDictionary

app = Flask(__name__)
dictionary = PyDictionary()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/lookup", methods=["POST"])
def lookup():
    word = request.form["word"]
    meanings = dictionary.meaning(word)
    
    return render_template("home.html", word=word, meanings=meanings)

if __name__ == "__main__":
    app.run(debug=True)
