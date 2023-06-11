'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //                                                            //
//  27/05/2023                                                  //
///////////////////////////////////////////////////////////////'''

import folium
import sqlite3
from jinja2 import Template

#//////////////////////////////////////////////////////////////////
#//                                                              //      
#//                     LES DONNEES                              //
#//                                                              //
#//////////////////////////////////////////////////////////////////

# Connexion à la base de données
connect = sqlite3.connect('./data/BDD.db')

# Création d'un curseur pour exécuter des requêtes
cur = connect.cursor()

#//////////////////////////////////////////////////////////////////
#//                                                              //      
#//                  CREATION DE LA CARTE                        //
#//                                                              //
#//////////////////////////////////////////////////////////////////


# Coordonnées de la carte centrée sur La Baule
lat = 47.264
lon = -2.385

def arrondi_dizaine(nombre):
    dizaine_superieure = (nombre // 10) * 10
    return dizaine_superieure

def rosace(winddeg):
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
    if(winddeg >= 315 and winddeg < 360):
        return 315
    

def make_map(windspeed, winddeg):
    
    # Recolte de donnée
    poid = int(input("Quel est votre poid ?"))
    poid = arrondi_dizaine(poid)
    if (poid > 90):
        poid = 90.1
    if (poid < 60):
        poid = 60
        print("Attention au petit poid !")
    
    cur.execute("SELECT Voile1,Voile2 FROM Planche_a_voile WHERE Poids = '{}' and Vent >= '{}'".format(poid, int(windspeed)))
    data_voile = cur.fetchall()

    #print(windspeed)
    #print(data_voile)

    # Donnée de la voile pour sa taille en fonction du poid et du vent
    voile = "Entre {} et {} m²".format(data_voile[0][0],data_voile[0][1])

    # Donné de la direction du vent en fonction du degré du vent

    image = "<img src= image/{}°.png>".format(rosace(winddeg))

    # Création de la carte
    ma_carte = folium.Map(location=[lat, lon], zoom_start=13)

    # Coordonnées prise en fonctions des paramètres du vent et de son orientation
    point_de_depart = [47.28048,-2.403553000000001]
    point_d_arrive = [47.24563801228261, -2.387373826689938]

    # Ajout d'un marqueur sur le point de départ
    folium.Marker(location=point_de_depart, tooltip='Le départ !').add_to(ma_carte)

    # Ajout d'un marqueur sur l'arrivé
    folium.Marker(location=point_d_arrive, tooltip="L'arrivé !").add_to(ma_carte)

    # Ajout du chemin entre le départ et l'arrivé
    folium.PolyLine(locations=[point_de_depart, point_d_arrive], color='red', weight=5).add_to(ma_carte)

    # Données à afficher dans l'encadré
    data = {
        'Vitesse du vent': str(windspeed) + ' m/s',
        'Orientation du vent': str(winddeg) + '°',
        'Taille de la voile ': voile,
        'Distance': 'Valeur 3',
        '': image,
    }
    
    # Création de l'encadré
    html_template = '''
    <div style="border: 4px solid black; background-color: white; padding: 40px;">
        <h4>Données</h4>
        <ul>
            {% for key, value in data.items() %}
            <B>{{ key }}</B>: <br><center>{{ value }}</center></br>
            {% endfor %}
        </ul>
    </div>
    '''

    # Formatage de la chaîne HTML avec les données
    template = Template(html_template)
    formatted_html = template.render(data=data)

    # Ajouter l'encadré à la carte
    folium.Marker([47.235536057291405, -2.4741868229542208], popup=folium.Popup(formatted_html)).add_to(ma_carte)


    # Enregistrement de la carte dans un fichier HTML
    ma_carte.save('ma_carte.html')