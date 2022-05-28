import csv
import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient='records')
current_card = {}

def generate_word():
	global current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(to_learn)
	english_word = current_card["English"]
	french_word = current_card["French"]
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=french_word, fill="black")
	canvas.itemconfig(card_background, image=card_front)
	flip_timer = window.after(3000, change_card)

def change_card():
	#card_title = canvas.create_text(400, 120, text='English', fill="white", font=("Arial", 50, "italic"))
	#card_word = canvas.create_text(400, 280, text="English", fill="white", font=("Arial", 60, "bold italic"))
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=current_card["English"], fill="white")
	canvas.itemconfig(card_background, image=card_back)


window = Tk()
window.title("Language Cards")
window.minsize(800, 500)
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000,change_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 120, text='English', font=("Arial", 50, "italic"))
card_word = canvas.create_text(400, 280, text="English", font=("Arial", 60, "bold italic"))

right = PhotoImage(file="images/right.png")
button_right = Button(window, image=right, highlightthickness=0, command=generate_word)
button_right.grid(column=0, row=1)

wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, command=generate_word)
button_wrong.grid(column=1, row=1)

generate_word()




window.mainloop()

