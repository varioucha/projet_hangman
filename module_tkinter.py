from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
import random

#Information de base necessaire pour la suite
nombre_erreurs = 0
MAX_ERREURS = 6
lettres_essai = []
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#ouverture de la première fenetre qui confirme si joueurs veux jouer ou quitter
def premiere_fenetre():
    #ouvre la fenetre
    global window
    window = Tk()
    window.title("Hangman")
    window.geometry("350x350")
    print("jeu ouvert")

    #creer label
    label_word = Label(window, text= "Bienvenue dans le jeu du pendu\nVoulez vous jouer?")
    label_word.place(relx = 0.5, rely = 0.2, anchor = CENTER)

    #boutons pour jouer et quitter
    play_button = Button(window, text="Jouer", command=play_action)
    play_button.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    exit_button = Button(window, text="Exit", command=window.destroy) 
    exit_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)



    window.mainloop()

#fenetre qui s'ouvre si on continue à jouer, permet de choisir le niveau de difficulté
def play_action():
    window.destroy()
    print("Play button clicked")

    #nouvelle fenetre
    global window_2
    window_2 = Tk()
    window_2.title("Hangman")
    window_2.geometry("350x350")

    #label
    label_word = Label(window_2, text= "Choisissez le niveau:")
    label_word.place(relx = 0.5, rely = 0.2, anchor = CENTER)

    #boutons
    niveau_facile_button = Button(window_2, text="Niveau facile", command=facile_action)
    niveau_facile_button.pack(pady=20)
    niveau_facile_button.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    niveau_diff_button = Button(window_2, text="Niveau difficile", command=diff_action)
    niveau_diff_button.pack(pady=20)
    niveau_diff_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)

    window_2.mainloop()

def facile_action():
    print("niveau facile")

    global f
    # fait choisir la list de mot facile
    # Obtenir le chemin complet vers le script courant 
    script_path = Path(__file__).resolve()
    #récupérer le chemin vers le dossier parent du script courant
    script_dir = script_path.parent
    # ajoute le nom de notre fichier
    path = str(script_dir)+ "/list_mots_2.txt"
    #ouvre le fichier file.txt
    f = open(path, "r")

    window_2.destroy()
    # boutons qui commence jeu - envoye sur une autre def
    global window_3
    window_3 = Tk()
    window_3.title("Hangman")
    window_3.geometry("350x350")

    label_word = Label(window_3, text= "Niveau choisi: facile")
    label_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    debut_jeu_button = Button(window_3, text="Commencer le jeu", command=jeu)
    debut_jeu_button.pack(pady=20)
    debut_jeu_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
    window_3.mainloop()

def diff_action():

    print("niveau difficile")
    global f
    #pour niveau diff
    script_path = Path(__file__).resolve()
    #récupérer le chemin vers le dossier parent du script courant
    script_dir = script_path.parent
    #On ajoute le nom de notre fichier
    path = str(script_dir)+ "/list_mots_diff_2.txt"
    #on ouvre le fichier file.txt
    f = open(path, "r")

    window_2.destroy()

    global window_3
    window_3 = Tk()
    window_3.title("Hangman")
    window_3.geometry("350x350")

    label_word = Label(window_3, text= "Niveau choisi: difficile")
    label_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    debut_jeu_button = Button(window_3, text="Commencer le jeu", command=jeu)
    debut_jeu_button.place(relx = 0.5, rely = 0.6, anchor = CENTER)

    window_3.mainloop()


