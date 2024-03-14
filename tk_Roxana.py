from tkinter import *
from PIL import Image, ImageTk

#creation de la fenetre
window = Tk()
window.title("Hangman")
window.geometry("600x400")


#text
label_word = Label(window, text= "Hello",  bg="white", fg="black")
label_word.place(x=100, y=200)

#creation d'un frame
frame = Frame(window)
frame.pack(padx=10, pady=10)

#intergartion de l'image
image_path = "projet_hangman/images/hangman0.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

#placement image
image_x = 200 
image_y = 150

#creation d'un canvas
canvas = Canvas(window, width=image.width, height=image.height)
canvas.pack()

# Using place to position the canvas
canvas.place(x=200, y=50)  # Adjust x et y pour changer postionnement de l'image

# Add the image to the canvas
canvas.create_image(0,0, anchor=NW, image=photo)

window.mainloop()


root = Tk() 
root.geometry("200x100") 
  
# Function for closing window 
  
  
def Close(): 
    root.destroy() 
  
  
# Button for closing 
exit_button = Button(root, text="Exit", command=Close) 
exit_button.pack(pady=20) 
  
root.mainloop()  

"""
text = Text(window)
text.insert(INSERT,"Bienvenue dans le jeu du pendu" )
text.pack()
window.mainloop()
"""
