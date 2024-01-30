# changer pour que ca soit ordi qui génère les mots avec la list
mot_choisi = input("hello")

nombre_de_erreur = 0

#tant que le nombre d'erreur autorisé n'est pas dépacé le jeux continue
while nombre_de_erreur < 7:
    lettre_essaie = input("fgd")
    if lettre_essaie in mot_choisi:
        print("Bravo!")
        #supp lettre de la list
    else:
        print("lettre pas dans le mot!")
        nombre_de_erreur = nombre_de_erreur + 1
