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
# create function for save input values

def get_data(website, email, password):
    get_website = website.get()
    get_email = email.get()
    get_password = password.get()
    return get_email, get_website, get_password

def save():
    website, email, password = get_data(website_text, username_text, password_text)

    if not website or not email or not password:
        messagebox.showinfo(title="input window is empty", message="Please, write data in input window")

    else:
        is_ok = messagebox.askokcancel(title="Check parameters", message=f"Your website: {website}\n"
                                                                         f"Your email: {email}\n"
                                                                         f"Your password: {password}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
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
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# entries data
website_text = Entry(width=35)
website_text.focus()
website_text.grid(column=1, row=1, columnspan=2)

username_text = Entry(width=35)
username_text.insert(0, "example@mail.com")

username_text.grid(column=1, row=2, columnspan=2)

password_text = Entry(width=35)
password_text.grid(column=1, row=3)

# -------------------------- buttons----------------------------------#
generate_pass = Button(text="Generate password", width=32, command=generate_password)
generate_pass.grid(column=1, row=4)
data_add = Button(text="Add", width=32, command=save)
data_add.grid(column=1, row=5)

window.mainloop()
