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
        return x['data'][countryCode]['advisory']['message']
    
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
            "X-RapidAPI-Key": "964b3ffe3cmshb993c590a1c0aa1p19004cjsn2e413354a3b4",
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

