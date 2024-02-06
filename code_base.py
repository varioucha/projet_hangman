# montrer quu'on est dans le jeu 


print("Welcome to hangman")
print("-------------------------------------------")
 
#cette partie prend un mot du fichier aleatoirement et le met en majuscule
import random
fichier = open("liste_de_mots_francais_frgut_.txt", "r")
list_de_mots = fichier.readlines()

mot_a_deviner = random.choice(list_de_mots)
mot_a_deviner = mot_a_deviner.upper()

nombre_de_erreur = 0

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

list_mot_choisi = []

#tant que le nombre d'erreur autorisé n'est pas dépacé le jeux continue
while nombre_de_erreur < 7:
    
    lettre_essaie = input("essayez une lettre").upper()
    #si la lettre dans l'alphabet, elle est supprimé de l'alphabet. Puis ajouté à la liste "list_mot_choisi".
    
    if lettre_essaie in alphabet:
        alphabet.remove(lettre_essaie)
        list_mot_choisi.append(lettre_essaie)
        
        # si lettre correspond au mot, le jeu continue sans erreur, sinon le nombre d'erreur augmente
        if lettre_essaie in mot_a_deviner: 
            print("Bravo!")
            
            #si mot_choisi correspond ä la liste, le boucle s'arrete
            if mot_a_deviner in list_mot_choisi:
                print("le jeu est fini")
                break 

        else:
            print("lettre pas dans le mot!")
            nombre_de_erreur = nombre_de_erreur + 1
    else: 
        print("arreeeeete")

print("perdu")
print("le mot était:" + mot_a_deviner)