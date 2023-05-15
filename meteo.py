import requests

city_name = input("mettre le nom de la ville :")
language = "fr"
clef = "e390b048d4f4d1e00adf7da19dd55613"
api_lien = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang={language}&appid={clef}"    

json = requests.get(api_lien).json()
JSON_speed = json["wind"]["speed"]

JSON_deg = json["wind"]["deg"]


def convertion(data):
    return (data * 3.6)

test = float(JSON_speed)
print(convertion(test) ,"km/h")

print("Direction du vent",JSON_deg,"°")
