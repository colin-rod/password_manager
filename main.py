from tkinter import *
import csv
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]


    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered\nEmail:{email}\nPassword:{password}\nIs it okay to save?")
        if is_ok:
            with open('data.csv', 'a') as fd:
                writer = csv.writer(fd)
                writer.writerow([website, email, password])
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "xxx@gmail.com")

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=save_data)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
