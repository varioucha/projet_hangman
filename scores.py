

game = "hangman"
fautes = "nombre de fautes dans le jeu à ajouter" * 10
niveau = 1


def choisir_score():
  if niveau == "facile":
    score = 500
  else:
    score = 1000

    # fgbiurj


def scores():
  for faute in game:
      score = score - fautes 
      if fautes == 0:
        print("Bravo! Tu as réussi sans faute. Ton score est {0} ".format(score))
      else:
          print("Ton score est {0}".format(score))
          

from tkinter import *

root = Tk()

class scores:
    def __init__(self, score):
        self.score = score


    def choisir_score():
      if niveau == "facile":
        score = 500
      
      elif niveau == "difficile":
        score = 1000

    def premiere_fenetre():
      global window
      window = Tk()
      window.title("Hangman")
      window.geometry("350x350")
      print("jeu ouvert")
      window.mainloop()
    
    def count_score(self):
        root = Tk()
        root.geometry("600x500")

        score_addition_easy_label = Label(root, text="Score count: ")
        score_addition_easy_label.place(x=25, y=100)

        score_addition_easy_number = Label(root, text=self.score)
        score_addition_easy_number.place(x=120, y=100)


def count_score(self):
        root = Tk()
        root.geometry("600x500")

        score_addition_easy_label = Label(root, text="Score count: ")
        score_addition_easy_label.place(x=25, y=100)

        score_addition_easy_number = Label(root, text=self.score)
        score_addition_easy_number.place(x=120, y=100)




root.mainloop()


from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()



from tkinter import *

root = Tk()
root.title('Basketball Score')
root.geometry("260x600")
point1 = Label(root, text=0)
point2 = Label(root, text=0)
def addone1():
    point1 = Label(root, text="0")
    point1 = point1 + 1
def addone2():
    point2 = Label(root, text="0")
    point2 = point2 + 1

titlelabel = Label(root, text="Basketball Score Keeper")
titlelabel.grid(row=0, column=3)

button1 = Button(root, text="Add Point", command=addone1)
button1.grid(row=1, column=0)
button2 = Button(root, text="Add Point", command=addone2)
button2.grid(row=1, column=5)

point1.grid(row=2, column=0)

point2.grid(row=2, column=5)

root.mainloop()


