from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from PIL import ImageTk
from PIL import Image
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = '#fdfefe'
BLUE = "#154360"
RED = '#e74c3c '
BLACK = ' #17202a'
YELLOW = '#f1c40f'
ORANGE = '#d35400'
FONT_TYPE = 'Courier New (monospace)'

current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("data/french_words.csv") #converting csv to dataframe dict
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") #converting dataframe dict into list of dict

# canvas allows things to be layer ontop each other

#--------------turns card_______________________#

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    #print(current_card["French"]) # grabs random French word from to_learn list of dict with value french
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="black")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn) # creates list of words to learn
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#-------------UI-------------------------------#




window = Tk()
window.title("Vocab Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR,)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img) # set x and y position on canvas
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))  #writes text on image
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))  #writes text on image
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


#buttons
right_btn= PhotoImage(file="images/right.png")
right_button = Button(image=right_btn, borderwidth=0, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1,)

wrong_btn= PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_btn, borderwidth=0, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1,)

next_card()

window.mainloop()

###note that card doesn't flip to background card, both my code and solution code have this bug