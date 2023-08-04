from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
# new_button.pack()
new_button.grid(column=2, row=0)

#Entry
entry = Entry(width=10)
print(entry.get())
# entry.pack()
entry.grid(column=3, row=2)

window.mainloop()