

game = "hangman"
fautes = "nobre de fautes dans le jeu à ajouter" * 10

def scores():
    for faute in game:
        score = score - fautes 
        if fautes == 0:
          print("Bravo! Tu as réussi sans faute. Ton score est {0} ".format(score))
        else:
           print("Ton score est {0}".format(score))



