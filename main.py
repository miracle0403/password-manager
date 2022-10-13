from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=300, height=300)
photo = PhotoImage(file="logo.png")

canvas.create_image(150, 150, image=photo)
canvas.grid(column=0,row=0)

window.mainloop()

