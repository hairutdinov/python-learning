from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(width=400, height=200, padx=20, pady=20)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

entry = Entry()
entry.grid(column=1, row=0)
entry.config(width=10)
entry.focus()

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def calculate():
    km_result_label["text"] = round(float(entry.get()) * 0.621371, 2)

calculate_btn = Button(text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=2)

window.mainloop()