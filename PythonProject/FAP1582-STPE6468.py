import numpy as np
import matplotlib.pyplot as plt


#1. Lecture des données des deux .csv en mémoire avEc Numpy.
def lecture_donnees(nfichier1,nfichier2) :
    tableau1 = np.genfromtxt(nfichier1,delimiter=',')
    tableau2 = np.genfromtxt(nfichier2,delimiter=',')

    #tableau1 = np.genfromtxt(tab1,delimiter=',')
    #tableau2 = np.genfromtxt(tab2,delimiter=',')


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
    hist1corrige= histogramme1[:,2]
    hist2corrige =histogramme2[:,2]
    #histo=np.logspace(histogramme2[:,2],num=1000)
    bins = np.logspace(1, 3, num=25)


    hS=concidence(histogramme1,histogramme2)

    plt.figure()
    #plt.xlim(0,300)
    #plt.ylim(0,3000)       plus beau sans les limites
    # pas utile : plt.plot(histogramme) car on fait l'histogramme
    plt.title('histogramme amplitude')
    plt.xlabel('amplitude(mV)')
    plt.ylabel('quantité')
    plt.semilogx()
    plt.hist(hist1corrige,bins=bins,histtype="step")    #plt.hist(hist1corrige,bins=1000) pas de bins est plus beau
    plt.hist(hist2corrige,bins=bins,histtype="step")
    plt.grid()
    plt.show()

def concidence(h1,h2):
    temps = 0.1
    i = 0
    y = 0
    hS = []  # Liste pour stocker les résultats
    while i < len(h1) and y < len(h2):
        if h2[y][1] <= h1[i][1] + temps and h1[i][1] <= h2[y][1] + temps:
            if h2[y][2] <= h1[i][2]:
                hS.append((h2[y][1], h2[y][2]))  # Utiliser append pour ajouter à la liste
                y+=1
                i+=1
            elif h1[i][2] < h2[y][2]:
                hS.append((h1[y][1], h1[y][2]))  # Utiliser append pour ajouter à la liste
                y += 1
                i += 1
        elif h2[y][1] < h1[i][1]:
            y += 1
        elif h1[i][1] < h2[y][1]:
            i += 1
    print(len(hS))
    print(hS[1290][0],hS[1290][1])
    print('fini')
    return hS  # Retourner toute la liste
concidence(np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv',delimiter=','), np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Secondaire.csv',delimiter=','))

