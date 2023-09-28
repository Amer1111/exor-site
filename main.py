from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


app.run(debug=False, host='0.0.0.0', port=8000)
