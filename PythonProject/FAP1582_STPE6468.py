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
    histogramme= np.concatenate((histogramme1,histogramme2), axis=0)
    hist1corrige= histogramme1[:,2]
    hist2corrige =histogramme2[:,2]
    #histo=np.logspace(histogramme2[:,2],num=1000)
    bins = np.logspace(1, 3, num=25)
    print(bins)
    #hS=[]
    #hS=concidence(histogramme1,histogramme2)
    #hist3 = [item[1] for item in hS]

    plt.figure()
    #plt.xlim(0,300)
    #plt.ylim(0,3000)       plus beau sans les limites
    # pas utile : plt.plot(histogramme) car on fait l'histogramme
    plt.title('histogramme amplitude')
    plt.xlabel('amplitude(mV)')
    plt.ylabel('quantité')
    plt.semilogx()
    plt.hist(histogramme[:,2],bins=bins,histtype="step")    #plt.hist(hist1corrige,bins=1000) pas de bins est plus beau
    plt.hist(hist2corrige,bins=bins,histtype="step")
    #plt.hist(hist3, bins=bins, histtype="step")
    plt.grid()
    plt.show()


def hist3():
    histogramme1,histogramme2 = lecture_donnees('S2GE_APP3_Problematique_Detecteur_Primaire.csv', 'S2GE_APP3_Problematique_Detecteur_Secondaire.csv')
    #histogramme= np.concatenate((histogramme1,histogramme2), axis=0)
    #histo=np.logspace(histogramme2[:,2],num=1000)
    bins = np.logspace(1, 3, num=25)

    hS,hN=coincidence(histogramme1,histogramme2)
    hist3 = [item[1] for item in hS]
    hist4 = [item[1] for item in hN]

    plt.figure()
    # pas utile : plt.plot(histogramme), car on fait l'histogramme
    plt.title('histogramme amplitude')
    plt.xlabel('amplitude(mV)')
    plt.ylabel('quantité')
    plt.semilogx()

    plt.hist(histogramme1[:,2],bins=bins,histtype="step",label="Tous les évenements")    #plt.hist(hist1corrige,bins=1000) pas de bins est plus beau
    y, bins_bout, _ = plt.hist(hist3, bins=bins, histtype="step", label="Coïncident")
    plt.hist(hist4, bins=bins, histtype="step",label="Autres")

    bins_centre = (bins_bout[:-1] + bins_bout[1:]) / 2
    erreur=np.zeros_like(y, dtype=float)
    for i in range(len(bins_bout)-1):
        dans = (hist3 >= bins_bout[i]) & (hist3 < bins_bout[i + 1])
        Nbarre = np.sum(dans)
        #erreur[i] = np.sqrt(Nbarre/i)

    #plt.errorbar(bins_centre,y,yerr=erreur)

    plt.legend()
    plt.grid()
    plt.show()

def coincidence(h1,h2):
    temps = 0.01
    i = 0
    y = 0
    hS = []  # Liste pour stocker les résultats
    hN =[] # Liste pour stocker les résultats non concident
    while i < len(h1) and y < len(h2):
        if h2[y][1] <= h1[i][1] + temps and h1[i][1] <= h2[y][1] + temps:
            if h2[y][2] <= h1[i][2]:
                hS.append((h2[y][1], h2[y][2]))  # Utiliser append pour ajouter à la liste
                y+=1
                i+=1
            elif h1[i][2] < h2[y][2]:
                hS.append((h1[i][1], h1[i][2]))  # Utiliser append pour ajouter à la liste
                y += 1
                i += 1
        elif h2[y][1] < h1[i][1]:
            y += 1
            #hN.append((h2[y][1], h2[y][2]))
        elif h1[i][1] < h2[y][1]:
            hN.append((h1[i][1], h1[i][2]))
            i += 1

    #print(y,i)
    #print(len(hS))
    #print(len(hN))
    #print(len(h1))
    #print(hS[1290][0],hS[1290][1])
    #print('fini')
    return hS, hN # Retourner toute la liste
