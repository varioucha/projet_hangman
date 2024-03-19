
from tkinter import *

root = Tk()
root.title('Score')
root.geometry("260x600")

def choisir_score():
    niveau = input("choisir niveau")
    if niveau == "facile":
        score = 500
      
    elif niveau == "difficile":
        score = 1000


score_total = Label(root, textvariable= score)


choisir_score()


def scores_process():
   score_total = Label(root, text="")
   score_total= score_total + 1


titlelabel = Label(root, text="Basketball Score Keeper")
titlelabel.grid(row=0, column=3)



score_total.grid(row=2, column=0)



root.mainloop()


def scores():
  for faute in mot_a_deviner:
      score_total = score_total - nombre_erreurs
      
      
      
def fin_jeu():
    if  nombre_erreurs == 0:
        print("Bravo! Tu as réussi sans faute. Ton score est {0} ".format(score_total))
      else:
          print("Ton score est {0}".format(score_total)


