from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------CSV DATA ----------------------#
try:
    data = pandas.read_csv("data/Words_to_remember.csv")
    words = data.to_dict(orient="records")

except FileNotFoundError:
    data = pandas.read_csv("data/chinese_words.csv")
    words = data.to_dict(orient="records")

current_card = {}


# ---------------------Buttons----------------------#
def known_word():
    words.remove(current_card)
    df = pandas.DataFrame(words)
    df.to_csv("data/Words_to_remember.csv", index=False)
    print(len(words))
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(language_text, text="Chinese", fill="Black")
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(word_text, text=current_card["Chinese"], fill="Black")
    flip_timer = window.after(3000, func=back_card)


def back_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(language_text, text="English", fill="White")
    canvas.itemconfig(word_text, text=current_card["English"], fill="White")


# ---------------------UI INTERFACE----------------------#


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=back_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=known_word)
tick_button.grid(row=1, column=0)
cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=1)

next_card()

window.mainloop()
