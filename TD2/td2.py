# -*- coding: utf-8 -*-
# %% Exercice 1

def Exo1():
    res = [] 
    with open("fichier.txt","r") as f:
        line = f.readline()
        while line:
            res.append(float(line.strip()))
            line = f.readline()
    with open("newfichier.txt","w") as f:
        for x in res:
            f.write(str(int(round(x,0)))) # avec round on obtien l'arrondi mais avec .0 a la fin, donc jai fait int() pour prendre que la pertie entiere
            f.write("\n")
# %% Exercice 2
def bissex(annee):
  
    if(annee%4==0 and annee%100!=0 or annee%400==0):
        return True
    else:
        return False

def Exo2():
    #a
    Semestre2 = {
        "janvier": 31,
        "février": 28,
        "mars" : 31,
        "avril" : 30,
        "mai" : 31
        }
    #b
    for x in Semestre2.keys():
        print(x)
    for x in Semestre2.values():
        print(x)
    #c
    annee = 2021 # input ???
    if bissex(annee):
        Semestre2["février"] = 28
    
    #d ? j'ai pas compris comment ça ça commen le 4sep
    Semestre1 = {
        "septembre": (30-4), # commece 4 septembre
        "octobre": 31,
        "novembre" : 30,
        "decembre" : 31,
      
    }
    AnneScolaire = {}
    for i,x in Semestre2.items():
        AnneScolaire[i] = x
    for i,x in Semestre1.items():
        AnneScolaire[i] = x
    print(AnneScolaire) 
    
if __name__ == "__main__":
    Exo2()
