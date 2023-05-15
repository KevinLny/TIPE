import folium

# Coordonnées de la carte centrée sur Paris
lat = 47.26
lon = -2.385

# Création de la carte
ma_carte = folium.Map(location=[lat, lon], zoom_start=13)

# Coordonnées de la tour Eiffel et de l'Arc de Triomphe
point_de_depart = [47.274733, -2.361031]
point_d_arrive = [47.24563801228261, -2.387373826689938]

# Ajout d'un marqueur sur le point de départ
folium.Marker(location=point_de_depart, tooltip='Le départ !').add_to(ma_carte)

# Ajout d'un marqueur sur l'arrivé
folium.Marker(location=point_d_arrive, tooltip="L'arrivé !").add_to(ma_carte)

# Ajout du chemin entre le départ et l'arrivé
folium.PolyLine(locations=[point_de_depart, point_d_arrive], color='red', weight=5).add_to(ma_carte)

# Enregistrement de la carte dans un fichier HTML
ma_carte.save('ma_carte.html')