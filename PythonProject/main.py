import numpy as np
import matplotlib.pyplot as plt

#1. Chargez les données des deux fichiers en mémoire à l’aide de la librairie Numpy.
Tableau1 = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv', delimiter=',')
Tableau2 = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Secondaire.csv', delimiter=',')
print(Tableau1)
print(Tableau2)