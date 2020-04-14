from random import*




def matalea(n,p): 
    mat=[]
    for i in range(0,p):
        ligne=[]
        for j in range(0,n):
            val = randint(1,9)
            ligne.append(val)
        mat.append(ligne)
    return mat
def matnulle(n,p):
    mat=[]
    for i in range(0,n+2):
        ligne=[]
        for j in range(0,p+2):
            valeur_nulle=0
            ligne.append(valeur_nulle)
        mat.append(ligne)
    return mat

def tableau(mat):
    
    for i in range(1,len(mat)-1):
        ligne_rand=randint(1,len(mat)-2)
        col_rand=randint(1,len(mat[1])-2)
        for j in range(1,len(mat[0])-1):
            mat[ligne_rand][col_rand] = '*'
    return mat
    
def afficher(mat): #affichage de la matrice en rangé pour mieux voir 
    for i in range(0,len(mat)):
        print(mat[i])

def tableau_debut(mat): #tableau avec des "?"
    
    for i in range(1,len(mat)-1):
        for j in range(1,len(mat[0])-1):
            mat[i][j] = '?'
    return mat


def nombre_mines(mat):

    for i in range(1,len(mat)-1):
        
        for j in range(1,len(mat[1])-1):
            
            if mat[i][j]==0:
                nbMines=0
                for l in range(i-1,i+2):
                    
                    for c in range(j-1,j+2):
                        if mat[l][c]=='*':
                            nbMines = nbMines+1
                mat[i][j]=nbMines
    return mat


def saisi_coordonnees():
    while (True):
        saisi_joueur = input("Veuillez entrer les coordonnées(ligne,colonne) : ")
        try:
            #verifie la saisi est du format (a,b)
            coor = saisi_joueur.split(',')
            if len(coor) != 2:
                raise Exception("Saisi incorrect, vos coordonnées comportent plus/moins d'élements qu'attendu (l,c).")
            #verifie que les saisi sont des entiers
            coor[0] = int(coor[0])
            coor[1] = int(coor[1])
            #Vérifie qu'ils sont compris entre 1 et 10
            if coor[0] > 9 or coor[0] < 0 or coor[1] > 9 or coor[1] < 0:
                raise Exception("Saisi incorect. Entrez des valeurs entre 1 et 10 .")

			#si tous les test sont bon on retourne les coordonnées
            return coor
            
        except ValueError:
            print ("Saisi incorrect. Veuillez entrer des valeur numérique seulement")
        except Exception as e:
            print (e)
def grille(mat_vide,mat_cache,mat_mine):
    liste_lettre = ["1","2","3","4","5"]
    liste_nombre = ["1","2","3","4","5"]
    liste_trait = ["___"] #7 under_scores
    liste_ver = ["|"]
    taille_lettre= len(liste_lettre)
    taille_nombre= len(liste_nombre)
    liste_cordo = []
    ligne_lettre=""
    ligne_trait=""
    ligne_vertical=""
    espace_7="   "
    espace_4="    "
    espace_8="      "

    for i in range(taille_lettre):
        ligne_lettre=ligne_lettre+liste_lettre[i]+espace_7
    print ("     "+ligne_lettre)

    for i in range(0,5):
       ligne_trait=ligne_trait+liste_trait[0]+" "
    print(espace_4+ligne_trait)
    for i in range(0,5):
        ligne_vertical=""
        for j in range(0,5):
            ligne_vertical= ligne_vertical+liste_ver[0]+" "+str(mat_vide[i+1][j+1])+" " #espaces de 6
            #ligne horizontal de traits verticaux
        print(liste_nombre[i]+"  "+ligne_vertical) #au début on affiche un chiffre allant de 1 à 9
    #Pareil que la 1er ligne
        print(espace_4+ligne_trait) #Ligne de traits horizontaux

def compteur_mines(mat_cache):
    compteur=0
    for i in range(1,len(mat_cache)-1):
        for j in range(1,len(mat_cache[1])-1):
            if mat_cache[i][j] == '*':
                compteur = compteur+1
    return compteur
    

def main():
    win=True
    mat_vide = matnulle(5,5) #creation de matrice nulle avec des 0
    mat_vide = tableau_debut(mat_vide) #placer des "?" dans toutes les cases

    mat_cache = matnulle(5,5) #Creation d'une deuxieme matrice
    mat_cache = tableau(mat_cache)#placer les mines au hasard
    

    mat_mine = nombre_mines(mat_cache) #matrice qui contient les nombre de mines dans les cases
    print (mat_cache) #test pour savoir on son les mines
    nb_mines = compteur_mines(mat_cache) #calcul du nombre de mines
    #on entoure la matrice du jeu avec des 0

    nb_gagner = 25 - compteur_mines(mat_cache) #nombre de cases sans mines
    print(nb_gagner)

    mines_gagner = 0
    

    # le jeu continue tant qu'on découvre pas les cases qui n'ont pas de mines
    # ou alors tant qu'on ne touche pas une mine
    while (win == True):
        if mines_gagner<nb_gagner: #on verifie a cache fois
            
            grille(mat_vide,mat_cache,mat_mine) #affichage de la grille avec "?"
            cord = saisi_coordonnees() #demande de saisi de cordonnées
            ligne = cord[0] #on récuper la ligne de la saisi
            colonne = cord[1]#recup de la colonne
            
            if mat_cache[ligne][colonne]!='*':  #si cordonnes difference d'une mine
                #devoiler la case avec le numero de mines autour
                mat_vide[ligne][colonne]=mat_mine[ligne][colonne]
                nb_mines = compteur_mines(mat_cache)
                mines_gagner=mines_gagner+1
                print(mines_gagner)
                win = True
            elif mat_cache[ligne][colonne] == 0:
                #si cordo est 0 devoiler la case avec 0 mines
                mines_gagner = mines_gagner+1
                print(mines_gagner)
                win = True
            elif mat_cache[ligne][colonne] =='*':
                #si on touche la mine on affiche "perdu" et on montre la solution
                print("**** Vous avez perdu ****  =( \n     Solution : \n")
                
                mat_vide = mat_mine
                grille(mat_vide,mat_cache,mat_mine)
                mines_gagner = mines_gagner= 0
                win = False
        #si le nombre de cases devoiles est complete alors on affiche "gagné"
        #et on montre le placement des mines
        else:
            win = False
            print("Bravo !! ***** Vous avez gagné *****")
            mat_vide = mat_mine
            grille(mat_vide,mat_cache,mat_mine)
        win = win
    
#pour relancer la partie on rentre main() sur la console
#appuyer sur entrer quand on lance le script
if __name__=="__main__":
	main()
  




    

    


