import numpy as np
import matplotlib.pyplot as plt


#1. Lecture des données des deux .csv en mémoire avEc Numpy.
def lecture_donnees(nfichier1,nfichier2) :
    tableau1 = np.genfromtxt(nfichier1,delimiter=',')
    tableau2 = np.genfromtxt(nfichier2,delimiter=',')
    return tableau1, tableau2
#2. test histogramme logarithmique
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

#3.+ 4.+ 5. histogramme complété
def hist2():
    histogramme1,histogramme2 = lecture_donnees('S2GE_APP3_Problematique_Detecteur_Primaire.csv', 'S2GE_APP3_Problematique_Detecteur_Secondaire.csv')
    hist1corrige= histogramme1[:,2]
    hist2corrige =histogramme2[:,2]
    bins = np.logspace(1,3, num=25)
    print(bins)
    plt.figure()
    #plt.xlim(0,300)
    #plt.ylim(0,3000)       plus beau sans les limites
    # pas utile : plt.plot(histogramme) car on fait l'histogramme
    plt.title('histogramme amplitude')
    plt.xlabel('amplitude(mV)')
    plt.ylabel('quantité')
    plt.semilogx()
    plt.hist(hist1corrige,bins=bins,histtype='step',label='histogramme primaire')    #plt.hist(hist1corrige,bins=1000) pas de bins est plus beau
    plt.hist(hist2corrige,bins=bins,histtype='step',label='histogramme secondaire')
    plt.legend()
    plt.grid()
    plt.show()


hist2()

