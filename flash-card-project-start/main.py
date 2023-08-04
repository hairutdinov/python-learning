from tkinter import *
from random import choice
import pandas
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}
timer = None


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    timer = window.after(3000, flip_card)


def know_btn_handler():
    to_learn.remove(current_card)
    save_words_to_learn()
    next_card()


def unknown_btn_handler():
    next_card()


def save_words_to_learn():
    with open("./data/words_to_learn.csv", "w") as file:
        df = pandas.DataFrame(data=to_learn)
        file.write(df.to_csv(index=False))

def flip_card():
    global timer
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 264, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = PhotoImage(file="images/wrong.png")
right_button_image = PhotoImage(file="images/right.png")

wrong_btn = Button(image=wrong_button_image, highlightthickness=0, command=unknown_btn_handler)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_button_image, highlightthickness=0, command=know_btn_handler)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()