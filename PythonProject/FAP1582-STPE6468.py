import numpy as np
import matplotlib.pyplot as plt


#1. Lecture des données des deux .csv en mémoire avEc Numpy.
def lecture_donnees(nfichier1,nfichier2) :
    tableau1 = np.genfromtxt(nfichier1,delimiter=',')
    tableau2 = np.genfromtxt(nfichier2,delimiter=',')
    return tableau1, tableau2
#2.+ 3. création dun premier 1er hist et nom axes et titre
def hist1():
    #la 1ere ligne est un tuple à cause des multiples return
    histogramme1, histinutile = lecture_donnees('S2GE_APP3_Problematique_Detecteur_Primaire.csv','S2GE_APP3_Problematique_Detecteur_Secondaire.csv')    #histinutile car on regarde que le 1er
    plt.figure()
    plt.xlim(0,300)
    plt.ylim(0,3000)
                                                # test:plt.plot(histogramme[:,2]) (ce n'est pas la façon de faire)
    plt.hist(histogramme1[:,2],bins=1000)       # on fait un tableau que pour le 1er histogramme
    plt.grid()
    plt.show()

def hist2():
    histogramme1,histogramme2 = lecture_donnees('S2GE_APP3_Problematique_Detecteur_Primaire.csv', 'S2GE_APP3_Problematique_Detecteur_Secondaire.csv')
    hist1corrige= np.log10(histogramme1[:,2])
    hist2corrige = np.log10(histogramme2[:,2])

    plt.figure()
    #plt.xlim(0,300)
    #plt.ylim(0,3000)       plus beau sans les limites
                                                # pas utile : plt.plot(histogramme) car on fait l'histogramme
    plt.title('histogramme amplitude')
    plt.xlabel('amplitude(mV)')
    plt.ylabel('quantité')
    plt.hist(hist1corrige)    #plt.hist(hist1corrige,bins=1000) pas de bins est plus beau
    plt.hist(hist2corrige)
    plt.grid()
    plt.show()


hist2()

