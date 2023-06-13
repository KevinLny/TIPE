'''///////////////////////////////////////////////////////////////
//  Kevin Kuzu                                                  //
//                                                              //
//  11/06/2023                                                  //
///////////////////////////////////////////////////////////////'''

from fonction_donnees_usuel import*
from meteo_data import*
import numpy as np
import matplotlib.pyplot as plt

#//////////////////////////////////////////////////////////////////
#//                                                              //      
#//                    EQUATION PHYSIQUE                         //
#//                                                              //
#//////////////////////////////////////////////////////////////////

def function(t, surface, ct, cp):
    return (1.0/(4.0*60.0)) * (t**2) * 1.292 * surface * (wind_speed**2) * (ct + cp)

def determine_t(distance, surface, angle_planche):
    distance = distance*(10**3)
    ct, cp = coefficient_porte_traine(wind_deg, angle_planche)
    t = 0
    res = 0.0
    while(distance > res):
        res = function(t, surface, ct, cp)
        t = t + 0.1
    return t

#//////////////////////////////////////////////////////////////////
#//                                                              //
#//               RECHERCHE TEMPS MINIMUM                        //
#//                                                              //
#//////////////////////////////////////////////////////////////////

time = []

for i in range(10):
    time.append(determine_t(element[i][3], data_voile[0][0], element[i][2]))

indicebest = time.index(min(time))  # Indice du meilleur point de départ pour aller à l'île des Evens
print(time.index(min(time)))

#//////////////////////////////////////////////////////////////////
#//                                                              //
#//                  COURBE DISTANCE DE LA                       //
#//                  MEILLEURS TRAJECTOIRE                       //
#//                                                              //
#//////////////////////////////////////////////////////////////////

x = np.linspace(0, 3600, 1000)
ct, cp = coefficient_porte_traine(wind_deg, element[i][2])
y = function(x, data_voile[0][0], ct, cp)

plt.plot(x, y)
plt.show()