import tkinter as tk
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None

# --------GENERATE CARD---------#
# Function that when called, chooses a random word in the series 'French"
# Takes that random word, and configs test_word to the assigned word

try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

to_learn = data.copy()

def is_known():
    global to_learn

    to_learn = to_learn.drop(current_card.name)
    to_learn.to_csv("data/words_to_learn.csv", index=False)
    gen_card()

def gen_card():
    global to_learn, current_card, flip_timer

    if flip_timer is not None:
     window.after_cancel(flip_timer)
    bg_img.config(file="images/card_front.png")

    if len(to_learn) == 0:
        to_learn = data.copy()

    sample = to_learn.sample()
    current_card = sample.iloc[0]


    canvas.itemconfig(test_word, text=current_card["French"])
    canvas.itemconfig(language_title, text="French")
    # Call card flip after 3 seconds
    flip_timer = window.after(3000, card_flip)

    return current_card

# --------CARD FLIP ------#
#Function that activates after 3000ms when a new word comes up flashes.
# Canvas is configed and bg_img becomes card_back.png
# language_title is configged to 'English'
# test_word is configged to the current row we are in, but the English column item instead
# After 3000ms, it goes back

def card_flip():

    canvas.itemconfig(test_word, text=current_card["English"])
    canvas.itemconfig(language_title, text="English")
    bg_img.config(file="images/card_back.png")
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
yes_button = Button(image=yes_button_img, highlightthickness=0, command=is_known)
yes_button.grid(row=1, column=1)


gen_card()
window.mainloop()