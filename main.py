import tkinter
import random
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {website: {
        "username": username,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooooppsss", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = tkinter.Entry(width=52)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

username_label = tkinter.Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_input = tkinter.Entry(width=52)
username_input.insert(0, "a.kulewicz@gmail.com")
username_input.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = tkinter.Entry(width=33)
password_input.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()