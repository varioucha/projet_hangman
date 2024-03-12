from pathlib import Path
import random

from tkinter import *
from PIL import Image, ImageTk

def display_word_state(mot_a_deviner, lettres_essai):
    # Initialiser le mot affiché comme une liste de tirets ou de lettres
    displayed_word = [letter if letter in lettres_essai else '_' for letter in mot_a_deviner]
    # Joindre les éléments de la liste en une chaîne pour l'affichage
    displayed_word_str = ' '.join(displayed_word)
    # Afficher l'état actuel du mot
    print("Mot actuel: " + displayed_word_str)
    # Afficher le nombre de lettres restantes à trouver
    remaining_letters = len([letter for letter in mot_a_deviner if letter not in lettres_essai])
    print(f"Il reste {remaining_letters} lettre(s) à trouver.")

#creation de la fenetre
window = Tk()
window.title("Hangman")
window.geometry("600x400")

# Message de bienvenue

text = Text(BOTTOM)
text.insert(INSERT,"Bienvenue dans le jeu du pendu" )
label_word = Label(window, text= "Bienvenue dans le jeu du pendu",  bg="white", fg="black")
label_word.place(x=100, y=200)


#creer systeme de joueurs enrengistrer et les milleures scores:

#choisir le niveau (list de mots un ou deux)
label_word = Label(window, text= "Hello",  bg="white", fg="black")
label_word.place(x=100, y=200)
niveau = int(input("choissisez votre niveau: (1) : mots facile, (2) : mots difficile."))
if niveau == 1:
    print("niveau choisi facile")
    # Obtenir le chemin complet vers le script courant x2
    script_path = Path(__file__).resolve()

    #récupérer le chemin vers le dossier parent du script courant
    script_dir = script_path.parent

    #On ajoute le nom de notre fichier
    path = str(script_dir)+ "/list_mots_2.txt"

    #on ouvre le fichier file.txt
    f = open(path, "r")

else:
    print("niveau choisi difficile")
    #pour niveau diff
    script_path = Path(__file__).resolve()

    #récupérer le chemin vers le dossier parent du script courant
    script_dir = script_path.parent

    #On ajoute le nom de notre fichier
    path = str(script_dir)+ "/list_mots_diff_2.txt"

    #on ouvre le fichier file.txt
    f = open(path, "r")


#definir mot
list_de_mots = f.readlines()

mot_a_deviner = random.choice(list_de_mots)
mot_a_deviner = mot_a_deviner.upper()

lettres_essai = []
# Nombre d'erreurs et Alphabet
nombre_de_erreurs = 0
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

display_word_state(mot_a_deviner, lettres_essai)

# Boucle de jeu
while nombre_de_erreurs < 6 and set(mot_a_deviner) != set(lettres_essai):
    lettre_essai = input("Essayez une lettre: ").upper()

    if lettre_essai in mot_a_deviner:
        if lettre_essai in lettres_essai:
            print("Vous avez déjà essayé cette lettre. Essayez en une autre")
            nombre_de_erreurs += 1
        else:
            print(f"Bien joué ! La lettre '{lettre_essai}' est dans le mot.")
            lettres_essai.append(lettre_essai)
    elif lettre_essai in alphabet:
        print(f"Dommage, la lettre '{lettre_essai}' n'est pas dans le mot.")
        nombre_de_erreurs += 1
    else:
        print("Mettez une Lettre ou arretez de jouer")

    display_word_state(mot_a_deviner, lettres_essai)

    if set(mot_a_deviner) == set(lettres_essai):
        print("Félicitations ! Vous avez trouvé le mot.")
        break
    elif nombre_de_erreurs >= 6:
        print("Jeu terminé. Vous avez dépassé le nombre d'erreurs autorisé.")
        break

if set(mot_a_deviner) != set(lettres_essai):
    print("Le mot à deviner était:", mot_a_deviner)

    