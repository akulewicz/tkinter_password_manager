import tkinter
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oooooppsss", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {username} "
                           f"\n Password: {password} \nIs it ok to save?")
        if is_ok:
            with open('pass.txt', "a") as file:
                file.write(f"{website} | {username} | {password} \n")
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

generate_button = tkinter.Button(text="Generate password")
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()