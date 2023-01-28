try:
    import pandas as pd
except ModuleNotFoundError:
    import subprocess
    subprocess.check_output(['pip', 'install','pandas'], shell=True)
    import pandas as pd
finally:
    from time import time
    from tkinter import *
    from random import randint

BACKGROUND_COLOR = "#B1DDC6"
FRENCH, ENGLISH = "French", "English"
FRONT, BACK = 'Front', "Back"

try:
    words_list = pd.read_csv('./data/words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    words_list = pd.read_csv('./data/french_words.csv').to_dict(orient='records')



def generate_word():
    global selected_word, flip, words_list
    window.after_cancel(flip)
    selected_word = words_list[randint(0, len(words_list))]
    canvas.itemconfig(title, text=FRENCH, fill='black')
    canvas.itemconfig(word, text=selected_word[FRENCH], fill='black')
    canvas.itemconfig(image_card, image=card_front)
    flip = window.after(3000, update)

def correct_guess():
    global words_list, selected_word
    words_list.remove(selected_word)
    print(len(words_list))
    pd.DataFrame(words_list).to_csv('./data/words_to_learn.csv', index=False)
    generate_word()

def update():
    global selected_word
    canvas.itemconfig(title, text=ENGLISH, fill='white')
    canvas.itemconfig(word, text=selected_word[ENGLISH], fill='white')
    canvas.itemconfig(image_card, image=card_back)

window = Tk()
window.title("Project 31")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(height=526, width=800)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

img, title_, selected_word = FRONT, FRENCH, words_list[randint(0,len(words_list))]



image_card = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text=FRENCH, font=("Nunito", 40, "italic"))
word = canvas.create_text(400, 263, text=selected_word[FRENCH], font=("Nunito", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


wrongButton = Button(image=wrong_img, highlightthickness=0, command=generate_word)
wrongButton.grid(row=1, column=0)
rightButton = Button(image=right_img, highlightthickness=0, command=correct_guess)
rightButton.grid(row=1, column=1)

flip = window.after(3000, update)


window.mainloop()