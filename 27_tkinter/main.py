from tkinter import *


def button_clicked():
    # print("I was clicked!")
    # label.config(text="Button clicked!")
    label.config(text=entered.get())


window = Tk()
window.title("GUI program")
window.minsize(width=800, height=600)
window.config(padx=30, pady=20)

# Label
label = Label(text="Label", font=("Arial", 24, "bold"))
# label.pack(side="left", expand=True)
label.grid(column=0, row=0)
label.config(padx=20, pady=20)

label["text"] = "new text"
label.config(text="Newer text")

button = Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New button", command=button_clicked)
new_button.grid(row=0, column=2)

entered = Entry(width=15)
entered.grid(row=2, column=3)

window.mainloop()
