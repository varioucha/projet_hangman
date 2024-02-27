from tkinter import *


#creation de la fenetre
window = Tk()
window.title("Hangman")
window.geometry("300x200")

#text
label_word = Label(window, text= "Hello",  bg="white", fg="black")
label_word.place(x=100, y=200)

#image
image_1 = PhotoImage(file="image.png")
label = Label(image=image_1)

window.mainloop()
