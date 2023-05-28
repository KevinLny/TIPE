'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //                                                            //
//  27/05/2023                                                  //
///////////////////////////////////////////////////////////////'''

import numpy as np
import pandas as pd

# Les limites géographiques de la Baie de La Baule
lat_max =  47.27599848411349
lat_min =  47.26199364389432
lon_max =  -2.3415423853609005
lon_min = -2.3504251728775216

# L'espacement souhaité entre les points
spacing = 0.0001

# Générer les coordonnées latitude/longitude
lats = np.arange(lat_min, lat_max, spacing)
lons = np.arange(lon_min, lon_max, spacing)

# Créer une grille de points en combinant les coordonnées latitude/longitude
points = np.array(np.meshgrid(lats, lons)).T.reshape(-1, 2)

# Convertir les coordonnées en DataFrame pour une utilisation facile
df = pd.DataFrame(points, columns=['Latitude', 'Longitude'])

# Enregistrer les données dans une base de données (par exemple, un fichier CSV)
df.to_csv('baie_de_la_baule_pointsbiq.csv', index=False)
