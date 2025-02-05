import numpy as np
import matplotlib.pyplot as plt
import argparse
from FAP1582_STPE6468 import concidence

def histogramme(error,fichier):
    donneesCompletes1 = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv',delimiter=',')
    donneesCompletes2 = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Secondaire.csv',delimiter=',')

    histogramme1 = donneesCompletes1[:, 2]
    histogramme2 = donneesCompletes1[:, 2]
    bins = np.logspace(1, 3, num=25)

    hS, hN = concidence(donneesCompletes1, donneesCompletes2)
    histogramme3 = [item[1] for item in hS]
    histogramme4 = [item[1] for item in hN]

    plt.figure()
    # plt.xlim(0,300)
    # plt.ylim(0,3000)       plus beau sans les limites
    # pas utile : plt.plot(histogramme) car on fait l'histogramme
    plt.title('histogramme amplitude')
    plt.xlabel('amplitude(mV)')
    plt.ylabel('quantité')
    plt.semilogx()
    plt.hist(histogramme1, bins=bins, histtype="step",label="Tous les évenements")  # plt.hist(hist1corrige,bins=1000) pas de bins est plus beau
    plt.hist(histogramme3, bins=bins, histtype="step", label="Coincident")
    plt.hist(histogramme4, bins=bins, histtype="step", label="Autres")
    plt.errorbar(1000, 2000)
    plt.legend()
    plt.grid()

    if error:
        #plt.errorbar()
        if fichier:
            plt.savefig("PAIF1582,STPE6468--corrige")
        else:
            plt.show()
    else:
        if fichier:
            plt.savefig("PAIF1582,STPE6468")
        else:
            plt.show()

parser=argparse.ArgumentParser(description='Fichier et temps mort')
parser.add_argument('-F','--fichier',help='0=print à écran, 1=print en png',type=bool,default=0)
parser.add_argument('-T','--temps-mort',help='0=sans barre d erreur, 1=barre d erreurs',type=bool,default=0)
args = parser.parse_args()

histogramme(args.temps_mort,args.fichier)