from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 5)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 3)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "" .join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savePassword():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if website == "" or password == "":
        messagebox.showerror(title="Error", message="ALl fields are required")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it Correct to Save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="Password saved successfully")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "vaishnav2103@gmail.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", bg="white", command=generatePassword)
password_button.grid(column=2, row=3,)

add_button = Button(text="Add", width=43, bg="white", command=savePassword)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
