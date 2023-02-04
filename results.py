class test():
    def parseDate(dict):
        entireDate = dict.year + "-" + dict.month + "-" + dict.day
        return entireDate

    def parseCountry(country):
        match country:
            case "United States of America":
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

import requests
import json

# Country name to code converter function
# Date start converter function
# Date end converter function

# YOU NEED TO ADD VALUES HERE

a_dict1 = {'year': '2023', 'month': '05', 'day': '01'}
a_dict2 = {'year': '2023', 'month': '05', 'day': '10'}
countryCode = test.parseCountry("United States Of America")
city = ""
startDateTime = test.parseDate(a_dict1)
startDateTime = startDateTime + "T01:00:00Z"
endDateTime = test.parseDate(a_dict2)
endDateTime = endDateTime + "T01:00:00Z"

# Working Example: Events in sydney australia from may 1st to may 5th
# countryCode = "AU"
# city = "sydney"
# startDateTime = "2023-05-01"
# startDateTime = startDateTime + "T01:00:00Z"
# endDateTime = "2023-05-05"
# endDateTime = endDateTime + "T01:00:00Z"

formatString = "https://app.ticketmaster.com/discovery/v2/events.json?"
formatString = formatString + "countryCode=" +  countryCode + "&"
formatString = formatString + "city=" + city + "&"
formatString = formatString + "startDateTime=" + startDateTime + "&"
formatString = formatString + "endDateTime=" + endDateTime + "&"
formatString = formatString + "apikey=h7wv6UQtzgusLrY4AWUYQhdTrsRmGr59"

# response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?countryCode=AU&city=sydney&startDateTime=2023-05-01T01:00:00Z&endDateTime=2023-05-15T01:00:00Z&apikey=h7wv6UQtzgusLrY4AWUYQhdTrsRmGr59")
response = requests.get(formatString)
print(response.status_code)
print(response.json())

parameters = {
    "lat": 40.71,
    "lon": -74
}

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())


lang = input("What's the programming language you want to learn? ")