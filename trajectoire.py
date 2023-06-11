'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //
//  11/06/2023                                                  //
///////////////////////////////////////////////////////////////'''

from creer_carte import*
from meteo import*
import sqlite3


# Connexion à la base de données
connect = sqlite3.connect('./data/BDD.db')

# Création d'un curseur pour exécuter des requêtes
cur = connect.cursor()
cur.execute("SELECT * FROM Coord_baie WHERE Angle <21")
element = cur.fetchall()
print(element)