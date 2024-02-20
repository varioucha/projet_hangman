
"""
import random
fichier = open("liste_de_mots_francais_frgut_.txt", "r")
list_de_mots = fichier.readlines()

mot_a_deviner = random.choice(list_de_mots)
mot_a_deviner = mot_a_deviner.upper()

mot_affiche_list = ["_"] * len(mot_a_deviner)

lettre_essaie = input("")

#dans if lettre dans word a deviner
for index, letter in enumerate(mot_a_deviner):
            if letter == lettre_essaie:
                mot_affiche_list[index] = lettre_essaie  # Replace the underscore with the guessed letter
        print(f"Word: {''.join(mot_affiche_list)}")  # Join the list elements into a string for display
"""



mot_montré = "_" * len(word)