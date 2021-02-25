import tkinter as tk
from tkinter import messagebox as mbox

window = tk.Tk()

def buttonClick():
    anouce = mbox.showinfo("button clicked","you clicked the button")
    
    

label = tk.Label(window, text = "test label")
label.pack()

frame = tk.Frame(window, height=30, width=100, bg="orchid")
frame.pack()

button = tk.Button(window, text="button", command=buttonClick)
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text="check button", variable=switch)
checkbutton.pack()

entrytext = tk.StringVar()
entrytext.set("enter text here...")

entry = tk.Entry(window, width=30, textvariable=entrytext)
entry.pack()


radio1 = tk.Radiobutton(window, text="radio 1", variable=switch, value=0)
radio2 = tk.Radiobutton(window, text="radio 2", variable=switch, value=1)
radio1.pack()
radio2.pack()

window.mainloop()
