from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/results",methods=["POST"])
def draft():
	return render_template("results.html")