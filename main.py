import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

BLUE = "#2f5d62"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generating_password():

    p_entry.delete(0, len(p_entry.get()))
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list += [random.choice(numbers) for numb in range(nr_numbers)]

    random.shuffle(password_list)

    generated_password = "".join(password_list)
    p_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_information():

    data_dict = {
        w_entry.get(): {
            "Password": p_entry.get(),
            "Email": e_entry.get()}
    }

    if len(e_entry.get()) == 0 and len(p_entry.get()) == 0 and len(w_entry.get()) == 0:
        messagebox.showerror(title="Retry", message="Please fill in everything...")
    else:
        try:
            with open(f"{e_entry.get()}.json", "r") as info:
                # Load/ read data
                data = json.load(info)
        except FileNotFoundError:
            with open(f"{e_entry.get()}.json", "w") as info:
                json.dump(data_dict, info, indent=4)
        else:
            # Update dict/json
            data.update(data_dict)
            # writing in Jason file
            with open(f"{e_entry.get()}.json", "w") as info:
                json.dump(data, info, indent=4)
        finally:
            w_entry.delete(0, len(w_entry.get()))
            p_entry.delete(0, len(p_entry.get()))


# ---------------------------- UI SETUP ------------------------------- #
# ---------------------------- Search Info ---------------------------- #
def search_info():
    try:
        with open(f"{e_entry.get()}.json", "r") as info:
            data = json.load(info)
    except FileNotFoundError or UnboundLocalError:
        messagebox.showerror(title="Error", message="file not found")
    else:
        try:
            pe_info = data[w_entry.get()]
        except KeyError:
            messagebox.showerror(title="Error", message="No data found.")
        else:
            messagebox.showinfo(title=f"{w_entry.get()}", message=f'Email: {pe_info["Email"]}'
                                                              f'\nPassword: {pe_info["Password"]}')
# ---------------------------- Search Info ---------------------------- #
# Window


window = tkinter.Tk()
window.title("Password Manager")
window.config(bg=BLUE, pady=50, padx=50)

# Image
lock_image = tkinter.PhotoImage(file="logo.png")

# Canvas
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0, bg=BLUE)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# labels #

# -Website
website = tkinter.Label(text="Website:", bg=BLUE)
website.grid(row=1, column=0)
# -Email/username
email_username = tkinter.Label(text="Email/Username:", bg=BLUE)
email_username.grid(row=2, column=0)
# -Password
password = tkinter.Label(text="Password:", bg=BLUE)
password.grid(row=3, column=0)

# Entries #
w_entry = tkinter.Entry(width=25)
w_entry.focus()
w_entry.grid(row=1, column=1)

e_entry = tkinter.Entry(width=44)
e_entry.insert(0, "jmajiku@gmail.com")
e_entry.grid(row=2, column=1, columnspan=3)

p_entry = tkinter.Entry(width=25)
p_entry.grid(row=3, column=1)

# Buttons #
# Generate password
generate_password = tkinter.Button(text="Generate Password", width=15, command=generating_password)
generate_password.grid(row=3, column=2)
# Add #
add = tkinter.Button(text="Add", width=37, command=add_information)
add.grid(row=4, column=1, columnspan=3)
# Search #
search = tkinter.Button(text="Search", width=15, command=search_info)
search.grid(row=1, column=2)

window.mainloop()
