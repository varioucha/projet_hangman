from tkinter import *

window = Tk()
window.title("Hangman")
window.geometry("300x200")


label = Label(window, text= "Hello",  bg="white", fg="black")
label.place(x=100, y=200)
window.mainloop()
