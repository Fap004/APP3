import numpy as np
import matplotlib.pyplot as plt
import argparse
from FAP1582_STPE6468 import concidence

def histogramme(error,fichier):
    donneesCompletes1 = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv',delimiter=',')
    donneesCompletes2 = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Secondaire.csv',delimiter=',')

    hS, hN = concidence(donneesCompletes1, donneesCompletes2)
    tempsTotal= (donneesCompletes1[-1][1]-donneesCompletes1[0][1])/1000
    tempsMort=np.sum(donneesCompletes1[:,3])/1000
    tempsActif=tempsTotal-tempsMort
    print(tempsTotal)
    histogramme1 = donneesCompletes1[:, 2]
    histogramme2 = donneesCompletes2[:, 2]
    histogramme3 = [item[1] for item in hS]
    histogramme4 = [item[1] for item in hN]
    print(len(histogramme3))
    bins = np.logspace(1, 3, num=25)




    plt.figure()
    plt.xlabel('amplitude(mV)')
    plt.ylabel('Rate/bin[S-1]')
    plt.semilogx()
    #plt.errorbar(1000, 2000)
    plt.grid()

    if error:
        plt.hist(histogramme1, bins=bins, histtype="step", weights = (1 / tempsActif) * np.ones_like(histogramme1),label="Tous les évenements")
        plt.hist(histogramme3, bins=bins, histtype="step",weights = (1 / tempsActif) * np.ones_like(histogramme3), label="Coincident")
        plt.hist(histogramme4, bins=bins, histtype="step", weights = (1 / tempsActif) * np.ones_like(histogramme4), label="Autres")
        plt.title('histogramme amplitude corrigé')
        plt.legend()
        if fichier:
            print("grosse bitch")
            plt.savefig("PAIF1582,STPE6468--corrige")
        else:
            plt.show()
    else:
        plt.hist(histogramme1, bins=bins, histtype="step", weights = (1 / tempsTotal) * np.ones_like(histogramme1),label="Tous les évenements")
        plt.hist(histogramme3, bins=bins, histtype="step",weights = (1 / tempsTotal) * np.ones_like(histogramme3), label="Coincident")
        plt.hist(histogramme4, bins=bins, histtype="step", weights = (1 / tempsTotal) * np.ones_like(histogramme4), label="Autres")
        plt.title('histogramme amplitude non-corrigé')
        plt.legend()
        if fichier:
            plt.savefig("PAIF1582,STPE6468")
        else:
            plt.show()

parser=argparse.ArgumentParser(description='Fichier et temps mort')
parser.add_argument('-F','--fichier', action='store_true',help='0=print à écran, 1=print en png')
parser.add_argument('-T','--temps-mort', action='store_true',help='0=sans barre d erreur, 1=barre d erreurs')
args = parser.parse_args()



histogramme(args.temps_mort,args.fichier)
