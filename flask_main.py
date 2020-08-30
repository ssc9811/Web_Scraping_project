from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return render_template("home.html")

app.run(host="127.0.0.1")