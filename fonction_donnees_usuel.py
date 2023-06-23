'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //
//  12/06/2023                                                  //
///////////////////////////////////////////////////////////////'''

from meteo_data import*
import sqlite3

#//////////////////////////////////////////////////////////////////
#//                                                              //      
#//                   Fonctions calculs                          //
#//                                                              //
#//////////////////////////////////////////////////////////////////

def arrondi_dizaine(nombre : int):
    """Détermine l'arrondi d'un nombre à la dizaine tout est dans le nom de la fonction

    Args:
        nombre (int): Le nombre que tu veux arrondir

    Returns:
        int: Le nombre arrondi à la dizaine près
    """
    dizaine_superieure = (nombre // 10) * 10
    return dizaine_superieure

def coefficient_porte_traine(winddeg, angle_planche):
    """Détermine le coefficient de porté et de trainé en fonction de l'orientation du vent
    et de l'orientation de la planche pour aller à l'île des Evens.

    Args:
        winddeg (float): Orientation du vent
        angle_planche (float): Orientation de la planche pour aller à l'île

    Returns:
        (float,float): coefficient de trainé et coefficient de porté
    """
    angle = abs(winddeg - angle_planche) % 90
    cp = 0.5
    ct = 0
    if(0 <= angle and angle < 5):
        cp,ct = (0.05,0.6)
    if(5 <= angle and angle < 10):
        cp,ct = (0.1,0.8)
    if(10 <= angle and angle < 15):
        cp,ct = (0.2,1)
    if(15 <= angle and angle < 20):
        cp,ct = (0.4,1.15)
    if(30 <= angle and angle < 25):
        cp,ct = (0.5,1.2)
    if(25 <= angle and angle < 30):
        cp,ct = (0.7,1.15)
    if(30 <= angle and angle < 40):
        cp,ct = (0.7,0.9)
    if(40 <= angle and angle < 50):
        cp,ct = (0.9,0.7)
    if(50 <= angle and angle < 60):
        cp,ct = (1,0.6)
    if(60 <= angle and angle < 70):
        cp,ct = (1.15,0.5)
    if(70 <= angle and angle < 80):
        cp,ct = (1.2,0.2)
    if(80 <= angle and angle <= 90):
        cp,ct = (1.3,0)
    return cp,ct

def rosace(winddeg : int):
    """Détermine l'orientation de la flèche sur la carte

    Args:
        winddeg (int): Orientation du vent

    Returns:
        int: L'orientation de la flèche sur la carte
    """
    if(winddeg >= 0 and winddeg < 45):
        return 0
    if(winddeg >= 45 and winddeg < 90):
        return 45
    if(winddeg >= 90 and winddeg < 135):
        return 90
    if(winddeg >= 135 and winddeg < 180):
        return 135
    if(winddeg >= 180 and winddeg < 225):
        return 180
    if(winddeg >= 225 and winddeg < 270):
        return 225
    if(winddeg >= 270 and winddeg < 315):
        return 270
    if(winddeg >= 315 and winddeg <= 360):
        return 315

#//////////////////////////////////////////////////////////////////
#//                                                              //      
#//                     LES DONNEES                              //
#//                                                              //
#//////////////////////////////////////////////////////////////////

# Récolte de données sur l'utilisateur
poid = int(input("Quel est votre poid ?"))
poid = arrondi_dizaine(poid)
if (poid > 90):
    poid = 90.1
if (poid < 60):
    poid = 60
    print("Attention au petit poid !")

# Connexion à la base de données
connect = sqlite3.connect('./data/BDD.db')

# Création d'un curseur pour exécuter des requêtes
cur = connect.cursor()

# Recolte de données
cur.execute("SELECT Voile1,Voile2 FROM Planche_a_voile WHERE Poids = '{}' and Vent >= '{}'".format(poid, int(wind_speed)))
data_voile = cur.fetchall()     # Données sur les voiles en fonction du poid

cur.execute("SELECT * FROM Coord_baie")
element = cur.fetchall()    # Toute les coordonnées 4-uplets (Latitude, Longitude, angle, distance (km))

