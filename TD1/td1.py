# -*- coding: utf-8 -*-
import time
# %%  Exercice 1

def vitesse(d,t):
    return d/t
def Exo1():
    d = 6.892
    t = 19.7
    res = vitesse(d, t)
    print(f"Vitesse : {round(res,2)}")

# %%  Exercice 2

def Questiona():
    print("\n**********avec test avec alternative :")
    a=input("Entrez un nombre a :")
    b=input("Entrez un nombre b :")
    if(a>b):
        maxi,mini=a,b
    else:
        maxi,mini=b,a
    print("minimum=",mini,"\nmaximum=",maxi )
    
def Questionb():
    print("\n*********avec test simple sans alternative :")
    a=eval(input("Entrez un nombre a : "))
    b=eval(input("Entrez un nombre b : "))
    maxi,mini=b,a
    if(a>b):
        maxi,mini=a,b
    print("minimum=",mini,"\nmaximum=",maxi )
    
def Questionc():
    print("\n*********avec test ternaire :")
    a=eval(input("Entrez un nombre a : "))
    b=eval(input("Entrez un nombre b : "))
    (maxi,mini)=(b,a) if a<b else (a,b)
    print("minimum=",mini,"\nmaximum=",maxi )

def Exo2():
    print("-----------------------Exo2--------------------")
    print("Prgm calculant le maximum et le minimum de 2 chiffres a et b : ")
    Questiona()
    Questionb()
    Questionc()
    
# %%  Exercice 3
def volBoite(x1 = None,x2 = None,x3 = None):
    
    if(x1):
        return x1**3
    elif x1 and x2:
        return x1*x1*x2
    elif x1 and x2 and x3:
         return x1*x3*x2
    else:
        return None
    
def Exo3():
    x1 = 5.2
    print(volBoite(x1))

# %%  Exercice 4
def eleMax(liste,debut = None,fin = None):
    if not fin:
        fin = len(liste)-1
    if not debut:
        debut = 0
   
    if(fin > len(liste)-1)or(debut < 0):
        print("error indice")
    else:
        return max(liste[debut:fin+1])

def Exo4():
    serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
    print(eleMax(serie))
    print(eleMax(serie,2,5))
    print(eleMax(serie,2))
    print(eleMax(serie,fin =3, debut =1))

# %%  Exercice 5
def mois(t1,t2):
    t3 = []
    for i in range(len(t1)):
        t3.append(t2[i])
        t3.append(t1[i])
    return t3
        
def Exo5():
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai','Juin','Juillet', 'Août', 'Septembre',
          'Octobre','Novembre', 'Décembre']
    print(mois(t1,t2))
    
# %%  Exercice 6

def inverse(s):
    res = list(s)
    res.reverse()
    return ''.join(res)

def Exo6():
    print(inverse("zorglub"))
    
# %%  Exercice 7
def mafonction(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr
                
def Exo7():
    l = [int(x) for x in list("522446")]
    print(l)
    l = mafonction(l)
    print(l)
    # la fct mafonction() trie le tableau ! ( une tri bulle)
Exo7()
# %%  Exercice 8
def loadFic(nomfic):
    res = [] 
    with open(nomfic,"r") as f:
        line = f.readline()
        while line:
            res.append(line.strip())
            line = f.readline()
    res = [int(k) for x in res for k in x.split(";")]
    return res   

def fusion(gauche,droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):        
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat
 
def Trifusion(m):
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = Trifusion(gauche)
    droite = Trifusion(droite)
    return list(fusion(gauche, droite))


def Exo8():
    listeInt = loadFic("tableau.txt")
    print("avant tri fusion",listeInt)
    a = time.time()
    listeInt = Trifusion(listeInt)
    b = time.time()
    print("après tri fusion",listeInt)
    tmp1 = b-a
    print("#", tmp1)
    listeInt = loadFic("tableau.txt")
    print("avant tri mafonction",listeInt)
    a = time.time()
    listeInt = mafonction(listeInt)
    b = time.time()
    print("après tri mafonction",listeInt)
    tmp2 = b-a
    print("#",tmp2)
    plusrapide = "trirapide" if tmp1 < tmp2 else "mafonction"
    print("le plus rapide est :",plusrapide)

if __name__== "__main__":
    Exo8()