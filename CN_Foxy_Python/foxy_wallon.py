import JeulinLib # module spécifique pour communiquer avec la console
import matplotlib.pyplot as plt
import numpy as np

def acquisition(voie, tf, N):
    "réalise l'acquisition de tension prise sur voie, pendant une durée tf, avec N points de mesure"
    "voie est une liste d'entiers correspondant aux voies à visualiser, N est un entier, tf un réel"
    
    # Connexion et Paramétrage
    bResultConnect = JeulinLib.Foxy_Connect() #connexion à la console
    if bResultConnect==False :
        print("Erreur de connexion à la console")
        return ...,...

    nb=len(voie)

    for i in range(nb):
        bResultCalibre =JeulinLib.Foxy_SetCalibre(str(voie[i]),0,0,3)
        if bResultCalibre==False :
            print("Erreur d'initialisation du calibre")
    
    dt=tf/N
    bResult = JeulinLib.Foxy_AcquisitionInit(tf,N) # paramètres acquisition
    if bResult==False :
        print("Erreur d'initialisation de l'acquisition")
        return ...,...
    
    
    # Sélection des voies qui seront acquises
    for i in range(nb):
        #print(i)
        zPort=str(voie[i])
        bResult2 = JeulinLib.Foxy_AcquisitionAdd(zPort,0)
        if bResult2==False:
            print("Erreur d'ajout de voie")
        
    # Lancement de l'acquisition
    Y=JeulinLib.Foxy_AcquisitionStart()
    if Y==None :
        print("Erreur d'acquisition")


    # Déconnexion
    JeulinLib.Foxy_Deconnect()

    t=np.linspace(0,tf,N)

    return t,Y


#tf=0.005
#N=1000

#t,Y=acquisition([1,2],tf,N)
#print(Y)

#plt.plot(t,Y[0],label="CH1")
#plt.plot(t,Y[1],label="CH2")

#plt.legend()
#plt.grid()
#plt.xlabel("t en s")
#plt.ylabel("tension en V")
#plt.show()

    
