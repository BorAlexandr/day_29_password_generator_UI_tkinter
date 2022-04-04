import json
from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_nums = [random.choice(numbers) for _ in range(nr_numbers)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = random_letters+random_nums+random_symbols
    random.shuffle(password_list)

    gen_password = "".join(password_list)

    password_text.delete(0, END)
    password_text.insert(0, gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_data():
    website = website_text.get().lower()
    try:
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
            try:
                messagebox.showinfo(title="Search results", message=f"Username/email: {data[website]['email']}\n"
                                                                    f"Password: {data[website]['password']}")
            except KeyError:
                messagebox.showinfo(title="Search results", message=f"{website} is not found")

    except FileNotFoundError:
        messagebox.showinfo(title="JSON file is not create", message="Please write at least one account")



# create function for save input values

def save():
    website = website_text.get().lower()
    email = username_text.get().lower()
    password = password_text.get().lower()
    current_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if not website or not email or not password:
        messagebox.showinfo(title="input window is empty", message="Please, write data in input window")

    else:
        try:
            # reading old and update current data
            with open("data.json", "r") as read_file:
                data = json.load(read_file)
                data.update(current_data)
            # write data in json file
            with open("data.json", "w") as write_file:
                json.dump(data, write_file, indent=4)

        except FileNotFoundError:
            # if file is not create we are creating new data.json
            with open("data.json", "w") as write_file:
                json.dump(current_data, write_file, indent=4)

        finally:
            # in any way we are clearing input fields
            website_text.delete(0, "end")
            password_text.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

# create work window
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

# download mail image in canvas
canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
# timer_text = canvas.create_text(260, 400, text="00:00", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# information data for input window
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=3)
password_label = Label(text="Password:")
password_label.grid(column=0, row=4)

# entries data
website_text = Entry(width=35)
website_text.focus()
website_text.grid(column=1, row=1, columnspan=2)

username_text = Entry(width=35)
username_text.insert(0, "example@mail.com")

username_text.grid(column=1, row=3, columnspan=2)

password_text = Entry(width=35)
password_text.grid(column=1, row=4)

# -------------------------- buttons----------------------------------#
generate_pass = Button(text="Generate password", width=32, command=generate_password)
generate_pass.grid(column=1, row=5)
data_add = Button(text="Add", width=32, command=save)
data_add.grid(column=1, row=6)
search = Button(text="Search", width=32, command=search_data)
search.grid(column=1, row=2, columnspan=2)

window.mainloop()
