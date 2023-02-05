class events():
	import json
	import requests

	def get_results(dict):
		index = 0
		resulting = []
		for x in dict['_embedded']['events']:
			new_dict = {"url": [], "imgurl": [], "name": [], "date": [], "price_min": [], "price_max": [], "time": []}
			new_dict["url"] = dict['_embedded']['events'][index]['url']
			new_dict["imgurl"] = dict['_embedded']['events'][index]['images'][3]['url']
			new_dict["name"] = dict['_embedded']['events'][index]['name']
			new_dict["date"] = dict['_embedded']['events'][index]['dates']['start']['localDate']
			try:
				new_dict["time"] = dict['_embedded']['events'][index]['dates']['start']['localTime']
			except: 
				new_dict["time"] = "N/A"
			try:
				new_dict["price_min"] = dict['_embedded']['events'][index]['priceRanges'][index]['min']
			except: 
				new_dict["price_min"] = "N/A"
			try:
				new_dict["price_max"] = dict['_embedded']['events'][index]['priceRanges'][index]['max']
			except:
				new_dict["price_max"] = "N/A"
			resulting.append(new_dict)
			index = index + 1
		return resulting
	
	def get_hotel_results(dict):
		index = 0
		resulting = []
		for x in dict['results']:
			new_dict = {"price": [], "name": [], "imgurl": [], "url": []}
			new_dict["url"] = dict['results'][index]['url']
			new_dict["price"] = dict['results'][index]['price']['rate']
			new_dict["name"] = dict['results'][index]['name']
			new_dict["imgurl"] = dict['results'][index]['hostThumbnail']
			resulting.append(new_dict)
			index = index + 1
		print(resulting)
		return resulting
	
  
	
	def get_safety(country):
		countryCode = events.parseCountry(country)
		formatString = "https://www.travel-advisory.info/api?countrycode=" + countryCode
		response = requests.get(formatString)
		x = response.json()
		value = x['data'][countryCode]['advisory']['score']
		value = round(value,1)
		safety_dict = {"message": x['data'][countryCode]['advisory']['message'], "value": value}
		return safety_dict
	
	def get_events(country, cities, start_date, end_date):
		countryCode = events.parseCountry(country)
		city = cities
		startDateTime = start_date
		startDateTime = startDateTime + "T01:00:00Z"
		endDateTime = end_date
		endDateTime = endDateTime + "T01:00:00Z"
		formatString = "https://app.ticketmaster.com/discovery/v2/events.json?"
		formatString = formatString + "countryCode=" +  countryCode + "&"
		formatString = formatString + "city=" + city + "&"
		formatString = formatString + "startDateTime=" + startDateTime + "&"
		formatString = formatString + "endDateTime=" + endDateTime + "&"
		formatString = formatString + "apikey=h7wv6UQtzgusLrY4AWUYQhdTrsRmGr59"
		response = requests.get(formatString)
		print(formatString)
		print(response.status_code)
		x = response.json()
		print(events.get_results(x))
		return events.get_results(x)
	
	def get_hotels(cities, start_date, end_date):
		url = "https://airbnb13.p.rapidapi.com/search-location"
		querystring = {"location":cities,"checkin":start_date,"checkout":end_date,"adults":"2","children":"0","infants":"0","page":"1"}
		headers = {
			"X-RapidAPI-Key": "18ed87ebeamsh15c980c94168d4dp163c32jsne320acf7c851",
			"X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		return events.get_hotel_results(response.json())

	
	def parseDate(dict):
		entireDate = dict["year"] + "-" + dict["month"] + "-" + dict["day"]
		return entireDate

	def parseCountry(country):
		match country:
			case "United States of America":
				return "US"
			case "United States":
				return "US"
			case "US":
				return "US"
			case "USA":
				return "US"
			case "U.S.":
				return "US"
			case "Anguilla":
				return "AI"
			case "Argentina":
				return "AR"
			case "Australia":
				return "AU"
			case "Austria":
				return "AT"
			case "Azerbaijan":
				return "AZ"
			case "Bahamas":
				return "BS"
			case "Bahrain":
				return "BH"
			case "Barbados":
				return "BB"
			case "Belgium":
				return "BE"
			case "Bermuda":
				return "BM"
			case "Brazil":
				return "BR"
			case "Bulgaria":
				return "BG"
			case "Canada":
				return "CA"
			case "Chile":
				return "CL"
			case "China":
				return "CN"
			case "Colombia":
				return "CO"
			case "Costa Rica":
				return "CR"
			case "Croatia":
				return "HR"
			case "Cyprus":
				return "CY"
			case "Czech Republic":
				return "CZ"
			case "Denmark":
				return "DK"
			case "Dominican Republic":
				return "DO"
			case "Ecuador":
				return "EC"
			case "Estonia":
				return "EE"
			case "Faroe Islands":
				return "FO"
			case "Finalnd":
				return "FI"
			case "France":
				return "FR"
			case "Georgia":
				return "GE"
			case "Germany":
				return "DE"
			case "Ghana":
				return "GH"
			case "Gibraltar":
				return "GI"
			case "Great Britain":
				return "GB"
			case "Greece":
				return "GR"
			case "Hong Kong":
				return "HK"
			case "Hungary":
				return "HU"
			case "Iceland":
				return "IS"
			case "India":
				return "IN"
			case "Ireland":
				return "IE"
			case "Israel":
				return "IL"
			case "Italy":
				return "IT"
			case "Jamaica":
				return "JM"
			case "Japan":
				return "JP"
			case "Korea":
				return "KR"
			case "South Korea":
				return "KR"
			case "Republic of Korea":
				return "KR"
			case "Latvia":
				return "LB"
			case "Lebanon":
				return "LB"
			case "Lithuania":
				return "LT"
			case "Luxembourg":
				return "LU"
			case "Malaysia":
				return "MY"
			case "Malta":
				return "MT"
			case "Mexico":
				return "MX"
			case "Monaco":
				return "MC"
			case "Montenegro":
				return "ME"
			case "Morocco":
				return "MA"
			case "Netherlands":
				return "NL"
			case "Netherlands Antilles":
				return "AN"
			case "New Zealand":
				return "NZ"
			case "North Ireland":
				return "ND"
			case "Norway":
				return "NO"
			case "Peru":
				return "PE"
			case "Poland":
				return "PL"
			case "Portugal":
				return "PT"
			case "Romania":
				return "RO"
			case "Russia":
				return "RU"
			case "Russian Federation":
				return "RU"
			case "Saint Lucia":
				return "LC"
			case "Saudi Arabia":
				return "SA"
			case "Serbia":
				return "RS"
			case "Singapore":
				return "SG"
			case "Slovakia":
				return "SK"
			case "Slovenia":
				return "SI"
			case "South Africa":
				return "ZA"
			case "Spain":
				return "ES"
			case "Sweden":
				return "SE"
			case "Switzerland":
				return "CH"
			case "Taiwan":
				return "TW"
			case "Thailand":
				return "TH"
			case "Trinidad":
				return "TT"
			case "Tobago":
				return "TT"
			case "Turkey":
				return "TR"
			case "Ukraine":
				return "UA"
			case "United Arab Emirates":
				return "AE"
			case "Uruguay":
				return "UY"
			case "Venezuela":
				return "VE"
			case _:
				print("Events for this country are not available.")
				return "US"
import requests
import json        

import requests

def get_weather(city, start_date, end_date):
		# To Generate coordinates for an input city
		from geopy.geocoders import Nominatim 

		# Import Meteostat library and dependencies
		from datetime import datetime
		import matplotlib.pyplot as plt
		from meteostat import Stations, Monthly
		from meteostat import Point, Daily

		geolocator = Nominatim(user_agent = "Your_Name")
		location = geolocator.geocode(city)
		print('\nPrinting City, Longitude, and latitude:')
		print(location.address)
		print((location.latitude, location.longitude))

		# Parses date for input into the datetime() function
		sm = start_date[5:7:1]  # start month
		sd = start_date[8:10:1] # start day
		em = end_date[5:7:1]    # end month
		ed = end_date[8:10:1]   # end day

		if (int(sm) < 10):
			sm = sm[1:2:1]

		if (int(sd) < 10):
			sd = sd[1:2:1]

		if (int(em) < 10):
			em = em[1:2:1]

		if (int(ed) < 10):
			ed = ed[1:2:1]

		# Create a point based on the coordinates of the city and 
		# fetch the weather data for that city

		start = datetime(2022, int(sm), int(sd))
		end = datetime(2022, int(em), int(ed))
		cityWeather = Point(location.latitude, location.longitude)
		data = Daily(cityWeather, start, end)
		data = data.fetch()

		# Isolate the average temperature and return it
		tavgData = data.tavg
		tavgList = tavgData.to_dict()
		tAvgFinalList = tavgList.values()
		SUMT = sum(list(tAvgFinalList))
		AVGT = SUMT / (len(list(tAvgFinalList)))
		print('\nAverage Temperature in Fahrenheit:')
		AVGT = round(((AVGT * 1.8) + 32), 2) # Celsius to Fahrenheit conversion
		avgtString = (str(AVGT) + ' degrees Fahrenheit')
		print(avgtString)

		# Isolate the average precipitation and return it
		prcpData = data.prcp
		prcpList = prcpData.to_dict()
		prcpFinalList = prcpList.values()
		SUMP = sum(list(prcpFinalList))
		AVGP = SUMP / (len(list(prcpFinalList)))
		print('\nAverage Precipitation in inches:')
		AVGP = round((AVGP * 0.0393), 2) # mm to inches conversion
		pcrpString = (str(AVGP) + ' inches')
		print(pcrpString)
		return_dict = {"avgTemp": AVGT, "avgPrcp": AVGP}
		return return_dict


def get_sun(city):
	from geopy.geocoders import Nominatim

	address=city
	geolocator = Nominatim(user_agent="Your_Name")
	location = geolocator.geocode(address)
	url = "https://api.sunrise-sunset.org/json?lat=" + str(location.latitude) + "&lng=" + str(location.longitude)
	response = requests.get(url)
	x = response.json()
	response1 = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key=35MGEOLVEU3G&format=json&by=position&lat=" + str(location.latitude) + "&lng=" + str(location.longitude))
	y = response1.json()
	time_change = y['gmtOffset']
	time_change = int(time_change)
	time_change = time_change / 3600
	sunset = x['results']['sunset']
	sunset = sunset.split(" ")
	holder = sunset[0].split(":")
	sunset = sunset[0].split(":")
	holder[0] = int(holder[0])
	if (holder[0] + time_change < 0):
		holder[0] = holder[0] + 12
	if (holder[0] + time_change > 12):
		holder[0] = holder[0] - 12
	holder[0] = int(holder[0] + time_change)
	sunrise = x['results']['sunrise']
	sunrise = sunrise.split(" ")
	sunrise = sunrise[0]
	holder1 = sunrise.split(":")
	sunrise = sunrise.split(":")
	holder1[0] = int(holder1[0])
	if (holder1[0] + time_change < 0):
		holder1[0] = holder1[0] + 12
	if (holder1[0] + time_change > 12):
		holder1[0] = holder1[0] - 12
	holder1[0] = int(holder1[0] + time_change)
	new_sunrise = str(holder1[0]) + ":" + sunrise[1] + ":" + sunrise[2] + " AM"
	new_sunset = str(holder[0]) + ":" + sunset[1] + ":" + sunset[2] + " PM"
	return_dict = {"sunrise": new_sunrise, "sunset": new_sunset}
	return return_dict