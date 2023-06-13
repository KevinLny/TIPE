'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //
//  27/05/2023                                                  //
///////////////////////////////////////////////////////////////'''

import requests

city_name = "Baule"
language = "fr"
clef = "e390b048d4f4d1e00adf7da19dd55613"
api_lien = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang={language}&appid={clef}"    

json = requests.get(api_lien).json()

# Vitesse du vent
wind_speed = json["wind"]["speed"]

# Orientation du vent
wind_deg = json["wind"]["deg"]


def convertion(data):
    return (data * 3.6)

wind_speedbis = convertion(float(wind_speed))

print(wind_speed, "m/s")
print(wind_speedbis ,"km/h")
print("Direction du vent",wind_deg,"°")