try:
    from tkinter import *
    from tkinter import messagebox
    from random import randint, sample, shuffle
    import pyperclip
except ModuleNotFoundError:
    import subprocess
    subprocess.call(['pip', 'install', 'pyperclip'], shell=True)
    import pyperclip

# -------------- Error Classes ----------------------
class ResultNotFound(Exception):
    errorName = "Result(s) Not Found"
    def __init__(self, data, *args):
        super().__init__(args)
        self.website = data
    
    def __str__(self) -> str:
        return f"login details for \"{self.website}\" wesbite were not found"

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

def searchPass(website):
    try:
        assert len(website) != 0
        with open('data.txt', 'r') as f:
            fileData = f.readlines()
            websites = [item.split('|')[0].strip() for item in fileData]
            if website in websites:
                password = fileData[websites.index(website)].split("|")[-1].strip()
                email = fileData[websites.index(website)].split("|")[1].strip()
                msg = f"Details found:\nWebsite: {website}\nPassword: {password}\nEmail: {email}\nClick Ok to copy the password to clipboard"
                isOk = messagebox.askokcancel(title='Details Found', message=msg)
                if isOk:
                    pyperclip.copy(password)
            else:
                raise ResultNotFound(website)
    except AssertionError:
            pass
    except FileNotFoundError:
        pass
    except ResultNotFound as err:
        # print(err)
        messagebox.showerror(title=err.errorName, message=err)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0,column=1)

#  --------------- Labels --------------- 
websiteLabel = Label(text='Website:')
websiteLabel.focus()
websiteLabel.grid(row=1, column=0)
email_user_label = Label(text='Email/Username:')
email_user_label.grid(row=2,column=0)
passwordLabel = Label(text='Password:')
passwordLabel.grid(row=3,column=0)

# --------------- entries -------------
websiteEntry = Entry(width=40)
websiteEntry.grid(row=1, column=1, columnspan=2)
emailEntry = Entry(width=40)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(0, 'email id')
passwordEntry = Entry(width=40)
passwordEntry.grid(row=3, column=1, columnspan=2)

# ----------- BUTTONS -------------------
generatePass = Button(text="Generate", command=generate_password)
generatePass.grid(row=3, column=2)
add = Button(text='Add content', width=35, command=save)
add.grid(row=4, column=1, columnspan=2)
searchOption = Button(text='Search', command=searchPass)
searchOption = Button(text='Search', command=lambda: searchPass(websiteEntry.get()))
searchOption.grid(row=1,column=2)

window.mainloop()



# what if there are multiple accounts on same website
# error handling for that if not allowed(ideally should be allowed)
# how to access the login data for this type of multiple 