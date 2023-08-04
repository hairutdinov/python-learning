import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# label
label = tkinter.Label(text="I am a label", font=("Arial", 24))
label.pack()

def btn_clicked():
    label["text"] = input.get()

# button
btn = tkinter.Button(text="Click me", command=btn_clicked)
btn.pack()

# entry
entry = tkinter.Entry(width=10)
entry.pack()

text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, "Example of multi-line text entry.")
print(text.get("1.0", tkinter.END))
text.pack()

def spinbox_used():
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

def scale_used(value):
    print(value)

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkbutton_used():
    print(checked_state.get())

checked_state = tkinter.IntVar()
checkbox = tkinter.Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checkbox.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()