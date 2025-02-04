import numpy as np
import matplotlib.pyplot as plt


#1. Chargez les données des deux fichiers en mémoire à l’aide de la librairie Numpy.
Tableau1str = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv',str, delimiter='\n')
#Tableau2str = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Secondaire.csv',str, delimiter='\n')

Tableau1 = np.genfromtxt(Tableau1str,int,delimiter=',')
#Tableau2 = np.genfromtxt(Tableau2str,int,delimiter=',')
print(Tableau1[1][2])
#print(Tableau2)


plt.figure()
#x=np.arange(0,1000,0.2)
plt.plot(Tableau1[:,2])
plt.xlabel("temps(ms)")
plt.ylabel("tension(mV)")
plt.hist()
plt.grid()
plt.show()