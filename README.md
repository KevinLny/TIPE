# TIPE

It's a project TIPE et on le fait à deux !
Le but de ce TIPE ? Donner le meilleur point de départ pour allé à l'île des Evins de la Baule. 
L'utilisateur qui fait de la planche à voile en sera ravi ! Mais pour ça étalons notre science !!!

Quelques api sur les cartes :
    - Premier problème, Shom api coutes 4500
    - Deuxième problème cartografier la carte (on évite en passant par une bibliothèque : folium)
    - https://openweathermap.org/current mail : kuzu9217@gmail.com / mdp : TIPEwithPaul
    - Troisième problème : Créer un encadré des données avec folium 

Quelque info pour la BDD :
    - Faire un nouvel enregistrement : INSERT INTO "main"."Coord_baie"
                                                ("Distance", "Angle")
                                                VALUES ('30', '20');
    
    - Deux tables créée pour les coordonnées de la baie et de la Planche
    - Créer la distance facile la formule de formule de Haversine qui permet de calculer la distance de 2 point
      de la terre du moins... D'une spère supposé parfaite !
    - Problème calcule d'angle. Je dois supposé mon point de départ l'origine d'un plan et calculé l'angle de ce point
      avec le point d'arrivée
    Réglé ! Je pars de l'île des Evens. L'Est = 0° Nord = 90° ect et le début de la plage commence à environ 20° et fini à 130° environ.