from events import get_events

country = "Australia"
city = "Sydney"
start_date = "2023-05-01"
end_date = "2023-05-10"

event_list = get_events(country, city, start_date, end_date)

print(event_list[0].name)