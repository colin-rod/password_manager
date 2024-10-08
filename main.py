from tkinter import *
import json
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
    new_data = {website:{
        "email":email,
        "password":password
    }}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as fd:
                data = json.load(fd)
        except FileNotFoundError:
            with open("data.json", "w") as fd:
                json.dump(new_data, fd, indent=4)
        except json.JSONDecodeError:
            data = new_data
            with open("data.json", "w") as fd:
                json.dump(new_data, fd, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as fd:
                json.dump(data,fd,indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = entry_website.get()
    try:
        with open("data.json","r") as fd:
            data = json.load(fd)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found")
    else:
        if website in data:
            print(website)
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for the website")




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

entry_website = Entry(width=21)
entry_website.grid(row=1, column=1)
entry_website.focus()

button_search = Button(text="Search",width=14, command=find_password)
button_search.grid(row=1, column=2)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

entry_email = Entry(width=38)
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
