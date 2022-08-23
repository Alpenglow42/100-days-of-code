from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


WHITE = '#fdfefe'
BLUE = "#154360"
RED = '#e74c3c '
BLACK = ' #17202a'
YELLOW = '#f1c40f'
ORANGE = '#d35400'
FONT_TYPE = 'Courier New (monospace)'





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_letters = [choice(letters)for _ in range(nr_letters)]
    password_symbols = [choice(symbols)for _ in range(nr_symbols)]
    password_numbers = [choice(numbers)for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)


    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# save to data.txt lookup
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        'email': email,
        'password': password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="No info in Fields", message="Please fill out all fields")

    else:
        with open("data.json","r") as data_file:

            #reading old data
            data = json.load(data_file)
            #updating old data with new data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            #saving updated data
            json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

#-------------------------search function ----------------------------#

"""to find previous website via searching in db for it. bring up info with key"""
def search():

    website = website_entry.get() #get entry from website field
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f'Website: {website}', message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #




window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=100, bg=WHITE,)

title_label = Label(text="Password Manager", fg=ORANGE, bg=WHITE, font=(FONT_TYPE, 25))
canvas = Canvas(width=200, height=200)
main_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=main_logo)
canvas.grid(column=1, row=0)

#buttons
password_button = Button(text="Password generate", width=14, highlightthickness=0, command=password_generator) #command=
password_button.grid(column=2, row=3, columnspan=2, padx=0, pady=0,)

add_button = Button(text="Add", width=40, highlightthickness=0, command =save) #command=
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, highlightthickness=0, command=search) #command=
search_button.grid(column=2, row=1, columnspan=2, padx=0, pady=0, sticky="nsew")

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=18,)
website_entry.grid(row=1, column=1, sticky="nsew")
website_entry.focus()

email_entry = Entry(width=40,)
email_entry.grid(row=2, column=1, columnspan=2, sticky="nsew")
email_entry.insert(0, "testemail@testblog.com")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1, sticky="nsew")


window.mainloop()