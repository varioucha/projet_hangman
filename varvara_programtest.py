
#test pour username et score

import pickle

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0

    def mettre_a_jour_score(self, points):
        self.score += points

class Jeu:
    def __init__(self):
        self.joueurs = []

    def ajouter_joueur(self, joueur):
         self.joueurs.append(joueur)   

    def trouver_joueur(self, nom):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                return joueur
        return None

    def sauvegarder(self, fichier):
        with open(fichier, 'wb') as f:
            pickle.dump(self.joueurs, f)

    def charger(self, fichier):
        try:
            with open(fichier, 'rb') as f:
                self.joueurs = pickle.load(f)
        except FileNotFoundError:
            self.scores = []

# Exemple d'utilisation
jeu = Jeu()
jeu.charger('sauvegarde.pkl')  # Charge les joueurs existants

# Ajouter ou mettre à jour un joueur
nom_joueur = input("Entrez votre nom: ")
joueur = jeu.trouver_joueur(nom_joueur)
if joueur is None:
    joueur = Joueur(nom_joueur)
    jeu.ajouter_joueur(joueur)

# Mettre à jour le score du joueur
joueur.mettre_a_jour_score(10)  # Ajoute 10 points au score du joueur

# Sauvegarder les joueurs après la mise à jour
jeu.sauvegarder('sauvegarde.pkl')


