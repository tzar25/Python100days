import random as rd
from tkinter import *
from tkinter import messagebox
import json
WHITE = "#ffffff"


def generate_password():
    """Generates a strong password randomly"""
    password_entry.delete(0, 'end')

    small_alphabet = "qwertzuiopasdfghjklyxcvbnm"
    caps_alphabet = small_alphabet.upper()
    numbers_string = "0123456789"
    specials_string = "+!%/=()<>#&@,.-*?:_[]$€|~§"

    letters = rd.randint(8, 16)
    small_letters = rd.randint(3, letters - 2)

    pw = [rd.choice(small_alphabet) for _ in range(small_letters)]
    pw += [rd.choice(caps_alphabet) for _ in range(letters - small_letters)]
    pw += [rd.choice(numbers_string) for _ in range(rd.randint(3, 7))]
    pw += [rd.choice(specials_string) for _ in range(rd.randint(1, 4))]
    rd.shuffle(pw)
    pw = "".join(pw)
    password_entry.insert(0, pw)

    window.clipboard_clear()
    window.clipboard_append(pw)


def save_password():
    """Adds the populated entries to the data file"""
    # TODO: Check if the website-user pair is already in data
    user_name = username_entry.get()
    website = website_entry.get()
    pwd = password_entry.get()
    new_data = {
        website: {
            "email": user_name,
            "password": pwd
        }
    }

    is_okay = messagebox.askokcancel(title="New entry", message=f"You entered the following:\nUser: {user_name}\n"
                                                                f"Website: {website}\nPassword: {pwd}\nDo you wish to"
                                                                f" proceed?")

    if (len(website) == 0 or len(pwd) == 0 or len(user_name) == 0) and is_okay:
        messagebox.showerror(title="Empty fields", message="Some of the fields were empty. You shouldn't save such a"
                                                           " password")
        is_okay = False

    if is_okay:
        # Exception handling and json format added on Day 30
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


def search_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website = website_entry.get()
            if website in data.keys() and data[website]["email"] == username_entry.get():
                messagebox.showinfo(message=f"Your login data for {website} is:\n"
                                            f"Email: {data[website]['email']}\n"
                                            f"Password: {data[website]['password']}", title="Your password")
            else:
                messagebox.showinfo(title="No entry", message="There is no saved data with those credentials.")
    except FileNotFoundError:
        messagebox.showerror(title="No data file", message="The data file was not found")


window = Tk()
window.title("Password manager")
window.minsize(width=400, height=400)
window.config(padx=40, pady=40, bg=WHITE)

canvas = Canvas(width=350, height=350, bg=WHITE, highlightthickness=0)
lock_image = PhotoImage(file="Logo.png")
canvas.create_image(175, 175, image=lock_image)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website:", bg=WHITE, width=15)
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:", bg=WHITE, width=15)
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg=WHITE, width=15)
password_label.grid(row=3, column=0)

website_entry = Entry(width=40)
website_entry.grid(sticky="W", row=1, column=1)
website_entry.focus()
username_entry = Entry(width=70)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "sanyi@sanyi.com")
password_entry = Entry(width=40)
password_entry.grid(sticky="W", row=3, column=1)

search_button = Button(text="Search", command=search_password, bg=WHITE, width=24)
search_button.grid(row=1, column=2, sticky="W")

generate_button = Button(text="Generate Password", command=generate_password, bg=WHITE, width=24)
generate_button.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", command=save_password, bg=WHITE, width=59)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
