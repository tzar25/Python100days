from tkinter import *


def calculate():
    miles = round(float(miles_entry.get()) * 1.609, 2)
    kph_converted.config(text=miles)


window = Tk()
window.title("Miles/kph converter")
window.minsize(width=150, height=100)
window.config(padx=10, pady=10)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

equal_text = Label(text="is equal to")
equal_text.grid(column=0, row=1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(row=2, column=1)

miles_entry = Entry(width=7)
miles_entry.grid(row=0, column=1)

kph_converted = Label(text="")
kph_converted.grid(row=1, column=1)

window.mainloop()
