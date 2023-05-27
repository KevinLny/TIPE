'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //                                                            //
//  27/05/2023                                                  //
///////////////////////////////////////////////////////////////'''

from math import radians, sin, cos, sqrt, atan2
import csv

def distance(lat1, lon1, lat2, lon2):
    # Conversion des degrés en radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Rayon de la Terre en kilomètres
    radius = 6371.0

    # Différence des longitudes et des latitudes
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Formule de la distance entre deux points sur une sphère, formule de Haversine
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Distance en kilomètres
    distance_km = radius * c

    return distance_km

from math import atan2, degrees

def angle(lat, lon):
    # Conversion des degrés en radians
    lat1_rad = radians(lat)
    lon1_rad = radians(lon)
    lat2_rad = 47.24563801228261 
    lon2_rad = -2.387373826689938

    # Différence des longitudes et des latitudes
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Calcul de l'angle en radians
    angle_rad = atan2(dlat, dlon)

    # Conversion de l'angle en degrés
    angle_deg = degrees(angle_rad)

    # Correction pour obtenir un angle entre 0 et 360 degrés
    if angle_deg < 0:
        angle_deg += 360

    return angle_deg


# Ouverture du document csv
f=open("baie_de_la_baule_points.csv", 'rt', encoding='UTF8')
lecteurcsv = csv.DictReader(f,delimiter=",")

'''for ligne in lecteurcsv:
        print(ligne['Latitude'],ligne['Longitude'])'''

print(angle(47.27230090555682, -2.4248411258982414))




