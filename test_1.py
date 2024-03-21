from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
import random

nombre_erreurs = 0
MAX_ERREURS = 6
lettres_essai = []
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

from tkinter import *

# Create a single instance of Tk
root = Tk()

def premiere_fenetre():
    global window
    window = Toplevel(root)  # Use Toplevel instead of Tk for additional windows
    window.title("Hangman")
    window.geometry("350x350")
    print("jeu ouvert")

    label_word = Label(window, text="Bienvenue dans le jeu du pendu\nVoulez vous jouer?")
    label_word.place(relx=0.5, rely=0.2, anchor=CENTER)

    # boutons
    play_button = Button(window, text="Jouer", command=username_window)
    play_button.place(relx=0.5, rely=0.4, anchor=CENTER)

    exit_button = Button(window, text="Exit", command=window.destroy)
    exit_button.place(relx=0.5, rely=0.6, anchor=CENTER)

    window.mainloop()
    

def play_action():
    window_1.destroy()  # Destroy window_1, not window
    print("Play button clicked")

#username window
def username_window():
    global window_1
    window_1 = Toplevel(root)  # Use Toplevel instead of Tk for additional windows
    window_1.title("Hangman Setup")
    window_1.geometry("300x150")
    username_label = Label(window_1, text="Enter your username:")
    username_label.pack(pady=5)
    username_entry = Entry(window_1, width=30)
    username_entry.pack(pady=5)
    start_button = Button(window_1, text="Start Game", command=play_action)
    start_button.pack(pady=10)

    window_1.mainloop()

premiere_fenetre()