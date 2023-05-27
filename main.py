'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //                                                            //
//  27/05/2023                                                  //
///////////////////////////////////////////////////////////////'''

import sqlite3
from creer_carte import*
from meteo import*

# Connexion à la base de données
connect = sqlite3.connect('BDD.db')

# Création d'un curseur pour exécuter des requêtes
cur = connect.cursor()

# Demande de données

#poid = input("Quel est votre poid ?")


# Récolte de données dans les tables
data_coord = cur.execute("")
#data_voile = cur.execute("SELECT Voile1,Voile2 FROM Planche_a_voile WHERE Poids = {} AND Vent = {}".format(poid, wind_speed))

# Propose la planche adapté en fonction du vent et du poids




# Créer la carte
make_map(wind_speed,wind_deg)


# Fermer la connexion à la base de données
connect .close()
