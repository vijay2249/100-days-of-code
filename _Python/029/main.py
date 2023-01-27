try:
    from tkinter import *
    from tkinter import messagebox
    from random import randint, sample, shuffle
    import pyperclip
except ModuleNotFoundError:
    import os
    os.system("pip install pyperclip")
    import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = sample(letters, randint(8, 10))
    password_list += sample(numbers, randint(2, 4))
    password_list += sample(symbols, randint(2, 4))
    shuffle(password_list)
    password = "".join(password_list)
    passwordEntry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website, email, password = websiteEntry.get(), emailEntry.get(), passwordEntry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Wrong Input', message='No fields should be left empty')
    else:
        msg = f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save..."
        isOk = messagebox.askokcancel(title=website, message=msg)
        if isOk:
            with open('data.txt', 'a') as f:
                f.write(f"{website} | {email} | {password}\n")
                websiteEntry.delete(0,END)
                emailEntry.delete(0,END)
                passwordEntry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

websiteLabel = Label(text='Website:')
websiteLabel.focus()
websiteLabel.grid(row=1, column=0)
email_user_label = Label(text='Email/Username:')
email_user_label.grid(row=2,column=0)
passwordLabel = Label(text='Password:')
passwordLabel.grid(row=3,column=0)


websiteEntry = Entry(width=40)
websiteEntry.grid(row=1, column=1, columnspan=2)
emailEntry = Entry(width=40)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(0, 'email id')
passwordEntry = Entry(width=40)
passwordEntry.grid(row=3, column=1, columnspan=2)


generatePass = Button(text="Generate Password", command=generate_password)
generatePass.grid(row=3, column=2)
add = Button(text='Add content', width=40, command=save)
add.grid(row=4, column=1, columnspan=2)


window.mainloop()