import tkinter as tk
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# --------GENERATE CARD---------#
# Function that when called, chooses a random word in the series 'French"
# Takes that random word, and configs test_word to the assigned word
data = pd.read_csv("data/french_words.csv")
to_learn = data.copy()

def gen_card():
    global to_learn

    if len(to_learn) == 0:
        to_learn = data.copy()

    sample = to_learn.sample()
    current_card = sample.French.item()

    to_learn.drop(sample.index)
    
    canvas.itemconfig(test_word, text=current_card)

    return current_card

# --------UI SET UP--------- #
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, height=2, width=2, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263, image=bg_img )
canvas.grid(row=0, column=0, columnspan=2)

language_title = canvas.create_text(400, 150, text="Language", font=("Ariel", 40, "italic"))
test_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

no_button_img = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_button_img, highlightthickness=0, command=gen_card)
no_button.grid(row=1, column=0)

yes_button_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_button_img, highlightthickness=0, command=gen_card)
yes_button.grid(row=1, column=1)

window.mainloop()