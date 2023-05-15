import requests

city_name = input("mettre le nom de la ville :")
language = "fr"
clef = "e390b048d4f4d1e00adf7da19dd55613"
api_lien = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang={language}&appid={clef}"    

json = requests.get(api_lien).json()
JSON = json["wind"]["speed"]

def convertion(data):
    return (data * 10**-3)* 3600

test = float(JSON)
print(test)
print(convertion(test) ,"km/s")
