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

# Définir un mot à deviner
#cette partie va prendre un mot du fichier aleatoirement et le met en majuscule
import random
fichier = open("liste_de_mots_francais_frgut_.txt", "r")
list_de_mots = fichier.readlines()

mot_a_deviner = random.choice(list_de_mots)
mot_a_deviner = mot_a_deviner.upper()

lettres_essai = []
# Message de bienvenue
print("Bienvenue dans le jeu du pendu")
print("-------------------------------------------")

# Nombre d'erreurs et Alphabet
nombre_de_erreurs = 0
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# Boucle de jeu
while nombre_de_erreurs < 7 and set(mot_a_deviner) != set(lettres_essai):
    lettre_essai = input("Essayez une lettre: ").upper()

    if lettre_essai in mot_a_deviner:
        if lettre_essai in lettres_essai:
            print("Vous avez déjà essayé cette lettre. Essayez en une autre")
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
    elif nombre_de_erreurs >= 7:
        print("Jeu terminé. Vous avez dépassé le nombre d'erreurs autorisé.")
        break

if set(mot_a_deviner) != set(lettres_essai):
    print("Le mot à deviner était:", mot_a_deviner)

