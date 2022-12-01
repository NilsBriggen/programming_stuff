from tkinter import *
from os import path

PATH = path.dirname(path.abspath(__file__))

BACKGROUND_COLOR = "#B1DDC6"

#INITIALIZE WINDOW
window = Tk()
window.title("Fleshy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#CREATE CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=f"{PATH}\\images\\card_front.png")
card_back = PhotoImage(file=f"{PATH}\\images\\card_back.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#CREATE BUTTONS
right_image = PhotoImage(file=f"{PATH}\\images\\right.png")
wrong_image = PhotoImage(file=f"{PATH}\\images\\wrong.png")
right_button = Button(image=right_image, highlightthickness=0)
wrong_button = Button(image=wrong_image, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

#card image
card_image = canvas.create_image(400, 263, image=card_front)
#card title
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
#card word
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

#DISPLAY WORDS
def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text="Word", fill="white")

window.mainloop()