'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //
//  11/06/2023                                                  //
///////////////////////////////////////////////////////////////'''

from fonction_donnees_usuel import*
from meteo_data import*
import numpy as np
from math import*
import matplotlib.pyplot as plt

#//////////////////////////////////////////////////////////////////
#//                                                              //      
#//                    EQUATION PHYSIQUE                         //
#//                                                              //
#//////////////////////////////////////////////////////////////////

def function(t, surface, angle_planche, ct, cp):
    angle = abs(wind_deg - angle_planche) % 360
    return (1.0/(2.0*(poid + 50))) * t * 1.292 * surface * (wind_speed**2) * abs(cp*sin(angle) - ct*cos(angle))


# On determine la vitesse de la planche à un instant t

def determine_v(t, surface, angle_planche):
    ct, cp = coefficient_porte_traine(wind_deg, angle_planche)
    v = function(t, surface, angle_planche, ct, cp)
    return v


#//////////////////////////////////////////////////////////////////
#//                                                              //
#//               RECHERCHE TEMPS MINIMUM                        //
#//                                                              //
#//////////////////////////////////////////////////////////////////


# On fait le rapport de la distance/vitesse de tous les points pour obtenir le temps minimum

def liste_vitesse():                  
    vitesses = []
    for i in range (len(element)):
        v = determine_v(600, data_voile[0][0], element[i][2])
        vitesses.append(v)  
    return vitesses

def temps_min():
    vitesses = liste_vitesse()
    temps = []
    for i in range (len(vitesses)):
        if(vitesses[i] != 0):
            t = element[i][3] / vitesses[i]
            temps.append(t)
        else :
            temps.append(700)
    indice_position = temps.index(min(temps))
    return indice_position
        
indicebest = temps_min()
print(indicebest)


vitesse = []
for t in range (600):
    vitesse.append(determine_v(t, data_voile[0][0], element[indicebest][2]))
