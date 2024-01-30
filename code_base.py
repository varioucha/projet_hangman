# montrer quu'on est dans le jeu 
print("Welcome to hangman")
print("-------------------------------------------")
# liste de mot 

# changer pour que ca soit ordi qui génère les mots avec la list
mot_choisi = input("mot a faire deviner")

nombre_de_erreur = 0

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#tant que le nombre d'erreur autorisé n'est pas dépacé le jeux continue
while nombre_de_erreur < 7:
    lettre_essaie = input("essayez une lettre")
    if lettre_essaie in mot_choisi:
        print("Bravo!")
        #supp lettre de la list
    else:
        print("lettre pas dans le mot!")
        nombre_de_erreur = nombre_de_erreur + 1
