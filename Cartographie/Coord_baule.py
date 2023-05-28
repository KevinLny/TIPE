'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //                                                            //
//  27/05/2023                                                  //
///////////////////////////////////////////////////////////////'''

from math import radians, sin, cos, sqrt, atan2, degrees
import sqlite3
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

# Ouverture du document csv
f=open("./data/baie_de_la_baule_points.csv", 'rt', encoding='UTF8')
lecteurcsv = csv.DictReader(f,delimiter=",")

angle = 126.37584000008509


connect = sqlite3.connect('./data/BDD.db')
cur = connect.cursor()

for ligne in lecteurcsv:
    cur.execute("INSERT INTO 'main'.'Coord_baie' ('Latitude','Longitude','Distance', 'Angle') VALUES ('{}','{}','{}','{}')".format(ligne['Latitude'],ligne['Longitude'],distance(float(ligne['Latitude']),float(ligne['Longitude']),47.24563801228261, -2.387373826689938),angle))
    angle = angle - 0.00504318209832646

connect.commit()
connect .close()




