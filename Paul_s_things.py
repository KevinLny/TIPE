# Vitesse du vent et sa direction
vent_reel = (41.16, 300.0)

# Tableau des distances entre le point que j'ai choisi et les evens et l'angle entre le point et l'ile
distance_evens_baie = [(4.21, 40.31), (4.14, 20.01), (4.03, 5.71), (3.92, 4.10), (3.82, 23.14), (3.73, 57.94)]

# J'ai juste gardé les angles entre mes 6 points et l'ile mais ca sert un peu a rien
vent_vitesse = [40.31, 20.01, 5.71, 4.10, 23.14, 57.94]

# Il faut faire un modulo 380 si jamais la somme des deux angles est superieure a 360
# En gros ca te renvoie la direction du vent apparent, c'est a dire le vent qu'on doit prendre en compte
def vent_apparent():
    v = [(0, 0.0)] * len(distance_evens_baie)
    for i in range(len(distance_evens_baie)):
        direction = (vent_reel[1] + vent_vitesse[i]) % 360.0
        v[i] = (i, direction)
    return v

# La c'est un peu du pif faut que je revois la fonction mais deja tu peux t'en servir
def trajectoire():
    point_depart = 0
    angle_opti = 360.0
    for i in range(len(vent_apparent())):
        if vent_apparent()[i][1] <= angle_opti:
            angle_opti = vent_apparent()[i][1]
            point_depart = vent_apparent()[i][0]
    return point_depart
