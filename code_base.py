# montrer quu'on est dans le jeu 
print("Welcome to hangman")
print("-------------------------------------------")

#cette partie prend un mot du fichier aleatoirement et le met en majuscule
import random
fichier = open("liste_de_mots_francais_frgut.txt", "r")
list_de_mots = fichier.readlines()

mot_a_deviner = random.choice(list_de_mots)
mot_a_deviner = mot_a_deviner.upper()

nombre_de_erreur = 0

#tant que le nombre d'erreur autorisé n'est pas dépacé le jeux continue
while nombre_de_erreur < 7:
    lettre_essaie = input("essayez une lettre")
    if lettre_essaie in mot_choisi:
        print("Bravo!")
        #supp lettre de la list
    else:
        print("lettre pas dans le mot!")
        nombre_de_erreur = nombre_de_erreur + 1
