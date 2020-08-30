from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    return render_template('report.html', word=word)

app.run(host="127.0.0.1")