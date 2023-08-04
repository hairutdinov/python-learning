from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP --------------------------- ---- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=23)
website_input.grid(column=1, row=1)
website_input.insert(0, "website.com")
website_input.focus()


def search_handler():
    website = website_input.get()
    data = {}

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



search_btn = Button(text="Search", width=13, command=search_handler)
search_btn.grid(column=2, row=1)

username_label = Label(text="Email/username:")
username_label.grid(column=0, row=2)

username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "bulat@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=23)
password_input.grid(column=1, row=3)


def generate_password():
    password = PasswordGenerator().generate()
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


generate_password_btn = Button(text="Generate Password", width=13, command=generate_password)
generate_password_btn.grid(column=2, row=3)


def add_button_handler():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    finally:
        website_input.delete(0, END)
        password_input.delete(0, END)


add_button = Button(text="Add", width=37, command=add_button_handler)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
