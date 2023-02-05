from flask import Flask, render_template, redirect, request
from events import events, get_weather, get_sun

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/results",methods=["GET", "POST"])
def results():
	if request.method == "POST":

		# Get form data
		country = request.form["country"]
		city = request.form["city"]
		start_date = request.form["start-date"]
		end_date = request.form["end-date"]

		# Get API results
		event_list = events.get_events(country, city, start_date, end_date)
		hotel_list = events.get_hotels(city, start_date, end_date)
		safety_check = events.get_safety(country)
		weather = get_weather(city, start_date, end_date)
		sun = get_sun(city)

		# Render template
		return render_template("results.html",
							country=country,
							city=city,
							events=event_list,
							hotels=hotel_list,
							start_date=start_date,
							end_date=end_date,
							safety=safety_check,
							weather=weather,
							sun=sun)

	else:
		return redirect("/", code=302)


@app.route("/events",methods=["GET", "POST"])
def event_page():

	# NOTE: These values are hard coded because we ran out of time. In a
	# production build these would be the same as the page the user came from
	country = "Australia"
	city = "Sydney"
	start_date = "2023-04-01"
	end_date = "2023-04-15"

	# Get API results
	event_list = events.get_events(country, city, start_date, end_date)

	# Render template
	return render_template("events.html",
							country=country,
							city=city,
							events=event_list,
							start_date=start_date,
							end_date=end_date)

@app.route("/hotels",methods=["GET", "POST"])
def hotel_page():

	# NOTE: These values are hard coded because we ran out of time. In a
	# production build these would be the same as the page the user came from
	country = "Australia"
	city = "Sydney"
	start_date = "2023-04-01"
	end_date = "2023-04-15"

	# Get API results
	hotel_list = events.get_hotels(city, start_date, end_date)

	# Render template
	return render_template("hotels.html",
							country=country,
							city=city,
							hotels=hotel_list,
							start_date=start_date,
							end_date=end_date)