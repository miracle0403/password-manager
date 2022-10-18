import random
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import pyperclip as pyperclip

caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']

low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-']
generated_password = []


def generate_pass():
    Blett = [random.choice(caps) for letter in range(8, 10)]
    Slett = [random.choice(low) for letter in range(6, 10)]
    Numb = [random.choice(num) for letter in range(8, 10)]
    Symb = [random.choice(symbols) for letter in range(8, 10)]
    generated_password = Blett + Slett + Numb + Symb
    passwo = ""
    for n in generated_password:
        passwo += str(n)
    pyperclip.copy(passwo)
    messagebox.showinfo(title="Alert", message=f"{passwo} copied into clipboard!")
    password_input.delete(0, END)
    password_input.insert(0, passwo)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    # get the input
    websites = website_input.get()
    email = email_input.get()
    passw = password_input.get()

    if websites == "":
        messagebox.showinfo(title="Error", message="Website field Cannot be empty!")
    elif email == "":
        messagebox.showinfo(title="Error", message="Email field Cannot be empty!")
    elif passw == "":
        messagebox.showinfo(title="Error", message="Password field Cannot be empty!")
    else:

        is_ok = messagebox.askokcancel(title=f"{websites}", message=f"Please re-check your information and make sure they are "
                                                            f"correct before saving.\nEmail: {email} \nWebsites: {websites}"
                                                            f"\nPassword: {passw}")
        if is_ok:
            print(f"website is {websites} email is {email} password is {passw}")
            # open the file for writing
            with open("passwords.txt", "a") as files:
                files.write(f"\nEmail: {email}\nWebsite: {websites} \nPassword: {passw}\n")

                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

website = Label(text="Website")
website.grid(column=0, row=1)

website_input = Entry(width=50, )
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_username = Label(text="Email/Username")
email_username.grid(column=0, row=2)

email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "lawrencemiracle72@gmail.com")

password = Label(text="Password")
password.grid(column=0, row=3, columnspan=1)

password_input = Entry(width=32)
password_input.grid(row=3, column=1)

generate_password = Button(text="Generate Password", command=generate_pass)
generate_password.grid(column=2, row=3)

add = Button(text="Add", fg="white", bg="red", width=26, command=save_password)
add.grid(column=1, row=4)



window.mainloop()
