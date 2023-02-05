from events import events

country = "Australia"
city = "Sydney"
start_date = "2023-05-01"
end_date = "2023-05-10"

hotels = events.get_hotels(city, start_date, end_date)

print(hotels)