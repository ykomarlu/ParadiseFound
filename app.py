from flask import Flask, render_template, redirect, request
import events

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/results",methods=["POST"])
def draft():
	if request.method == "POST":

		# Get form data
		country = request.form["country"]
		city = request.form["city"]
		start_date = request.form["start-date"]
		end_date = request.form["end-date"]

		# Get API results
		event_list = events.get_events(country, city, start_date, end_date)

		# Print form data (For debugging)
		print(f"country: {country}")
		print(f"city: {city}")
		print(f"start_date: {start_date}")
		print(f"end_date: {end_date}")

		# Render template
		return render_template("results.html", country=country, city=city, events=event_list)

	else:
		return redirect("/", code=302)