def jeu():
    print("début du jeu")

    window_3.destroy()
    # ouvre la fenetre
    window_4 = Tk()
    window_4.title("Hangman")
    window_4.geometry("800x800")

    #prend la list de mot en fonction de la difficulté choisi
    list_de_mots = f.readlines()
    #prend le mot au hasard de la list
    mot_a_deviner = random.choice(list_de_mots)
    mot_a_deviner = mot_a_deviner.strip()
    mot_a_deviner = mot_a_deviner.upper()

    # Affiche le jeu (les lettres à trouver), et le nombre de lettres retants 
    displayed_word_var = StringVar()
    remaining_letters_var = StringVar()
    
    displayed_word_label = Label(window_4, textvariable=displayed_word_var, font=("Arial", 24))
    displayed_word_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    remaining_letters_label = Label(window_4, textvariable=remaining_letters_var, font=("Arial", 20))
    remaining_letters_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    #espace pour mettre lettre + réacrion à la lettre 
    entree_lettre = Entry(window_4)
    entree_lettre.place(relx = 0.5, rely = 0.85, anchor = CENTER)
    message_var = StringVar()
    message_label = Label(window_4, textvariable=message_var, font=("Arial", 17))
    message_label.pack(pady = 40)

    #defénition qui permet de vérifié si la lettre est dans le mot recherché 
    def verifier_lettre():
        global nombre_erreurs
        lettre = entree_lettre.get().upper()  # Récupère la lettre de l'Entry
        entree_lettre.delete(0, 'end')  # Efface l'Entry après récupération

        if lettre in mot_a_deviner:
            if lettre in lettres_essai:
                message_var.set("Vous avez déjà essayé cette lettre.")
                nombre_erreurs += 1
                update_image()
            else:
                lettres_essai.append(lettre)
                message_var.set(f"Bien joué ! La lettre '{lettre}' est dans le mot.")
                display_word_state()
        elif lettre in alphabet:
            nombre_erreurs += 1
            update_image()

            message_var.set(f"Dommage, la lettre '{lettre}' n'est pas dans le mot.")
        else:
            message_var.set("Veuillez entrer une lettre valide.")

        display_word_state()

        # Vérifie ici si le jeu doit être arrêté et arret le jeu si oui
        if nombre_erreurs >= MAX_ERREURS:
            message_var.set(f"Jeu terminé. Vous avez dépassé le nombre d'erreurs autorisé. Le mot était : {mot_a_deviner}")
            entree_lettre.config(state='disabled')
            bouton_verif.config(state='disabled')
            recommencer_bouton = Button(window_4, text="Recommencer", command=recommencer_jeu)
            recommencer_bouton.place(relx = 0.5, rely = 0.7, anchor = CENTER)
            exit_button = Button(window_4, text="Exit", command=window_4.destroy) 
            exit_button.place(relx = 0.5, rely = 0.8, anchor = CENTER)

        elif set(mot_a_deviner) <= set(lettres_essai):  # Vérifie si le joueur a gagné et arret le jeu si oui
            message_var.set("Félicitations ! Vous avez trouvé le mot.")
            entree_lettre.config(state='disabled')
            bouton_verif.config(state='disabled')
            recommencer_bouton = Button(window_4, text="Recommencer", command=recommencer_jeu)
            recommencer_bouton.place(relx = 0.5, rely = 0.7, anchor = CENTER)
            exit_button = Button(window_4, text="Exit", command=window_4.destroy) 
            exit_button.place(relx = 0.5, rely = 0.8, anchor = CENTER)

        
# définition qui créer et adapte le jeu (lettres trouvé et recherché)
    def display_word_state():
        # Initialise le mot affiché comme une liste de tirets ou de lettres
        displayed_word = [letter if letter in lettres_essai else '_' for letter in mot_a_deviner]
        # Joins les éléments de la liste en une chaîne pour l'affichage
        displayed_word_str = ' '.join(displayed_word)
        # Mets à jour le widget Label pour l'état actuel du mot
        displayed_word_var.set("Mot actuel: " + displayed_word_str)
        # Afficher le nombre de lettres restantes à trouver
        remaining_letters = len([letter for letter in mot_a_deviner if letter not in lettres_essai])
        remaining_letters_var.set(f"Il reste {remaining_letters} lettre(s) à trouver.")
    
    display_word_state()

    def reinitialiser_jeu():#def qui rénitialise le jeu
        global nombre_erreurs, lettres_essai

        nombre_erreurs = 0
        lettres_essai = []

        # actualiser l'affichage
        display_word_state()
        message_var.set("")


    def recommencer_jeu():#def qui recommence le jeu
        window_4.destroy()
        reinitialiser_jeu()
        premiere_fenetre()

 #bouton qui permet de vérifié la solution
    bouton_verif= Button(window_4, text="Vérifier", command=verifier_lettre)
    bouton_verif.place(relx = 0.5, rely = 0.9, anchor = CENTER)


    #intergartion de l'image
    image_path_0 = Path(__file__).resolve()
    script_dir = image_path_0.parent
    image_path = str(script_dir)+ "/images/hangman0.png"
    image_original = Image.open(image_path)
    resized_image = image_original.resize((180, 180))
    photo = ImageTk.PhotoImage(resized_image)

    label_image = Label(window_4, image=photo)
    label_image.pack()
    label_image.place(relx = 0.5, rely = 0.3, anchor = CENTER)

    def update_image():
        global photo
        image_path_1 = Path(__file__).resolve()
        script_dir_1 = image_path_1.parent
        image_path_1 = str(script_dir_1)+ f"/images/hangman{nombre_erreurs}.png"
        image_original_1 = Image.open(image_path_1)
        resized_image = image_original_1.resize((180, 180))
        photo = ImageTk.PhotoImage(resized_image)
        label_image = Label(window_4, image=photo)
        label_image.pack()
        label_image.place(relx = 0.5, rely = 0.3, anchor = CENTER)



    window_4.mainloop()



premiere_fenetre()

